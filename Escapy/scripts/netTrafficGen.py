#!/usr/bin/python
from escapyUtilities import *
from scapy.all import *
from uuid import getnode as get_mac

# Print Banner
print((56 * '\033[31m-\033[1;m'))
print "\033[1;32mNetwork Traffic Generator : Made By Group 4 \033[1;m"
print((56 * '\033[31m-\033[1;m'))


# Print Instructions
print "\033[1;93mLeave Blank For Choosing  Default Values\033[1;m"



#Initial Values
smac = get_mac() 
dmac = "aa:aa:aa:aa:aa:aa"
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

if "1" in protocol:
    smac = getsmac()
    dmac = getdmac()
    if smac == "":
        smac = get_mac()
    if dmac == "":
        dmac = "aa:aa:aa:aa:aa:aa"
    ether = 1

if "2" in protocol:
    sip = getSip()
    dip = getDip()
    ttl = getTTL()
    if sip == "":
        sip = "127.0.0.1"
    if dip == "":
        dip = "127.0.0.1"
    if ttl == "":
        ttl = 64
    ip = 1

if "3" in protocol:
    sport = getSport()
    dport = getDport()
    if sport == "":
        sport = 20
    if dport == "":
        dport = 80
    tcp = 1

elif "4" in protocol:
    sport = getSport()
    dport = getDport()
    if sport == "":
        sport = 20
    if dport == "":
        dport = 80
    udp = 1

if "5" in protocol:
    reqType = getRequestType()
    if "Request" in reqType:
        reqType = 0
    elif "Reply" in reqType:
        reqType = 8
    if reqType == "":
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
elif tcp == 1:
    packet = IP()/Tcp
elif udp == 1:
    packet = IP()/Udp
elif icmp == 1:
    packet = IP()/Icmp



pktSize = 0
try:
    pktByte = bytes(packet)
    for a in pktByte:
        pktSize += 1
except:
    pktSize = 80
print "\033[1;95mSize of a single packet is:\033[0m" + str(pktSize) + "\n"

trafficSize = raw_input("\033[1;94mEnter the Size of Traffic to be generated in MB\nDefault: 1 MB\033[1;m")
if trafficSize == "":
    trafficSize = 1
else:
    trafficSize = int(trafficSize)
count = (trafficSize * 1024)/pktSize
print str(count) + "\033[1;92mPackets will be generated \n\033[1;m"

while count >0:
    if ether == 1:
        try:
            sendp(packet)
        except:
            send(packet)
        if count == 1:
            packet.show()
        count -= 1
    else:
        send(packet)
        if count ==1:
            packet.show()
        count -= 1
