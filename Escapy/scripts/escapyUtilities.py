#!/usr/bin/python

sipMsg = "Enter the Source IP\nDefault: 127.0.0.1\n"
dipMsg = "Enter the Destination IP\nDefault: 127.0.0.1" 
protocolMsg = "Choose the Protocol Numbers separated by space\n"
protocols = ["1.Ether","2.IP","3.TCP","4.UDP","5.ICMP"]
sportMsg = "Enter the Source Port\nDefault: 20\n"
dportMsg = "Enter the Destination Port\nDefault: 80\n"
smacMsg = "Enter the source MAC Address\nDefault: Machine's Original MAC\nFormat: aa:aa:bb:bb:aa:aa\n"
dmacMsg = "Enter the destination MAC Address\nDefault: 0.0.0.0\nFormat: aa:bb:aa:bb:aa:bb\n"
dataMsg = "Enter the Data Part\nDefault: NULL\n"
getTTLMsg = "Enter the TTL value\nDefault: 64\n"
getRequestTypeMsg = "Echo-Request(1) or Echo-Reply(2)\nDefault: Echo-Request\n"

def getRequestType():
    reqType = raw_input(getRequestTypeMsg)
    if reqType == "1":
        return "1.Echo-Request\n"
    elif reqType == "2":
        return "2:Echo_Reply\n"
    else:
        return "Invalid Choice\n"

def getSIP():
    sip = raw_input(sipMsg)
    return sip

def getDIP():
    dip = raw_input(dipMsg)
    return dip

def getProtocol():
    for p in protocols:
        print p 
    protocol = raw_input(protocolMsg)
    print protocol
    return protocol

def getSport():
    sport = raw_input(sportMsg)
    if sport == "":
        sport = 20
    else:
        sport = int(sport)
    return sport


def getDport():
    dport = raw_input(dportMsg)
    if dport == "":
        dport = 80
    else:
        dport = int(dport)
    return dport


def getsmac():
    smac = raw_input(smacMsg)
    return smac

def getdmac():
    dmac = raw_input(dmacMsg)
    return dmac


def getData():
    data = raw_input(dataMsg)
    return data

def getTTL():
    ttl = raw_input(getTTLMsg)
    if ttl == "":
        ttl = 64 
        return ttl
    else:
        newttl = int(ttl)
    return newttl

def getSip():
    sip = raw_input(sipMsg)
    return sip

def getDip():
    dip = raw_input(dipMsg)
    return dip
