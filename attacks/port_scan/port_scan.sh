#!/bin/bash

echo "=== Port Scanning ==="
echo "Objectif: Decouvrir les services ouverts sur PC2"

CIBLE_IP="10.0.0.20"
RESULTS_DIR="~/attacks/port_scan"

echo "=== Scan SYN rapide ==="
nmap -sS $CIBLE_IP -oN $RESULTS_DIR/scan_syn.txt

echo "=== Scan des versions de services ==="
nmap -sV $CIBLE_IP -oN $RESULTS_DIR/scan_services.txt

echo "=== Scan complet ==="
nmap -A $CIBLE_IP -oN $RESULTS_DIR/scan_complet.txt

echo ""
echo "Resultats sauvegardes dans $RESULTS_DIR/"
ls -la $RESULTS_DIR/scan_*.txt
