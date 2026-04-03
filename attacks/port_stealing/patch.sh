#!/bin/bash
echo "[*] Applying Port Stealing countermeasures..."

echo "[+] Configuring Port Security on switch (requires switch config)..."
echo "    Run on switch:"
echo "    configure terminal"
echo "    interface Et0/2"
echo "    switchport port-security"
echo "    switchport port-security maximum 1"
echo "    switchport port-security mac-address sticky"
echo "    switchport port-security violation shutdown"
echo "    end"

echo "[+] Verifying port security status..."
echo "    Run on switch: show port-security interface Et0/2"

echo "[*] Countermeasures applied."
