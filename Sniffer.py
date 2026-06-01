import sys
import time
from scapy.all import sniff, IP, TCP, UDP, Raw

def packet_callback(packet):
    if packet.haslayer(IP):
        ip_layer = packet[IP]
        src_ip = ip_layer.src
        dst_ip = ip_layer.dst
        proto = ip_layer.proto
        
        # Determine the human-readable protocol name
        protocol_name = "Other"
        if proto == 6:
            protocol_name = "TCP"
        elif proto == 17:
            protocol_name = "UDP"
        elif proto == 1:
            protocol_name = "ICMP"

        # 2. Extract Transport Layer details (Layer 4)
        layer4_info = ""
        if packet.haslayer(TCP):
            tcp_layer = packet[TCP]
            layer4_info = f"TCP {tcp_layer.sport}->{tcp_layer.dport}"
        elif packet.haslayer(UDP):
            udp_layer = packet[UDP]
            layer4_info = f"UDP {udp_layer.sport}->{udp_layer.dport}"
        else:
            layer4_info = "No L4"

        # 3. Extract Payload (Layer 7 - Application Data)
        payload_snippet = ""
        if packet.haslayer(Raw):
            payload = packet[Raw].load
            payload_snippet = repr(payload[:100])

        print(f"Source:{src_ip} | Dest:{dst_ip} | Protocol:{protocol_name} | {layer4_info} | {payload_snippet}")
        time.sleep(0.5)

def main():
    print("[*] Starting Python Network Sniffer...")
    print("[*] Press Ctrl+C to stop sniffing.")
    
    try:
        # sniff() is a blocking function that listens indefinitely.
        # prn specifies the callback function to run on every single packet captured.
        # store=0 ensures packets are processed on the fly and not saved in RAM.
        sniff(prn=packet_callback, store=0)
    except PermissionError:
        print("[-] Error: Insufficient privileges. Please run as root/administrator.", file=sys.stderr)
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n[*] Sniffer stopped by user. Exiting.")
        sys.exit(0)

if __name__ == "__main__":
    main()