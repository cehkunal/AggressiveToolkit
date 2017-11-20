#!/usr/bin/python

import mechanize
import itertools
import cookielib
import sys
from bs4 import BeautifulSoup
from re import search , findall
from urllib import urlopen
from urllib2 import URLError

#Initializing Mechanize
br = mechanize.Browser()
cookies = cookielib.LWBCookieJar()
br.set_cookiejar(cookies)

#Mechanize Settings
br.set_handle_equiv(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)
br.set_debug_http(False)
br.set_debug_responses(False)
br.set_debug_redirects(False)
br.set_handle_refresh(mechanize.__http.HTTPRefreshProcessor(), max_time = 1 )
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1'),
('Accept','text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'), ('Accept-Encoding','br')]

print((56 * '\033[31m-\033[1;m'))
print "\033[1;32mBRUTER : Made By Kunal \033[1;m"
print((56 * '\033[31m-\033[1;m'))

#Take URL as Input from User 
url = raw_input('\033[1;34m[?]\033[0m Enter Target URL: ')
if 'http://' in url:
    pass
elif 'https://' in url:
    url = url.replace('https://','http://')
else:
    url = 'http://' + url

#Open the URL
try:
    br.open(url, timeout=10.0)
except URLError as e:
    url = 'https://' + url
    br.open(url)

#Find out all the forms
forms = br.forms()

#Store the headers 
headers = str(urlopen(url).headers.headers).lower()

#Basic Vulnerability Check
if 'x-frame-options:' not in headers:
    print '\033[1;32m[+]\033[0m Clickjacking Vulnerability maybe Present'
if 'cloudfare-nginx' in headers:
    print '\033[1;32m[+]\033[0m Target is Protected By CloudFare'


#Fetch the data and read Response
data = br.open(url).read() 
if 'type="hidden"' not in data:
    print '\033[1;32m[+]\033[0m CSRF Vulnerability maybe Present'

#Parse the response and save title in Original
soup = BeautifulSoup(data, 'lxml')
i_title = soup.find('title')
if i_title != None:
    original = i_title.contents 

def WAF_detector():
    noise = "?=<script>alert()</script>" #XSS Payload
    fuzz = url + noise
    res1 = urlopen(fuzz) 
    
    if res1.code == 406 or res1.code == 501:
        print"\033[1;31m[-]\033[1;m WAF Detected : Mod_Security"
    elif res1.code == 999:
        print"\033[1;31m[-]\033[1;m WAF Detected : WebKnight"
    elif res1.code == 419:
        print"\033[1;31m[-]\033[1;m WAF Detected : F5 BIG IP"
    elif res1.code == 403: 
        print "\033[1;31m[-]\033[1;m Unknown WAF Detected"

WAF_detector()




























