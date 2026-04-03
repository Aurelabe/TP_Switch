# CAM Flooding - Attaque de table CAM

## Objectif
Deborder la table CAM d'un switch pour provoquer un comportement de hub et capturer tout le trafic.

## Principe
La table CAM (Content Addressable Memory) mappe les adresses MAC aux ports. En inondant le reseau de fausses adresses MAC, on remplit cette table, forcant le switch a broadcaster sur tous les ports.

## Utilisation
```bash
sudo bash cam_flooding.sh
# ou
sudo python3 cam_flooding.py
```

## Configuration
- Interface: ens224
- Cible: 192.168.189.200 (PC1), 192.168.189.201 (PC2)
- Attaquant: 192.168.189.128

## Outils
- macof (dsniff)
- Scapy (Python)

## Contre-mesures
- Port Security sur le switch
- Limitation du nombre de MAC par port
