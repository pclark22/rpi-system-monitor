from pprint import pprint

from system_info import (
    get_hostname,
    get_os,
    get_release,
    get_cpu_usage,
    get_memory_usage,
    get_disk_usage,
)

class SystemMonitor:

    def collect(self):
        return {
            "hostname": get_hostname(),
            "operating_system": get_os(),
            "release": get_release(),
            "cpu_usage": get_cpu_usage(),
            "memory_usage": get_memory_usage(),
            "disk_usage": get_disk_usage(),
        }

def main():
    monitor = SystemMonitor()
    system_status = monitor.collect()
    pprint(system_status, sort_dicts=False)

if __name__ == "__main__":
    main()