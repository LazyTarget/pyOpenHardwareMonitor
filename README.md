# pyOpenHardwareMonitor

Python3 library for getting data from [Open Hardware Monitor](https://openhardwaremonitor.org/) and [Libre Hardware Monitor](https://github.com/LibreHardwareMonitor/LibreHardwareMonitor)

## Install

```
pip3 install pyopenhardwaremonitor
```

## Example

```
import asyncio
import json
from pyopenhardwaremonitor.api import OpenHardwareMonitorAPI

async def main():
    ohm = OpenHardwareMonitorAPI('192.168.1.114', 8085)
    data = await ohm.get_data()
    print(json.dumps(data))
    await ohm.close()

if __name__ == '__main__':
    asyncio.run(main())

```

For a more detailed example, see `example.py`
