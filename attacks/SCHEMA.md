# Schema d'architecture du TP

## Architecture reseau

```
                                    Internet
                                        |
                                    [Cloud1]
                                        |
                    +-------------------+-------------------+
                    |                                       |
                [Switch1]                                   |
                    |                                       |
            +-------+-------+                       +-------+-------+
            |               |                       |               |
         [PC1]           [PC2]                  [Rocky-Attacker]
        10.0.0.10       10.0.0.20               192.168.189.128
            |               |                       |
            |               |                       |
        [ Victim 1 ]    [ Victim 2 ]            [ Attaquant ]
            |               |
            +-------+-------+
                    |
                [Cible]
```

## Plan d'adressage

| Machine      | IP           | Role         |
|--------------|--------------|--------------|
| PC1          | 10.0.0.10    | Victime 1    |
| PC2          | 10.0.0.20    | Victime 2    |
| Rocky        | 192.168.189.128 | Attaquant |

## Description des attaques

### Attaque 1: ARP Poisoning (MITM)

```
[PC1] -----> [Rocky] -----> [PC2]
 10.0.0.10    192.168.189.128  10.0.0.20
    |             |
    |             v
    |      [ Interception ]
    |             |
    +<----[ Reponses ARP falsifiees ]
    
Objectif: Se placer entre PC1 et PC2 pour intercepter le trafic
Outils: arpspoof, dsniff, driftnet, urlsnarf, tcpdump
```

### Attaque 2: SYN Flood (DoS)

```
[Rocky]  ============>  [PC1]
            |
            | 1000+/sec
            |
        [ Paquets SYN ]
            |
            v
    [ Saturation ressources ]
    
Objectif: Rendre PC1 inaccessible
Outils: hping3, nmap
```

### Attaque 3: Port Scanning

```
[Rocky]  ------>  [PC2]
              |
              |  SYN
              |
         [Scan ports]
              |
              v
    [ Ports decouverts ]
    
Objectif: Decouvrir les services ouverts sur PC2
Outils: nmap (-sS, -sV, -A)
```

### Attaque 4: SSH Brute Force

```
[Rocky]  ------->  [PC2:22]
              |
              |  login/password
              |
         [ Force brute ]
              |
    +---------+---------+
    |         |         |
  fail    fail     SUCCESS
              |
              v
    [ Acces SSH obtenu ]
    
Objectif: Trouver les identifiants SSH
Outils: hydra, nmap --script ssh-brute
```

## Commandes rapides

```bash
# Verifier la connexion aux cibles
ping 10.0.0.10
ping 10.0.0.20

# Voir les machines sur le reseau
arp -a
ip neigh show

# Activer le routage IP (pour MITM)
echo 1 > /proc/sys/net/ipv4/ip_forward

# Capturer le trafic
tcpdump -i eth0 -w capture.pcap

# Analyser une capture
tcpdump -r capture.pcap
```

## Dossiers des attaques

```
~/attacks/
├── arp_poisoning/      # Attaque 1
│   ├── arp_poisoning.sh
│   └── README.md
├── syn_flood/         # Attaque 2
│   ├── syn_flood.sh
│   └── README.md
├── port_scan/         # Attaque 3
│   ├── port_scan.sh
│   └── README.md
└── ssh_bruteforce/   # Attaque 4
    ├── ssh_bruteforce.sh
    └── README.md
```

## Resultats attendus

| Attaque | Resultat |
|---------|----------|
| ARP Poisoning | Images, URLs, mots de passe |
| SYN Flood | PC1 hors service |
| Port Scan | Liste des ports/services |
| SSH Brute | Identifiants valides |
