# SSH Brute Force

## Objectif
Trouver le mot de passe SSH de PC2 par brute force.

## Principe
Essai systematique de mots de passe depuis une wordlist.

## Utilisation
```bash
python3 ssh_bruteforce.py -t 192.168.189.201 -u admin -P passwords.txt
```

## Configuration
- Target: 192.168.189.201:22
- User: admin (default)

## Contre-mesures
- Mots de passe complexes
- fail2ban
- Clefs SSH
