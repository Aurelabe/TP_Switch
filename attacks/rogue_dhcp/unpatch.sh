#!/bin/bash
echo "[*] Removing Rogue DHCP countermeasures..."

echo "[+] Disabling DHCP Snooping on switch (requires switch config)..."
echo "    Run on switch:"
echo "    configure terminal"
echo "    no ip dhcp snooping"
echo "    end"

echo "[*] Countermeasures removed. Network is now vulnerable."
