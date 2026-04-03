#!/bin/bash
echo "[*] Removing ARP Poisoning countermeasures..."

echo "[+] Flushing static ARP entries..."
arp -d 192.168.189.200
arp -d 192.168.189.201

echo "[+] Stopping arpwatch daemon..."
sudo pkill arpwatch

echo "[*] Countermeasures removed. Network is now vulnerable."
