# IP Spoofing - Usurpation d'adresse IP

## Objectif
Usurper l'adresse IP d'une autre machine pour eviter la filtration par IP ou simuler une attaque depuis une autre source.

## Principe
Modification de l'adresse IP source dans les paquets pour se faire passer pour une autre machine.

## Utilisation
```bash
sudo python3 ip_spoofing.py
# ou
sudo hping3 -a <FAKE_IP> -S -p 80 <TARGET>
```

## Configuration
- Fake IP: 192.168.189.200 (PC1)
- Target: 192.168.189.201 (PC2)
- Attaquant: 192.168.189.128
- Interface: ens224

## Outils
- Scapy (Python)
- hping3
- nmap

## Contre-mesures
- IP Source Guard sur le switch
- Filtrage ingress
- uRPF (Unicast Reverse Path Forwarding)
