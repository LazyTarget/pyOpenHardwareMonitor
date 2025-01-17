#!/usr/bin/env python3

import asyncio
import json
from openhardwaremonitor.api import OpenHardwareMonitorAPI


async def main():
    ohm = OpenHardwareMonitorAPI('192.168.50.20', 8085)
    data = await ohm.get_data()
    print(json.dumps(data))
    await ohm.close()

if __name__ == '__main__':
    asyncio.run(main())
