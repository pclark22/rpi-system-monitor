from fastapi import FastAPI

from monitor import SystemMonitor


app = FastAPI(
    title="Raspberry Pi System Monitor API",
    description="REST API for Raspberry Pi system information",
    version="1.0.0",
)


monitor = SystemMonitor()


@app.get("/system")
def get_system_status():
    return monitor.collect()