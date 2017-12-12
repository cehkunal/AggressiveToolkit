#!/usr/bin/python
import sys
import nmap
from threading import *
import subprocess
import optparse

threadlock = BoundedSemaphore(value=20)

def findIP(domainName):
    global outputFile
    ipdata = subprocess.Popen(["nslookup",domainName], stdout=subprocess.PIPE).communicate()
    outputFile.write((ipdata[0]).split()[-1]) 
    outputFile.write('\n')
    threadlock.release()

parser = optparse.OptionParser('usage %prog ' + '-i <target Domain List> -o <output File>')
parser.add_option('-i', dest='domainList', type='string', help='specify File Containing Domain List')
parser.add_option('-o', dest='opFile', type='string', help='specify the output file')
(options, args) = parser.parse_args()

domainList = options.domainList
opFile = options.opFile


if domainList == None or opFile == None:
    print parser.usage
    exit(0)

domainFile = open(domainList,'r')
outputFile = open(opFile,'a')

data = domainFile.readlines()

for line in data:
    threadlock.acquire()
    domain = line.strip()
    t = Thread(target=findIP(domain))
    t.start()
