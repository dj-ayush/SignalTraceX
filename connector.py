import os
from dotenv import load_dotenv
import asyncio
from bleak import BleakClient
from rich.console import Console
from rich.table import Table

# Load environment variables
load_dotenv()
DEVICE_ADDRESS = os.getenv("DEVICE_ADDRESS")
console = Console()

class BLEConnector:
    def __init__(self, address=None):
        self.address = address or DEVICE_ADDRESS
        self.client = None
        self.connected = False

    async def connect(self):
        """Establish connection to the BLE device."""
        try:
            self.client = BleakClient(self.address, timeout=20.0)
            self.connected = await self.client.connect()
            if self.connected:
                console.print(f"[green]Successfully connected to {self.address}[/green]")
                return True
            else:
                console.print(f"[red]Failed to connect to {self.address}[/red]")
                return False
        except Exception as e:
            console.print(f"[red]Connection error: {str(e)}[/red]")
            return False

    async def disconnect(self):
        """Disconnect from the BLE device."""
        if self.client and self.connected:
            await self.client.disconnect()
            self.connected = False
            console.print("[yellow]Disconnected from device[/yellow]")

    async def read_characteristic(self, uuid):
        """Read a characteristic value from the device."""
        if not self.connected:
            if not await self.connect():
                return None
        
        try:
            data = await self.client.read_gatt_char(uuid)
            return data.decode("utf-8") if isinstance(data, bytes) else data
        except Exception as e:
            console.print(f"[red]Error reading characteristic {uuid}: {str(e)}[/red]")
            return None

    async def write_characteristic(self, uuid, data):
        """Write data to a characteristic."""
        if not self.connected:
            if not await self.connect():
                return False
        
        try:
            await self.client.write_gatt_char(uuid, data)
            return True
        except Exception as e:
            console.print(f"[red]Error writing to characteristic {uuid}: {str(e)}[/red]")
            return False

    async def get_services(self):
        """Get all services and characteristics from the device."""
        if not self.connected:
            if not await self.connect():
                return None
        
        try:
            services = await self.client.get_services()
            return services
        except Exception as e:
            console.print(f"[red]Error getting services: {str(e)}[/red]")
            return None

    def display_services(self, services):
        """Display services and characteristics in a formatted table."""
        if not services:
            return

        table = Table(title="Device Services and Characteristics")
        table.add_column("Service UUID", style="cyan")
        table.add_column("Characteristic UUID", style="green")
        table.add_column("Properties", style="yellow")

        for service in services:
            for char in service.characteristics:
                table.add_row(
                    str(service.uuid),
                    str(char.uuid),
                    ", ".join(char.properties)
                )

        console.print(table)

# Example usage
async def main():
    connector = BLEConnector()
    services = await connector.get_services()
    if services:
        connector.display_services(services)
    await connector.disconnect()

if __name__ == "__main__":
    asyncio.run(main())
async def connect(self):
    if not self.address:
        console.print("[red]No DEVICE_ADDRESS provided[/red]")
        return False