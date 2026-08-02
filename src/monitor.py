import time
import argparse
import subprocess
import json

from system_info import (
    get_hostname,
    get_model,
    get_os,
    get_release,
    get_cpu_usage,
    get_memory_usage,
    get_disk_usage,
    get_cpu_temperature,
    get_ip_address,
    get_uptime,
    get_current_time,
    get_mac_address,
    get_network_interfaces,
)


class SystemMonitor:

    def cpu(self) -> dict:
        """Return current CPU metrics."""
        return {
            "cpu_usage": get_cpu_usage(),
            "cpu_temperature": get_cpu_temperature(),
        }

    def memory(self) -> dict:
        """Return current memory metrics."""
        return {
            "memory_usage": get_memory_usage(),
        }

    def disk(self) -> dict:
        """Return current disk metrics."""
        return {
            "disk_usage": get_disk_usage(),
        }

    def system(self) -> dict:
        """Return all current system metrics."""
        return {
            "hostname": get_hostname(),
            "model": get_model(),
            "operating_system": get_os(),
            "release": get_release(),
            **self.cpu(),
            **self.memory(),
            **self.disk(),
            "ip_address": get_ip_address(),
            "uptime": get_uptime(),
            "current_time": get_current_time(),
            "mac_address": get_mac_address(),
            "interfaces": get_network_interfaces(),
        }

    def network(self) -> dict:
        """Return current network metrics."""
        return {
            "hostname": get_hostname(),
            "ip_address": get_ip_address(),
            "mac_address": get_mac_address(),
            "interfaces": get_network_interfaces()
        }

def bytes_to_gb(bytes_value) -> float:
    return round(bytes_value / (1024 ** 3), 1)

def display_report(system_status):
    """Display a formatted system status report."""

    print("-" * 40)
    print("      Raspberry Pi System Monitor")
    print("-" * 40)

    print(f"{'Hostname':18}: {system_status['hostname']}")
    print(f"{'Model':18}: {system_status['model']}")
    print(f"{'Operating System':18}: {system_status['operating_system']}")
    print(f"{'Kernel':18}: {system_status['release']}")

    print()

    print(f"{'CPU Usage':18}: {system_status['cpu_usage']:.1f}%")
   
    memory = system_status["memory_usage"]

    print(
        f"{'Memory':18}: "
        f"{bytes_to_gb(memory['used'])} GB / "
        f"{bytes_to_gb(memory['total'])} GB "
        f"({memory['percent']:.1f}%)"
    )

    disk = system_status["disk_usage"]

    print(
        f"{'Disk':18}: "
        f"{bytes_to_gb(disk['used'])} GB / "
        f"{bytes_to_gb(disk['total'])} GB "
        f"({disk['percent']:.1f}%)"
    )

    temp = system_status["cpu_temperature"]

    if temp is None:
        print(f"{'CPU Temperature':18}: Unavailable")
    else:
        print(f"{'CPU Temperature':18}: {temp:.1f} °C")

    print()

    print(f"{'IP Address':18}: {system_status['ip_address']}")
    print(f"{'MAC Address':18}: {system_status['mac_address']}")
    print(f"{'Network Interfaces':18}: {system_status['interfaces']}")
    print(f"{'Uptime':18}: {system_status['uptime']}")
    print(f"{'Current Time':18}: {system_status['current_time']}")

    print("-" * 40)

def clear_screen() -> None:
    subprocess.run(["clear"])

def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Raspberry Pi System Monitor"
    )

    parser.add_argument(
        "--watch",
        action="store_true",
        help="Continuously monitor system status"
    )

    parser.add_argument(
        "--interval",
        type=int,
        default=5,
        help="Refresh interval in seconds"
    )

    parser.add_argument(
        "--json",
        action="store_true",
        help="Display output as JSON"
    )

    return parser.parse_args()

def display_json(system_status: dict) -> None:
    print(json.dumps(system_status, indent=4))

def main() -> None:

    args = parse_arguments()
    monitor = SystemMonitor()

    if args.watch:
        try:
            while True:
                clear_screen()

                system_status = monitor.system()
                display_report(system_status)

                print(f"\nRefreshing every {args.interval} seconds...")
                time.sleep(args.interval)

        except KeyboardInterrupt:
            print("\nMonitoring stopped.")

    else:
        system_status = monitor.system()

        if args.json:
            display_json(system_status)
        else:
            display_report(system_status)

if __name__ == "__main__":
    main()