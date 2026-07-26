from pydantic import BaseModel


class CpuInfo(BaseModel):
    cpu_usage: float
    cpu_temperature: float


class MemoryInfo(BaseModel):
    memory_usage: dict


class DiskInfo(BaseModel):
    disk_usage: dict


class SystemInfo(BaseModel):
    hostname: str
    model: str
    operating_system: str
    release: str
    cpu_usage: float
    cpu_temperature: float
    memory_usage: dict
    disk_usage: dict
    ip_address: str
    mac_address: str
    interfaces: list[str]
    uptime: str
    current_time: str


class VersionInfo(BaseModel):
    application: str
    version: str


class NetworkInfo(BaseModel):
    hostname: str
    ip_address: str
    mac_address: str
    interfaces: list[str]