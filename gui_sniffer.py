from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP, ICMP
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from threading import Thread
from datetime import datetime

# Packet counters
packet_count = 0
tcp_count = 0
udp_count = 0
icmp_count = 0

# Running flag
sniffing = False


# Function to display packets
def process_packet(packet):
    global packet_count, tcp_count, udp_count, icmp_count

    packet_count += 1

    timestamp = datetime.now().strftime("%H:%M:%S")

    output = f"\n===== Packet #{packet_count} =====\n"
    output += f"Time: {timestamp}\n"

    if packet.haslayer(IP):

        ip_layer = packet[IP]

        output += f"Source IP      : {ip_layer.src}\n"
        output += f"Destination IP : {ip_layer.dst}\n"

        # TCP
        if packet.haslayer(TCP):

            tcp_count += 1

            tcp_layer = packet[TCP]

            output += "Protocol       : TCP\n"
            output += f"Source Port    : {tcp_layer.sport}\n"
            output += f"Destination Port: {tcp_layer.dport}\n"

        # UDP
        elif packet.haslayer(UDP):

            udp_count += 1

            udp_layer = packet[UDP]

            output += "Protocol       : UDP\n"
            output += f"Source Port    : {udp_layer.sport}\n"
            output += f"Destination Port: {udp_layer.dport}\n"

        # ICMP
        elif packet.haslayer(ICMP):

            icmp_count += 1

            output += "Protocol       : ICMP\n"

    # Insert into text area
    text_area.insert(tk.END, output)
    text_area.see(tk.END)

    # Update statistics
    stats_label.config(
        text=f"Total: {packet_count}   TCP: {tcp_count}   UDP: {udp_count}   ICMP: {icmp_count}"
    )


# Sniffing function
def start_sniffing():
    global sniffing

    sniffing = True

    text_area.insert(tk.END, "\n[+] Sniffer Started...\n")

    sniff(prn=process_packet, store=False, filter="ip",
          stop_filter=lambda x: not sniffing)


# Start button
def start_button():
    thread = Thread(target=start_sniffing)
    thread.daemon = True
    thread.start()


# Stop button
def stop_sniffing():
    global sniffing

    sniffing = False

    text_area.insert(tk.END, "\n[-] Sniffer Stopped...\n")


# GUI Window
root = tk.Tk()
root.title("Advanced Network Sniffer Dashboard")
root.geometry("900x600")
root.configure(bg="black")

# Title
title_label = tk.Label(
    root,
    text="CYBER SECURITY NETWORK SNIFFER",
    font=("Arial", 18, "bold"),
    fg="lime",
    bg="black"
)
title_label.pack(pady=10)

# Statistics label
stats_label = tk.Label(
    root,
    text="Total: 0   TCP: 0   UDP: 0   ICMP: 0",
    font=("Arial", 12, "bold"),
    fg="cyan",
    bg="black"
)
stats_label.pack()

# Scrolled text area
text_area = ScrolledText(
    root,
    width=110,
    height=25,
    bg="black",
    fg="white",
    insertbackground="white",
    font=("Consolas", 10)
)
text_area.pack(pady=10)

# Buttons frame
button_frame = tk.Frame(root, bg="black")
button_frame.pack()

# Start button
start_btn = tk.Button(
    button_frame,
    text="Start Sniffing",
    command=start_button,
    bg="green",
    fg="white",
    width=20,
    font=("Arial", 12, "bold")
)
start_btn.grid(row=0, column=0, padx=10)

# Stop button
stop_btn = tk.Button(
    button_frame,
    text="Stop Sniffing",
    command=stop_sniffing,
    bg="red",
    fg="white",
    width=20,
    font=("Arial", 12, "bold")
)
stop_btn.grid(row=0, column=1, padx=10)

# Run GUI
root.mainloop()