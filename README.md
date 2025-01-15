# pyOpenHardwareMonitor

Python3 library for getting data from [Open Hardware Monitor](https://openhardwaremonitor.org/) and [Libre Hardware Monitor](https://github.com/LibreHardwareMonitor/LibreHardwareMonitor)

## Install

```
pip3 install pyOpenHardwareMonitor
```

## Example

```
import asyncio
import json
from openhardwaremonitor import OpenHardwareMonitor

async def main():
    ohm = OpenHardwareMonitor('192.168.1.114', 8085)
    data = await ohm.get_data()
    json.dumps(data)
    await ohm._api.close()

if __name__ == '__main__':
    asyncio.run(main())
```
