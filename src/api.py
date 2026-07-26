from fastapi import FastAPI
from monitor import SystemMonitor

app = FastAPI(
    title="Raspberry Pi System Monitor API",
    description="REST API for Raspberry Pi system information, including CPU, model, memory, and OS metrics.",
    version="1.0.0",
)


monitor = SystemMonitor()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/system")
def system():
    return monitor.system()

@app.get("/cpu")
def cpu():
    return monitor.cpu()

@app.get("/memory")
def memory():
    return monitor.memory()

@app.get("/disk")
def disk():
    return monitor.disk()