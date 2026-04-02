# ARP Poisoning - MITM

## Objectif
Se placer en homme du milieu entre PC1 et PC2 pour intercepter le trafic.

## Principe
Envoi de fausses reponses ARP pour associer l'adresse MAC de l'attaquant aux adresses IP des victimes.

## Utilisation
```bash
sudo python3 arp_poisoning.py
```

## Configuration
- Victim PC1: 192.168.189.200
- Target PC2: 192.168.189.201
- Attacker: 192.168.189.128

## Capture
```bash
tcpdump -i eth0 -w capture.pcap
driftnet -i eth0
urlsnarf -i eth0
```

## Contre-mesures
- ARP statique
- arpwatch
- HTTPS everywhere
