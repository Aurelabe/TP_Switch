# Port Stealing - Attaque de vol de port

## Objectif
Usurper l'adresse MAC d'une victime pour recevoir son trafic.

## Principe
En combinant CAM flooding et manipulation des paquets, un attaquant peut voluer le port d'une victime et recevoir tout son trafic.

## Utilisation
```bash
sudo bash port_stealing.sh
```

## Configuration
- Victim PC1: 192.168.189.200
- Victim PC2: 192.168.189.201
- Attaquant: 192.168.189.128
- Interface: eth0

## Outils
- macof, arpspoof, ettercap

## Contre-mesures
- Port Security avec sticky MAC
- DHCP Snooping
