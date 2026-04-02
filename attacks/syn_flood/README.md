# SYN Flood - Rapport d'attaque

## Objectif
Attaque par deni de service (DoS) sur PC1.

## Principe
Envoi de nombreux paquets SYN sans completer la connexion TCP.

## Commandes executees
hping3 -S -p 80 --flood 10.0.0.10 -V

## Contre-mesures
SYN cookies, rate limiting, firewall
