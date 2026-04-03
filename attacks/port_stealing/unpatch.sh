#!/bin/bash
echo "[*] Removing Port Stealing countermeasures..."

echo "[+] Disabling Port Security on switch (requires switch config)..."
echo "    Run on switch:"
echo "    configure terminal"
echo "    interface Et0/2"
echo "    no switchport port-security"
echo "    end"

echo "[*] Countermeasures removed. Network is now vulnerable."
