#!/usr/bin/python
from urllib2 import *

def printBanner():
    #Code to Print Banner
    print((56 * '\033[31m-\033[1;m'))
    print "\033[1;32mRecon Detective : Made By Kunal \033[1;m"
    print((56 * '\033[31m-\033[1;m'))
    return

def menu():
    #Code to print menu
    print "\n\033[1;34m1. Whois Lookup\033[1;m"
    print "\033[1;34m2. DNS Lookup + Cloudflare Detector\033[1;m"
    print "\033[1;34m3. Zone Transfer\033[1;m"
    print "\033[1;34m4. Port Scan\033[1;m"
    print "\033[1;34m5. HTTP Header Grabber\033[1;m"
    print "\033[1;34m6. Honeypot Detector\033[1;m"
    print "\033[1;34m7. Robots.txt Scanner\033[1;m"
    print "\033[1;34m8. Link Grabber\033[1;m"
    print "\033[1;34m9. IP Location Finder\033[1;m"
    print "\033[1;34m10. Traceroute\033[1;m"
    return

def reconDetective():
    try:
        choice = input('\033[1;91mEnter your choice: \033[1;m ')
            
        if choice == 1:
            ipaddr = raw_input('\033[1;91mEnter Domain Name or IP Address: \033[1;m')
            url = "http://api.hackertarget.com/whois/?q=" + ipaddr
            whoisResponse = urlopen(url).read()
            print(whoisResponse)
            printBanner()
            menu()
            reconDetective()

        if choice ==2:        
            domain = raw_input('\033[1;91mEnter Domain: \033[1;m')
            url = "http://api.hackertarget.com/dnslookup/?q=" + domain
            dnsLookupResponse = urlopen(url).read()
            print dnsLookupResponse
            if 'cloudfare' in dnsLookupResponse:
                print '\033[1;31mCloudfare Detected\033[1;m'
            printBanner()
            menu()
            reconDetective()    

        if choice == 3:
            domain = raw_input('\033[1;91mEnter Domain: \033[1;m')
            zone = "http://api.hackertarget.com/zonetransfer/?q=" + domain
            try:
                zonetransfer = urlopen(zone).read()
                print zonetransfer
            except 'failed' in zonetranfer:
                print '\033[1;31mZone Transfer Failed \033[1;m'
            printBanner()
            menu()
            reconDetective()

        if choice == 4:
            domain = raw_input('\033[1;91mEnter Domain or IP Address : \033[1;m')
            url = "http://api.hackertarget.com/nmap/?q=" + domain
            portscanResponse = urlopen(url).read()
            print portscanResponse
            printBanner()
            menu()
            reconDetective()

        if choice == 5:
            domain = raw_input('\033[1;91mEnter Domain or IP Address : \033[1;m')
            header = "http://api.hackertarget.com/httpheaders/q=?" + domain
            headerResponse = urlopen(header).read()
            print headerResponse
            printBanner()
            menu()
            reconDetective()

        if choice ==6:
            domain = raw_input('\033[1;91mEnter  IP Address : \033[1;m')
            url = "https://api.shodan.io/labs/honeyscore/" + domain + "?key=3FMOjOIAuNzQC7AUlyKaraGvZSdfI0du"
            reponse = urlopen(url).read()
            if '0.0' in response:
                print '\033[1;32mHoneyPot Probability: 0%\033[1;m'
            if '0.1' in response:
                print '\033[1;32mHoneyPot Probability: 10%\033[1;m'
            if '0.2' in response:
                print '\033[1;32mHoneyPot Probability: 20%\033[1;m'
            if '0.3' in response:
                print '\033[1;32mHoneyPot Probability: 30%\033[1;m'
            if '0.4' in response:
                print '\033[1;32mHoneyPot Probability: 40%\033[1;m'
            if '0.5' in response:
                print '\033[1;32mHoneyPot Probability: 50%\033[1;m'
            if '0.6' in response:
                print '\033[1;32mHoneyPot Probability: 60%\033[1;m'
            if '0.7' in response:
                print '\033[1;32mHoneyPot Probability: 70%\033[1;m'
            if '0.8' in response:
                print '\033[1;32mHoneyPot Probability: 80%\033[1;m'
            if '0.9' in response:
                print '\033[1;32mHoneyPot Probability: 90%\033[1;m'
            if '1.0' in response:
                print '\033[1;32mHoneyPot Probability: 100%\033[1;m'
            printBanner()
            menu()
            reconDetective()

        if choice == 7:
            domain = raw_input('\033[1;91mEnter  Domain: \033[1;m')
            if 'http://' in domain or 'https://' in domain:
                pass
            else:
                domain = 'http://' + domain
            robot = domain + "/robots.txt"
            response = urlopen(domain).read()
            print response
            printBanner()
            menu()
            reconDetective()

        if choice == 8:
            domain = raw_input('\033[1;91mEnter  URL : \033[1;m')
            if 'http://' in domain or 'https://' in domain:
                pass
            else:
                domain = 'http://' + domain
            crawl = "https://api.hackertarget.com/pagelinks/?q=" + domain
            response = urlopen(crawl).read()
            print response
            printBanner()
            menu()
            reconDetective()

        if choice == 9:
            domain = raw_input('\033[1;91mEnter IP Address : \033[1;m')
            geo = "http://ipinfo.io/" + domain + "/geo"
            response = urlopen(geo).read()
            print response
            printBanner()
            menu()
            reconDetective()

        if choice == 10:
            domain = raw_input('\033[1;91mEnter Domain or IP Address: \033[1;m')
            trace = "https://api.hackertarget.com/mtr/?q=" + domain
            response = urlopen(trace).read()
            print response
            printBanner()
            menu()
            reconDetective()

        else:
            print '\033[1;32mInvalid Option\033[1;m'
            printBanner()
            menu()
            reconDetective()

    except:
        print "\033[1;35m[-] Something Went Wrong\n \033[1;m"

printBanner()
menu()
reconDetective()






