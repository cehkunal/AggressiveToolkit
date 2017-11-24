#!/usr/bin/python
from escapyUtilities import *
from scapy.all import *


# Print Banner

# Print Instructions
print "Press Enter For Choosing  Default Values"

# Craft The Packet
data = getData()
pingFlag=0

smac



while True:
    protocol = getProtocol()
    if "ARP" in protocol:
        smac = getsmac()
        dmac = getdmac()
    elif "TCP" in protocol:
        sport = getSport()
        dport = getDport()
    elif "UDP" in protocol:
        sport = getSport()
        dport = getDport()
    elif "IP" in protocol:
        sip = getSip()
        dip = getDip()
        ttl = getTTL()
    elif "ICMP" in protocol:
        reqType = getRequestType()
        if "Request" in reqType:
            reqType = 8
        elif "Response" in reqType:
            reqType = 0
        pingFlag=1
    elif "break" in protocol:
        break
    else:
        print "Invalid Usage"


count = int(raw_input("Enter the number of packets to be generated"))

pkt = IP()/ICMP()

if pingFlag==1:
    pkt = Ether(dst=dmac,src=smac)/IP(src=sip,dst=dip,ttl=ttl)/ICMP(code=reqType)/data
elif pingFlag == 0:
    if "TCP" in protocol:
        pkt = Ether(dst=dmac,src=smac)/IP(src=sip,dst=dip,ttl=ttl)/TCP(sport=sport, dport=dport)/data
    elif "UDP" in protocol:
        pkt = Ether(dst=dmac,src=smac)/IP(src=sip,dst=dip,ttl=ttl)/TCP(sport=sport, dport=dport)/data
        
while count >0:
    send(pkt)
    count -= 1
