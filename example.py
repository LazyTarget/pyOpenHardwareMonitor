#!/usr/bin/env python3
import asyncio
import json
from pyopenhardwaremonitor.api import OpenHardwareMonitorAPI


async def main(host=None, port=8085):
    """Main example on using pyOpenHardwareMonitor"""
    host = host or get_current_ip()
    print("Running against: ", host, port)

    # Example when using `async with` syntax
    async with OpenHardwareMonitorAPI(host, port) as api:
        data = await api.get_data()
        j = json.dumps(data)
        print(j)
        return j

    # Example with explicit method calls
    # api = OpenHardwareMonitorAPI(host, port)
    # data = await api.get_data()
    # await api.close()
    # j = json.dumps(data)
    # print(j)
    # return j


def get_current_ip() -> str:
    """Gets the local IP-address of this machine"""
    import socket

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return str(s.getsockname()[0])


if __name__ == "__main__":
    # if running on Windows
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    # Run main with async
    asyncio.run(main())
