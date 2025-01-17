"""Exceptions for the OpenHardwareMonitor API."""


class OpenHardwareMonitorError(Exception):
    """Base OpenHardwareMonitorException class."""


class UnauthorizedError(OpenHardwareMonitorError):
    """When the server does not accept the API token."""


class NotFoundError(OpenHardwareMonitorError):
    """When the server responds with 404."""


class DisconnectedError(OpenHardwareMonitorError):
    """Channel disconnected"""
