# Battery, firmware and mnufacturer info
import os
from dotenv import load_dotenv
import asyncio
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from connector import BLEConnector

# Load environment variables
load_dotenv()
DEVICE_ADDRESS = os.getenv("DEVICE_ADDRESS")
CHAR_BATTERY = os.getenv("CHAR_BATTERY")
CHAR_FW_VER = os.getenv("CHAR_FW_VER")
CHAR_MANUFACTURER = os.getenv("CHAR_MANUFACTURER")

console = Console()

async def read_device_info(address=None):
    """Read and display device information."""
    address = address or DEVICE_ADDRESS
    console.print(Panel.fit(f"Reading device information: {address}", title="Device Information"))
    
    connector = BLEConnector(address)
    if not await connector.connect():
        return
    
    table = Table(title="Device Information")
    table.add_column("Characteristic", style="cyan")
    table.add_column("Value", style="green")
    
    # Read battery level
    if CHAR_BATTERY:
        battery = await connector.read_characteristic(CHAR_BATTERY)
        if battery is not None:
            table.add_row("Battery Level", f"{battery}%")
    
    # Read firmware version
    if CHAR_FW_VER:
        firmware = await connector.read_characteristic(CHAR_FW_VER)
        if firmware is not None:
            table.add_row("Firmware Version", firmware)
    
    # Read manufacturer information
    if CHAR_MANUFACTURER:
        manufacturer = await connector.read_characteristic(CHAR_MANUFACTURER)
        if manufacturer is not None:
            table.add_row("Manufacturer", manufacturer)
    
    console.print(table)
    await connector.disconnect()

async def main():
    await read_device_info()

if __name__ == "__main__":
    asyncio.run(main())
