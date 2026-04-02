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
- Interface: eth0
- Generation de MACs aleatoires

## Outils
- macof (dsniff)
- Scapy (Python)

## Contre-mesures
- Port Security sur le switch
- Limitation du nombre de MAC par port
