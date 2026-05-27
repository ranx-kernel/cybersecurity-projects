from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP, ICMP
from colorama import Fore, Style, init
from datetime import datetime
import pandas as pd
import os

# Initialize colorama
init(autoreset=True)

# Packet counters
packet_count = 0
tcp_count = 0
udp_count = 0
icmp_count = 0

# Suspicious ports
suspicious_ports = [21, 23, 445, 3389]

# CSV file
csv_file = "packets.csv"

# Create CSV if not exists
if not os.path.exists(csv_file):
    df = pd.DataFrame(columns=[
        "Timestamp",
        "Source IP",
        "Destination IP",
        "Protocol",
        "Source Port",
        "Destination Port"
    ])
    df.to_csv(csv_file, index=False)


def process_packet(packet):
    global packet_count, tcp_count, udp_count, icmp_count

    packet_count += 1

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    source_ip = "N/A"
    destination_ip = "N/A"
    protocol = "Other"
    source_port = "N/A"
    destination_port = "N/A"

    print(Fore.YELLOW + f"\n======= Packet #{packet_count} =======")
    print(Fore.CYAN + f"Timestamp        : {timestamp}")

    # IP Layer
    if packet.haslayer(IP):

        ip_layer = packet[IP]

        source_ip = ip_layer.src
        destination_ip = ip_layer.dst

        print(Fore.CYAN + f"Source IP        : {source_ip}")
        print(Fore.CYAN + f"Destination IP   : {destination_ip}")

        # TCP
        if packet.haslayer(TCP):

            tcp_count += 1
            protocol = "TCP"

            tcp_layer = packet[TCP]

            source_port = tcp_layer.sport
            destination_port = tcp_layer.dport

            print(Fore.GREEN + "Protocol         : TCP")
            print(Fore.GREEN + f"Source Port      : {source_port}")
            print(Fore.GREEN + f"Destination Port : {destination_port}")

        # UDP
        elif packet.haslayer(UDP):

            udp_count += 1
            protocol = "UDP"

            udp_layer = packet[UDP]

            source_port = udp_layer.sport
            destination_port = udp_layer.dport

            print(Fore.BLUE + "Protocol         : UDP")
            print(Fore.BLUE + f"Source Port      : {source_port}")
            print(Fore.BLUE + f"Destination Port : {destination_port}")

        # ICMP
        elif packet.haslayer(ICMP):

            icmp_count += 1
            protocol = "ICMP"

            print(Fore.RED + "Protocol         : ICMP")

        # Suspicious Port Detection
        if destination_port in suspicious_ports:

            print(Fore.RED + Style.BRIGHT +
                  f"⚠ Suspicious Port Detected: {destination_port}")

        # Payload Preview
        payload = bytes(packet.payload)

        if payload:
            print(Fore.MAGENTA +
                  f"Payload Preview  : {payload[:50]}")

    # Statistics
    print(Fore.YELLOW + "\n===== Packet Statistics =====")
    print(Fore.YELLOW + f"Total Packets : {packet_count}")
    print(Fore.GREEN + f"TCP Packets   : {tcp_count}")
    print(Fore.BLUE + f"UDP Packets   : {udp_count}")
    print(Fore.RED + f"ICMP Packets  : {icmp_count}")

    # Save logs to TXT
    with open("packets_log.txt", "a", encoding="utf-8") as log_file:

        log_file.write(
            f"\nPacket #{packet_count}\n"
            f"Timestamp: {timestamp}\n"
            f"Source IP: {source_ip}\n"
            f"Destination IP: {destination_ip}\n"
            f"Protocol: {protocol}\n"
            f"Source Port: {source_port}\n"
            f"Destination Port: {destination_port}\n"
        )

    # Save to CSV
    packet_data = pd.DataFrame([{
        "Timestamp": timestamp,
        "Source IP": source_ip,
        "Destination IP": destination_ip,
        "Protocol": protocol,
        "Source Port": source_port,
        "Destination Port": destination_port
    }])

    packet_data.to_csv(csv_file, mode='a',
                       header=False, index=False)


print(Fore.YELLOW + "\nStarting Advanced Network Sniffer...\n")

# Start sniffing
sniff(prn=process_packet, store=False, filter="ip")