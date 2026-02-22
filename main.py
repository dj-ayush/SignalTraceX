import asyncio
import click
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from connector import BLEConnector
from scanner import scan_devices
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
console = Console()

@click.group()
def cli():
    """BlueSense - BLE Device Management Tool"""
    pass

@cli.command()
def scan():
    """Scan for nearby BLE devices"""
    console.print(Panel.fit("Scanning for BLE devices...", title="Device Scanner"))
    asyncio.run(scan_devices())

@cli.command()
@click.argument('address')
def connect(address):
    """Connect to a specific BLE device"""
    console.print(Panel.fit(f"Connecting to device: {address}", title="Connection"))
    connector = BLEConnector(address)
    asyncio.run(connector.connect())

@cli.command()
@click.argument('address')
def info(address):
    """Get device information"""
    console.print(Panel.fit(f"Reading device information: {address}", title="Device Info"))
    connector = BLEConnector(address)
    asyncio.run(connector.connect())
    services = asyncio.run(connector.get_services())
    if services:
        connector.display_services(services)
    asyncio.run(connector.disconnect())

@cli.command()
@click.argument('address')
@click.argument('uuid')
def read(address, uuid):
    """Read a specific characteristic"""
    console.print(Panel.fit(f"Reading characteristic {uuid} from {address}", title="Characteristic Reader"))
    connector = BLEConnector(address)
    value = asyncio.run(connector.read_characteristic(uuid))
    if value is not None:
        console.print(f"[green]Value: {value}[/green]")
    asyncio.run(connector.disconnect())

@cli.command()
@click.argument('address')
@click.argument('uuid')
@click.argument('data')
def write(address, uuid, data):
    """Write data to a specific characteristic"""
    console.print(Panel.fit(f"Writing data to characteristic {uuid} on {address}", title="Characteristic Writer"))
    connector = BLEConnector(address)
    success = asyncio.run(connector.write_characteristic(uuid, data))
    if success:
        console.print("[green]Data written successfully[/green]")
    else:
        console.print("[red]Failed to write data[/red]")
    asyncio.run(connector.disconnect())

def display_help():
    """Display help information"""
    table = Table(title="Available Commands")
    table.add_column("Command", style="cyan")
    table.add_column("Description", style="green")
    
    commands = [
        ("scan", "Scan for nearby BLE devices"),
        ("connect <address>", "Connect to a specific BLE device"),
        ("info <address>", "Get device information and services"),
        ("read <address> <uuid>", "Read a specific characteristic"),
        ("write <address> <uuid> <data>", "Write data to a specific characteristic"),
    ]
    
    for cmd, desc in commands:
        table.add_row(cmd, desc)
    
    console.print(table)

if __name__ == '__main__':
    try:
        cli()
    except Exception as e:
        console.print(f"[red]Error: {str(e)}[/red]")
        display_help() 