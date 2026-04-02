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
     192.168.189.200  192.168.189.201          192.168.189.128
            |               |                       |
            |               |                       |
        [ Victim 1 ]    [ Victim 2 ]            [ Attaquant ]
```

## Plan d'adressage

| Machine      | IP               | Role         |
|--------------|------------------|--------------|
| PC1          | 192.168.189.200  | Victime 1    |
| PC2          | 192.168.189.201  | Victime 2    |
| Rocky        | 192.168.189.128  | Attaquant    |

## Dossiers des attaques

```
attacks/
├── arp_poisoning/
│   ├── arp_poisoning.py
│   └── README.md
├── syn_flood/
│   ├── syn_flood.py
│   └── README.md
├── port_scan/
│   ├── port_scan.py
│   └── README.md
└── ssh_bruteforce/
    ├── ssh_bruteforce.py
    └── README.md
```
