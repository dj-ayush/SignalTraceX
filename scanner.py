import asyncio
from bleak import BleakScanner
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

async def scan_devices():
    console.print(Panel.fit("Scanning for BLE devices...", title="Device Scanner"))

    devices = {}

    def detection_callback(device, advertisement_data):
        devices[device.address] = {
            "name": device.name or "Unknown",
            "address": device.address,
            "rssi": advertisement_data.rssi,
            "uuids": advertisement_data.service_uuids or [],
            "manufacturer": bool(advertisement_data.manufacturer_data),
        }

    scanner = BleakScanner(detection_callback)
    await scanner.start()
    await asyncio.sleep(5)
    await scanner.stop()

    if not devices:
        console.print("[yellow]No devices found[/yellow]")
        return

    table = Table(title="Discovered BLE Devices")
    table.add_column("Name", style="cyan")
    table.add_column("Address", style="green")
    table.add_column("RSSI", style="yellow")
    table.add_column("Details", style="white")

    for d in devices.values():
        details = []
        if d["uuids"]:
            details.append(f"Services: {len(d['uuids'])}")
        if d["manufacturer"]:
            details.append("Manufacturer Data")

        table.add_row(
            d["name"],
            d["address"],
            f"{d['rssi']} dBm" if d["rssi"] is not None else "N/A",
            " | ".join(details) if details else "No extra data"
        )

    console.print(table)

if __name__ == "__main__":
    asyncio.run(scan_devices())