#!/usr/bin/python

sipMsg = "Enter the Source IP\n"
dipMsg = "Enter the Destination IP\n"
protocolMsg = "Choose the Protocol\n"
protocols = ["1.ARP","2.IP","3.TCP","4.UDP","5.ICMP","6.Done"]
sportMsg = "Enter the Source Port\n"
dportMsg = "Enter the Destination Port\n"
smacMsg = "Enter the source MAC Address\n"
dmacMsg = "Enter the destination MAC Address\n"
dataMsg = "Enter the Data Part"
getTTLMsg = "Enter the TTL value"
getRequestTypeMsg = "Echo-Request(1) or Echo-Reply(2)"

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
    if protocol == "1":
        return "1.ARP"
    elif protocol == "3":
        return "3.TCP"
    elif protocol == "4":
        return "4.UDP"
    elif protocol == "5":
        return "5.ICMP"
    elif protocol == "2":
        return "2.IP"
    elif protocol == "6":
        return "break"
    else:
        return "Invalid Choice"


def getSport():
    sport = raw_input(sportMsg)
    return sport


def getDport():
    dport = raw_input(dportMsg)
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
    return ttl

def getSip():
    sip = raw_input(sipMsg)
    return sip

def getDip():
    dip = raw_input(dipMsg)
    return dip
