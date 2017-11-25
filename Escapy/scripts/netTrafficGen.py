#!/usr/bin/python
from escapyUtilities import *
from scapy.all import *
from uuid import getnode as get_mac

# Print Banner
print((56 * '\033[31m-\033[1;m'))
print "\033[1;32mESCAPY: : Made By Kunal \033[1;m"
print((56 * '\033[31m-\033[1;m'))


# Print Instructions
print "Leave Blank For Choosing  Default Values"



#Initial Values
smac = get_mac() 
dmac = "0.0.0.0"
sip = "127.0.0.1"
dip = "127.0.0.1"
sport = "20"
dport = "80"
ttl = "64"
reqType = "0"
ether = 0
tcp = 0
udp = 0
ip = 0
icmp = 0

protocol = getProtocol()
print protocol
if "1" in protocol:
    smac = getsmac()
    dmac = getdmac()
    ether = 1
if "2" in protocol:
    sip = getSip()
    dip = getDip()
    ttl = getTTL()
    ip = 1
if "3" in protocol:
    sport = getSport()
    dport = getDport()
    tcp = 1
elif "4" in protocol:
    sport = getSport()
    dport = getDport()
    udp = 1
if "5" in protocol:
    reqType = getRequestType()
    if "Request" in reqType:
        reqType = 8
    elif "Response" in reqType:
        reqType = 0
    icmp=1


# Craft Packet according to Requirements
if ether == 1:
    Ether = Ether(src = smac , dst = dmac)
if ip == 1:
    Ip = IP(src = sip, dst = dip , ttl = ttl)

if tcp == 1:
   Tcp = TCP(sport = sport , dport = dport)
elif udp == 1:
    Udp = UDP(sport = sport , dport = dport)
elif tcp != 1:
    if udp != 1: 
        if icmp == 1:
            Icmp = ICMP(code = reqType)

#Generate Packet

if ether == 1:
    if ip == 1:
        if tcp == 1:
            packet = Ether/Ip/Tcp
        elif udp == 1:
            packet = Ether/Ip/Udp
        elif icmp == 1:
            packet = Ether/Ip/Icmp
        else:
            packet = Ether/Ip
    elif tcp == 1:
        packet = Ether/Tcp
    elif udp == 1:
        packet = Ether/Udp
    elif icmp == 1:
        packet = Ether/Icmp
elif ip == 1:
        if tcp == 1:
            packet = Ip/Tcp
        elif udp == 1:
            packet = Ip/Udp
        elif icmp == 1:
            packet = Ip/Icmp
        else:
            packet = Ip



pktSize = 0
pktByte = bytes(packet)
for a in pktByte:
    pktSize += 1
print "Size of a single packet is:" + str(pktSize) + "\n"

trafficSize = int(raw_input("Enter the Size of Traffic to be generated in MB"))
count = (trafficSize * 1024)/pktSize
print str(count) + "Packets will be generated \n"

while count >0:
    if ether == 1:
        sendp(packet)
        if count == 1:
            packet.show()
        count -= 1
    else:
        send(packet)
        if count ==1:
            packet.show()
        count -= 1
