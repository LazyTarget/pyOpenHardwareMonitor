#!/usr/bin/env python3

import asyncio
import json
from openhardwaremonitor import OpenHardwareMonitor


async def main():
    ohm = OpenHardwareMonitor('192.168.1.114', 8085)
    data = await ohm.get_data()
    print(json.dumps(data))
    await ohm._api.close()

if __name__ == '__main__':
    asyncio.run(main())
