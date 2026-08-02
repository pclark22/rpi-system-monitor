"""
Collects Raspberry Pi system information.

This module provides functions for retrieving hardware,
operating system, network, and resource utilization data.
"""

import platform
import socket
import psutil

from datetime import timedelta, datetime


def get_hostname() -> str:
    return socket.gethostname()

def get_model() -> str | None:
    try:
        with open("/proc/device-tree/model", "r") as file:
            return file.read().replace("\x00", "").strip()
    except OSError:
        return None

def get_os() -> str:
    return platform.system()

def get_release() -> str:
    return platform.release()

def get_cpu_usage() -> float:
    return psutil.cpu_percent(interval=1)

def get_memory_usage() -> dict[str, int | float]:
    memory = psutil.virtual_memory()

    return {
        "used": memory.used,
        "total": memory.total,
        "percent": memory.percent,
    }

def get_disk_usage() -> dict[str, int | float]:
    disk = psutil.disk_usage("/")

    return {
        "used": disk.used,
        "total": disk.total,
        "percent": disk.percent,
    }
    
def get_cpu_temperature() -> float | None:
    try:
        with open("/sys/class/thermal/thermal_zone0/temp", "r") as file:
            temperature = int(file.read()) / 1000
        return round(temperature, 1)
    except OSError:
        return None   

def get_ip_address() -> str | None:
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.connect(("8.8.8.8", 80))
            return s.getsockname()[0]
    except OSError:
        return None

def get_uptime() -> str | None:
    try:
        with open("/proc/uptime") as f:
            uptime_seconds = float(f.readline().split()[0])
        return str(timedelta(seconds=int(uptime_seconds)))
    except OSError:
        return None

def get_current_time() -> str:
    return datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

def get_mac_address() -> str:
    interfaces = psutil.net_if_addrs()

    for interface, addresses in interfaces.items():
        for address in addresses:
            if address.family == psutil.AF_LINK:
                return address.address

    return "unknown"

def get_network_interfaces() -> list[str]:
    return list(psutil.net_if_addrs().keys())

def main():
    print(f"Hostname: {get_hostname()}")
    print(f"Model: {get_model()}")
    print(f"Operating System: {get_os()}")
    print(f"Release: {get_release()}")
    print(f"CPU Usage: {get_cpu_usage()}%")
    print(f"Memory Usage: {get_memory_usage()}")
    print(f"Disk Usage: {get_disk_usage()}")
    print(f"CPU Temperature: {get_cpu_temperature()}°C")
    print(f"IP Address: {get_ip_address()}")
    print(f"Uptime: {get_uptime()}")
    print(f"Current Time: {get_current_time()}")
    print(f"MAC Address: {get_mac_address()}")
    print(f"Network Interfaces: {get_network_interfaces()}")
          

if __name__ == "__main__":
    main()