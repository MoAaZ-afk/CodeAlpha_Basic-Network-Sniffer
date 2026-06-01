# Basic-Network-Sniffer

# Lightweight Python Network Sniffer

A lightweight, real-time packet sniffer written in Python using the **Scapy** library. This tool monitors network traffic, intercepts IPv4 packets, and extracts crucial Layer 3 (Network), Layer 4 (Transport), and Layer 7 (Application) information directly to your terminal.

---

## 🚀 Features

* **Layer 3 Dissection:** Extracts source and destination IPv4 addresses.
* **Layer 4 Identification:** Detects and parses specific protocol structures for **TCP**, **UDP**, and **ICMP**.
* **Payload Inspection:** Grabs a 100-character snippet of raw data payloads (Layer 7) when available.
* **Memory Efficient:** Processes packets on the fly (`store=0`) to ensure a minimal RAM footprint during long capture sessions.
* **Graceful Termination:** Handles user interrupts (`Ctrl+C`) cleanly.

---

## 🛠️ Prerequisites & Installation

### 1. Requirements

* Python 3.x
* Administrative/Root privileges (required to put your network interface card into promiscuous mode)

### 2. Dependencies

This script relies on `scapy`. You can install it via pip:

```bash
pip install scapy

```

*Note: Depending on your Operating System, Scapy may require additional system-level packet capture tools (like `libpcap` on Linux/maconOS or `Npcap` on Windows).*

---

## 💻 Usage

Because packet sniffing requires raw socket access, you **must run this script with administrative privileges**.

### On Linux / macOS:

```bash
sudo python3 sniffer.py

```

### On Windows:

Open your command prompt or PowerShell **as Administrator** and run:

```powershell
python sniffer.py

```

### Stopping the Tool:

Press `Ctrl+C` at any time to safely halt packet interception and exit the script.

---

## 📊 Output Format

The sniffer outputs captured data dynamically in the following format:

```text
Source:<Source_IP> | Dest:<Destination_IP> | Protocol:<Proto> | <L4 Details> | <Payload Snippet>

```

### Example Log Output:

```text
[*] Starting Python Network Sniffer...
[*] Press Ctrl+C to stop sniffing.
Source:192.168.1.15 | Dest:93.184.216.34 | Protocol:TCP | TCP 53214->80 | b'GET / HTTP/1.1\r\nHost: example.com...'
Source:192.168.1.1 | Dest:192.168.1.15 | Protocol:UDP | UDP 53->53214 | b'\x00\x01\x81\x80\x00\x01...'
Source:192.168.1.15 | Dest:8.8.8.8 | Protocol:ICMP | No L4 | ''

```

---

## ⚠️ Disclaimer

> [!WARNING]
> This tool is developed strictly for **educational purposes** and **authorized security testing**. Sniffing network traffic on networks you do not own or do not have explicit permission to monitor is illegal and unethical.
