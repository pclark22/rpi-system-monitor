import platform
import socket
import psutil
from datetime import timedelta, datetime

def get_hostname():
    return socket.gethostname()

def get_model():
    try:
        with open("/proc/device-tree/model", "r") as file:
            return file.read().replace("\x00", "").strip()
    except OSError:
        return "Unavailable"

def get_os():
    return platform.system()

def get_release():
    return platform.release()

def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

def get_memory_usage():
    memory = psutil.virtual_memory()

    return {
        "used": memory.used,
        "total": memory.total,
        "percent": memory.percent,
    }

def get_disk_usage():
    disk = psutil.disk_usage("/")

    return {
        "used": disk.used,
        "total": disk.total,
        "percent": disk.percent,
    }
    
def get_cpu_temperature():
    with open("/sys/class/thermal/thermal_zone0/temp", "r") as file:
        temperature = int(file.read()) / 1000
    return round(temperature, 1)

def get_ip_address():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.connect(("8.8.8.8", 80))
            return s.getsockname()[0]
    except OSError:
        return "Unavailable"

def get_uptime():
    try:
        with open("/proc/uptime") as f:
            uptime_seconds = float(f.readline().split()[0])
        return str(timedelta(seconds=int(uptime_seconds)))
    except OSError:
        return "Unavailable"

def get_current_time():
    return datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

def main():
    print(f"Hostname: {get_hostname()}")
    print(f"Model: {get_model()}")
    print(f"Operating System: {get_os()}")
    print(f"Release: {get_release()}")
    print(f"CPU Usage: {get_cpu_usage()}%")
    print(f"Memory Usage: {get_memory_usage()}%")
    print(f"Disk Usage: {get_disk_usage()}%")
    print(f"CPU Temperature: {get_cpu_temperature()}°C")
    print(f"IP Address: {get_ip_address()}")
    print(f"Uptime: {get_uptime()}")
    print(f"Current Time: {get_current_time()}")
          

if __name__ == "__main__":
    main()