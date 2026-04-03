#!/bin/bash
echo "[*] Applying Rogue DHCP countermeasures..."

echo "[+] Configuring DHCP Snooping on switch (requires switch config)..."
echo "    Run on switch:"
echo "    configure terminal"
echo "    ip dhcp snooping"
echo "    ip dhcp snooping vlan 1"
echo "    interface Et0/3"
echo "    ip dhcp snooping trust"
echo "    exit"
echo "    interface Et0/2"
echo "    ip dhcp snooping limit rate 15"
echo "    exit"
echo "    end"

echo "[+] Verifying DHCP snooping status..."
echo "    Run on switch: show ip dhcp snooping"

echo "[*] Countermeasures applied."
