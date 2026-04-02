# SYN Flood - DoS

## Objectif
Deni de service sur PC1 en envoyant des paquets SYN massifs.

## Principe
Envoi de nombreux paquets SYN sans completer le handshake TCP.

## Utilisation
```bash
sudo python3 syn_flood.py
```

## Configuration
- Target: 192.168.189.200:80
- Attacker: 192.168.189.128

## Contre-mesures
- SYN cookies
- Rate limiting
- Firewall
