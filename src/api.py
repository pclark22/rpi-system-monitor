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
    description="REST API for Raspberry Pi system information, including CPU, model, memory, and OS metrics.",
    version="1.0.0",
)


monitor = SystemMonitor()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/version", response_model=VersionInfo)
def version():
    return {
        "application": "Raspberry Pi System Monitor API",
        "version": "1.0.0"
    }

@app.get("/system", response_model=SystemInfo)
def system():
    return monitor.system()

@app.get("/cpu", response_model=CpuInfo)
def cpu():
    return monitor.cpu()

@app.get("/memory", response_model=MemoryInfo)
def memory():
    return monitor.memory()

@app.get("/disk", response_model=DiskInfo)
def disk():
    return monitor.disk()

@app.get("/network", response_model=NetworkInfo)
def network():
    return monitor.network()