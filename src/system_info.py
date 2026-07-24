import platform
import socket
import psutil

def get_hostname():
    return socket.gethostname()

def get_os():
    return platform.system()

def get_release():
    return platform.release()

def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

def get_memory_usage():
    return psutil.virtual_memory().percent

def get_disk_usage():
    return psutil.disk_usage("/").percent

def get_cpu_temperature():
    with open("/sys/class/thermal/thermal_zone0/temp", "r") as file:
        temperature = int(file.read()) / 1000
    return temperature


def main():
    print(f"Hostname: {get_hostname()}")
    print(f"Operating System: {get_os()}")
    print(f"Release: {get_release()}")
    print(f"CPU Usage: {get_cpu_usage()}%")
    print(f"Memory Usage: {get_memory_usage}%")
    print(f"Disk Usage: {get_disk_usage()}%")
    print(f"CPU Temperature: {get_cpu_temperature()}°C")

if __name__ == "__main__":
    main()