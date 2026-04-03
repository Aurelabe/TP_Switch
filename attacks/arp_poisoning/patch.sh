#!/bin/bash
echo "[*] Applying ARP Poisoning countermeasures..."

echo "[+] Enabling Dynamic ARP Inspection on switch (requires switch config)..."
echo "    Run on switch:"
echo "    configure terminal"
echo "    ip arp inspection vlan 1"
echo "    interface Et0/2"
echo "    ip arp inspection trust"
echo "    end"

echo "[+] Setting static ARP entries on local machine..."
arp -s 192.168.189.200 00:50:79:66:68:01
arp -s 192.168.189.201 00:50:79:66:68:02

echo "[+] Starting arpwatch daemon..."
sudo arpwatch -i ens224 &

echo "[*] Countermeasures applied."
echo "[*] Monitor with: sudo tail -f /var/log/syslog | grep arpwatch"
