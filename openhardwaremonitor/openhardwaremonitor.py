from .api import API

class OpenHardwareMonitor:
    def __init__(self, *args, **kwargs):
        """Initialize the client."""
        self._api = API(*args, **kwargs)
    
    async def get_data(self):
        json = await self._api.request(f"data.json")
        return json
    