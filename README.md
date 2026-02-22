# 📡 SignalTraceX

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![Bluetooth](https://img.shields.io/badge/Bluetooth-Low%20Energy-0082FC?logo=bluetooth&logoColor=white)
![Networking](https://img.shields.io/badge/Domain-Computer%20Networks-green)
![CLI](https://img.shields.io/badge/Interface-CLI-black)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Stars](https://img.shields.io/github/stars/dj-ayush/SignalTraceX?style=social)

**SignalTraceX** is a developer-focused **Bluetooth Low Energy (BLE) discovery, monitoring, and diagnostics tool** built using Python.  
The project is designed to explore and analyze **BLE communication at the protocol level**, including device discovery, connection handling, characteristic inspection, and real time data monitoring.

This project was built **out of personal interest** to deeply understand **BLE, IoT communication, and Computer Networks concepts** through hands on experimentation.

---

## ✨ Core Features

- 📡 BLE device discovery and scanning  
- 🔗 BLE connection and session management  
- 🔋 Read static device information (battery, firmware, manufacturer)  
- 📊 Real-time characteristic monitoring  
- 🖥️ Lightweight command-line interface (CLI)  
- 🧪 Diagnostics-first design for learning and debugging  

---

## 🛠️ Tech Stack

- **Language**: Python 3.8+  
- **Protocol**: Bluetooth Low Energy (BLE – GATT)  
- **Interface**: Command Line Interface (CLI)  
- **Environment**: Python Virtual Environment (venv)  

---

## 📁 Project Structure

SignalTraceX/  
├── scanner.py        - BLE device discovery  
├── connector.py      - BLE connection management  
├── static_info.py    - Read static device information  
├── reader.py         - Monitor device characteristics  
├── main.py           - Main CLI entry point  
├── requirements.txt  - Python dependencies  
├── .gitignore  
└── README.md  

---

## ⚙️ Getting Started

### 1. Clone the repository

git clone https://github.com/dj-ayush/SignalTraceX.git  
cd SignalTraceX  

### 2. Create and activate a virtual environment

python -m venv venv  

Windows:  
venv\Scripts\activate  

macOS / Linux:  
source venv/bin/activate  

### 3. Install dependencies

pip install -r requirements.txt  

---

## 🔧 BLE Device Configuration

SignalTraceX is **device-agnostic**.  
Instead of hardcoding values, BLE-specific parameters are **externally configurable**, allowing the tool to work with **any BLE peripheral**.

Create a `.env` file in the project root and define the following:

DEVICE_ADDRESS=XX:XX:XX:XX:XX:XX  
CHAR_BATTERY=XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX  
CHAR_FW_VER=XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX  
CHAR_MANUFACTURER=XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX  

### What these values represent:

- **DEVICE_ADDRESS:** The MAC address of the target BLE device you want to connect to.

- **CHAR_BATTERY:** UUID of the Battery Level characteristic (typically under the Battery Service).

- **CHAR_FW_VER:**  UUID representing the Firmware Version characteristic.

- **CHAR_MANUFACTURER:**  UUID for Manufacturer Name or vendor-specific metadata.

This approach makes SignalTraceX:
- reusable across multiple devices  
- safer to experiment with  
- closer to real-world diagnostic tooling  

---

## ▶️ Usage

Scan for nearby BLE devices:
python scanner.py  

Read static device information:
python static_info.py  

Monitor device characteristics:
python reader.py  

Run the complete application:
python main.py  

---

## 🎯 Learning Focus

- BLE architecture (GATT, services, characteristics)  
- Device discovery and connection lifecycles  
- Real-time BLE data flow  
- Protocol-level debugging  
- Applying Computer Networks concepts to IoT systems  

---

## 🤝 Contributing

We welcome contributions!

1. Fork the repo
2. Create a new branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -m "Added feature"`
4. Push to your branch: `git push origin feature-name`
5. Create a pull request 🚀
---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

> Built with ❤️ by [@dj-ayush](https://github.com/dj-ayush)
