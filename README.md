# Infrastructure Réseaux Sécurisé
**Date** : 08/03/2026  
**Projet** : Mise en place d'une infrastructure réseaux sécurisé virtualisé avec GNS3

## 1. L'infrastructure
L'infrastructure mise en place représente une architecture simple contenant :
  - Un routeur dont une interface est connecté à internet tandis qu'une autre est segmenté en différentes sous interfaces afin de pouvoir faire du routage inter vlan.
  - Un switch dit principale, ce switch est le lien entre le routeur est les autres switchs qui ont en terminaisons des postes clients ou serveurs.
  - Quatre switchs qui auront en terminaison des postes clients ou des serveurs.

La présente image illustre la topologies complète : 

![Image_Topologie](/img/infra.png)

De plus, vous trouverez ci-dessous la tables d'adressage IP ansi que la table d'adressage VLAN.

#### Table d'adressage IP
Machine	| admins | clients |	servers	| guests
:------:|:------:|:------:|:------:|:------:|
r1.tp1.efrei	|10.1.10.254	|10.1.20.254	|10.1.30.254	|10.1.40.254
mario.tp1.efrei	|x	|10.1.20.1	|x|	x
luigi.tp1.efrei	|x	|10.1.20.2	|x|	x
peach.tp1.efrei	|x	|10.1.20.3	|x|	x
daisy.tp1.efrei	|x|	x	|x	|10.1.40.1
lakitu.tp1.efrei	|x	|10.1.20.4	|x	|x
bowser.tp1.efrei	|10.1.10.1	|x	|x|	x
dhcp.tp1.efrei	|x	|x	|10.1.30.1	|x

#### Table d'adressage VLAN

Réseau	|Adresse|	VLAN|	Pour qui ?
:------:|:------:|:------:|:------:
admins	|10.1.10.0/24	|10|	Les laptops des admins
clients	|10.1.20.0/24	|20	|Les laptops des clients
servers	|10.1.30.0/24	|30|	Les serveurs de l'infrastructure
guests	|10.1.40.0/24	|40|	Les invités qui ont besoin d'un accès réseau
## 2. Les configurtaions
Dans cette topologie, nous avons du mettre en place différents switchs et un routeur comme vu précedement, et ce, pour plusieurs étapes. Vous trouverez ci-dessous les différentes configurations et scripts utilisés.

### TP1
Les configurations : 
 - [Configuration dnsmasq](/tp1/conf/dnsmasq.conf)
 - [Configuration routeur](/tp1/conf/r1-running-config.txt)
 - [Configuration switch1](/tp1/conf/access1-running-config.txt)
 - [Configuration switch2](/tp1/conf/access2-running-config.txt)
 - [Configuration switch3](/tp1/conf/access3-running-config.txt)
 - [Configuration switch4](/tp1/conf/access4-running-config.txt)
 - [Configuration switch_core](/tp1/conf/core1-running-config.txt)
### TP2
Les scripts :
- [Script Mitm](/tp2/script+img/arp_mitm.py)
- [Script Arp Poisonnig](/tp2/script+img/arp_poisoning.py)
- [Script DHCP Starvation](/tp2/script+img/dhcp_starvation.py)
### TP3
Les configurations : 
- [Configuration routeur](/tp3/conf/r1-running-config.txt)
 - [Configuration switch1](/tp3/conf/access1-running-config.txt)
 - [Configuration switch2](/tp3/conf/access2-running-config.txt)
 - [Configuration switch3](/tp3/conf/access3-running-config.txt)
 - [Configuration switch4](/tp3/conf/access4-running-config.txt)
