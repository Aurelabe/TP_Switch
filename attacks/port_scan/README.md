# Port Scanner

## Objectif
Decouvrir les services ouverts sur PC2.

## Principe
Connection TCP sur chaque port pour detecter ceux qui repondent.

## Utilisation
```bash
python3 port_scan.py -t 192.168.189.201 -p 1-1024
python3 port_scan.py -t 192.168.189.201 -p 22,80,443
```

## Configuration
- Target: 192.168.189.201
- Port range: 1-1024 (default)

## Contre-mesures
- Firewall
- Desactiver services inutiles
