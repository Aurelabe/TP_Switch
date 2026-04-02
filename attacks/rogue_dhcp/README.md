# Rogue DHCP Server - Attaque par serveur DHCP illegitime

## Objectif
Inserer un serveur DHCP malveillant pour rediriger le trafic des victimes.

## Principe
Le rogue DHCP repond aux requetes DHCP avec une configuration reseau preferences, faisant passer tout le trafic par l'attaquant (MITM).

## Utilisation
```bash
sudo bash rogue_dhcp.sh
```

## Configuration
- Rogue DHCP: 192.168.189.128
- Cible: 192.168.189.200 (PC1), 192.168.189.201 (PC2)
- Gateway: 192.168.189.1
- DNS: 8.8.8.8
- Interface: eth0

## Outils
- isc-dhcp-server
-yersinia

## Contre-mesures
- DHCP Snooping sur le switch
- Port-based VLAN
