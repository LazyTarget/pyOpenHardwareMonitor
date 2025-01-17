import asyncio
import logging
import random

import aiohttp
from aiohttp.client_exceptions import ClientResponseError
from yarl import URL

from .exceptions import NotFoundError, OpenHardwareMonitorError, UnauthorizedError

_LOGGER = logging.getLogger(__name__)


class OpenHardwareMonitorAPI:

    DEFAULT_TIMEOUT = 10

    def __init__(
        self,
        host,
        port,
        loop=None,
        session=None,
        timeout=DEFAULT_TIMEOUT,
        retry_count=3,
        retry_delay=None
    ):
        self._timeout = timeout
        self._close_session = False
        self.session = session

        if self.session is None:
            loop = loop or asyncio.get_event_loop()
            self.session = aiohttp.ClientSession(raise_for_status=True)
            self._close_session = True

        self._retry_count = retry_count
        self._retry_delay = retry_delay or (lambda attempt: 3**attempt + random.uniform(0, 3))

        self.API_URL = URL(f"http://{host}:{port}/")

    def base_headers(self):
        return {
            "content-type": "application/json;charset=UTF-8",
            "accept": "application/json, text/plain, */*",
        }

    async def request(self, *args, **kwargs):
        """Perform request with error wrapping."""
        try:
            return await self.raw_request(*args, **kwargs)
        except ClientResponseError as error:
            if error.status in [401, 403]:
                raise UnauthorizedError from error
            if error.status == 404:
                raise NotFoundError from error
            raise OpenHardwareMonitorError from error
        except Exception as error:
            raise OpenHardwareMonitorError from error

    async def raw_request(  # pylint: disable=too-many-arguments
        self, uri, params=None, data=None, method="GET", attempt: int = 1
    ):
        """Perform request."""
        async with self.session.request(
            method,
            self.API_URL.join(URL(uri)).update_query(params),
            json=data,
            headers=self.base_headers(),
            timeout=self._timeout,
        ) as response:
            _LOGGER.debug("Request %s, status: %s", response.url, response.status)

            if response.status == 429:
                if attempt <= self._retry_count:
                    delay = self._retry_delay(attempt)
                    _LOGGER.info("Request limit exceeded, retrying in %s second", delay)
                    await asyncio.sleep(delay)
                    return await self.raw_request(uri, params, data, method, attempt=attempt + 1)
                raise OpenHardwareMonitorError("Request limit exceeded")

            content = None
            if "Content-Type" in response.headers and "application/json" in response.headers["Content-Type"]:
                content = await response.json()
            else:
                content = await response.read()
            _LOGGER.debug("Response %s, status: %s", response.url, response.status)
            _LOGGER.debug("Response content: %s", content)
            return content

    async def get_data(self):
        json = await self.request("data.json")
        return json

    async def close(self):
        """Close the session."""
        if self.session and self._close_session:
            await self.session.close()
