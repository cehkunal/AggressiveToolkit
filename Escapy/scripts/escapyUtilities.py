#!/usr/bin/python

sipMsg = "\033[1;96mEnter the Source IP\033[1;m\n\033[1;93mDefault: 127.0.0.1\n\033[1;m"
dipMsg = "\033[1;96mEnter the Destination IP\033[1;m\n\033[1;93mDefault: 127.0.0.1\n\033[1;m" 
protocolMsg = "\033[1;96mChoose the Protocol Numbers separated by space\n\033[1;m"
protocols = ["1.Ether","2.IP","3.TCP","4.UDP","5.ICMP"]
sportMsg = "\033[1;96mEnter the Source Port\033[1;m\n\033[1;93mDefault: 20\n\033[1;m"
dportMsg = "\033[1;96mEnter the Destination Port\033[1;m\n\033[1;93mDefault: 80\n\033[1;m"
smacMsg = "\033[1;96mEnter the source MAC Address\033[1;m\n\033[1;93mDefault: Machine's Original MAC\033[1;m\n\033[1;94mFormat: aa:aa:bb:bb:aa:aa\n\033[1;m"
dmacMsg = "\033[1;96mEnter the destination MAC Address\033[1;m\n\033[1;93mDefault: aa:aa:aa:aa:aa:aa\033[1;m\n\033[1;94mFormat: aa:bb:aa:bb:aa:bb\n\033[1;m"
dataMsg = "\033[1;96mEnter the Data Part\nDefault: NULL\n\033"
getTTLMsg = "\033[1;96mEnter the TTL value\033[1;m\n\033[1;93mDefault: 64\n\033[1;m"
getRequestTypeMsg = "\033[1;96mEcho-Request(1) or Echo-Reply(2)\033[1;m\n\033[1;93mDefault: Echo-Request\n\033[1;m"

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
