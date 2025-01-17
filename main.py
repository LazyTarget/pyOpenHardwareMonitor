#!/usr/bin/env python3

import asyncio
import json
from openhardwaremonitor import openhardwaremonitor


async def main():
    ohm = openhardwaremonitor.OpenHardwareMonitor('192.168.50.20', 8085)
    data = await ohm.get_data()
    print(json.dumps(data))
    await ohm._api.close()

if __name__ == '__main__':
    asyncio.run(main())
