from fastapi import FastAPI
from monitor import SystemMonitor
from models import (
    CpuInfo,
    MemoryInfo,
    DiskInfo,
    SystemInfo,
    VersionInfo,
    NetworkInfo,
)


app = FastAPI(
    title="Raspberry Pi System Monitor API",
    description=""""
A REST API for monitoring Raspberry Pi hardware and operating system
information.

The API provides endpoints for retrieving CPU, memory, disk, network,
and overall system information in JSON format.

This project demonstrates REST API design using FastAPI and automatic
OpenAPI documentation.
""",
    version="1.0.0",
)

monitor = SystemMonitor()

@app.get(
    "/health",
    summary="Health check",
    description="""
Returns a simple status value indicating that the API is running.

This endpoint can be used by monitoring software or load balancers 
to verify that the service is available.
""",
    response_description="API health status",
    tags=["General"],
    )
def health():
    return {"status": "ok"}

@app.get(
    "/version", 
    response_model=VersionInfo,
    summary="Get API version",
    description="""
Returns the application name and current API version.

This endpoint is useful for confirming which version of the API
is deployed.
""",
    response_description="Application version information",
    tags=["General"],
    )
def version():
    return {
        "application": "Raspberry Pi System Monitor API",
        "version": "1.0.0"
    }

@app.get(
    "/system", 
    response_model=SystemInfo,
    summary="Get complete system information",
    description="""
Returns a complete snapshot of the Raspberry Pi.

The response combines operating system, processor, memory,
storage, and network information into a single JSON object.

Use this endpoint when an application requires a comprehensive
view of the device.
""",
    response_description="Complete system status",
    tags=["System"],
    )
def system():
    return monitor.system()

@app.get(
    "/cpu",
    response_model=CpuInfo,
    summary="Get CPU information",
    description="""
Returns current processor metrics, including CPU utilization
and temperature.
""",
    response_description="CPU metrics",
    tags=["Hardware"],
    )
def cpu():
    return monitor.cpu()

@app.get(
    "/memory", 
    response_model=MemoryInfo,
    summary="Get memory information",
    description="""
Returns current memory metrics, including memory used, total 
memory, and percent used.
""",
    response_description="Memory usage",
    tags=["Hardware"]
    )
def memory():
    return monitor.memory()

@app.get(
    "/disk", 
    response_model=DiskInfo,
    summary="Get disk information",
    description="""
Returns filesystem capacity, used space, free space, and 
utilization percentage.
""",
    response_description="Disk usage",
    tags=["Hardware"]
    )
def disk():
    return monitor.disk()

@app.get(
    "/network", 
    response_model=NetworkInfo,
    summary="Get network information",
    description="""
Returns network configuration, including IP address, MAC address,
and available interfaces.
""",
    response_description="Network information",
    tags=["Network"],
    )
def network():
    return monitor.network()