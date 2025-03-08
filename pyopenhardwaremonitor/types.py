"""Types for the OpenHardwareMonitor integration."""

from enum import Enum
from typing import TypedDict


class SensorType(str, Enum):
    """What kind of sensor is this."""

    # Copied from `SensorType` enum in: https://github.com/LibreHardwareMonitor/LibreHardwareMonitor/blob/master/LibreHardwareMonitorLib/Hardware/ISensor.cs

    Voltage = "Voltage"  # V
    Current = "Current"  # A
    Power = "Power"  # W
    Clock = "Clock"  # MHz
    Temperature = "Temperature"  # °C
    Load = "Load"  # %
    Frequency = "Frequency"  # Hz
    Fan = "Fan"  # RPM
    Flow = "Flow"  # L/h
    Control = "Control"  # %
    Level = "Level"  # %
    Factor = "Factor"  # 1
    Data = "Data"  # GB = 2^30 Bytes
    SmallData = "SmallData"  # MB = 2^20 Bytes
    Throughput = "Throughput"  # B/s
    TimeSpan = "TimeSpan"  # Seconds
    Energy = "Energy"  # milliwatt-hour (mWh)
    Noise = "Noise"  # dBA
    Conductivity = "Conductivity"  # µS/cm
    Humidity = "Humidity"  # %


class SensorNode(TypedDict):
    """Describes a data point node (smallest descendant, with info about their parents)."""

    id: int | None
    Text: str | None
    Min: str | None
    Value: str | None
    Max: str | None
    ImageURL: str | None

    SensorId: str | None
    Type: SensorType | None

    ComputerName: str
    ParentNames: list[str]
    FullName: str


class DataNode(TypedDict):
    """Describes a node in the data tree."""

    id: int
    Text: str
    Min: str
    Value: str
    Max: str
    ImageURL: str
    Children: list["DataNode"]
    SensorId: str | None
    Type: SensorType | str | None
