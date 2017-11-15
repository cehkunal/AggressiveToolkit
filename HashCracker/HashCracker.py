#!/usr/bin/python

from urllib import urlopen , urlencode
from re import search
import sys

#Utility Functions for Cracking Hash

def crackSHA256():
    responseHtml = urlopen("http://md5decrypt.net/Api/api.php?hash="+hashVal+"&hash_type=sha256&email=nitinsharmarks_cse13@its.edu.in&code=07014c0e89b17ef2")
    responseString = responseHtml.read()
    if len(responseString) > 0:
        print "\n\033[1;32m[+] Hash Cracked By md5decrypt.net: \033[1;m", responseString
        sys.exit()
    else:
        print "\033[1;31m[-]\033[1;m Hash Not Found"
        sys.exit()

def crackSHA():
    responseHtml = urlopen("http://md5decrypt.net/Api/api.php?hash="+hashVal+"&hash_type=sha1&email=nitinsharmarks_cse13@its.edu.in&code=07014c0e89b17ef2")
    responseString = responseHtml.read()
    if len(responseString) > 0:
        print "\n\033[1;32m[+] Hash Cracked By md5decrypt.net: \033[1;m", responseString
        sys.exit()
    else:
        print "\033[1;31m[-]\033[1;m Hash Not Found"
        sys.exit()

def crackSHA384():
    responseHtml = urlopen("http://md5decrypt.net/Api/api.php?hash="+hashVal+"&hash_type=sha384&email=nitinsharmarks_cse13@its.edu.in&code=07014c0e89b17ef2")
    responseString = responseHtml.read()
    if len(responseString) > 0:
        print "\n\033[1;32m[+] Hash Cracked By md5decrypt.net: \033[1;m", responseString
        sys.exit()
    else:
        print "\033[1;31m[-]\033[1;m Hash Not Found"
        sys.exit()

def crackSHA512():
    responseHtml = urlopen("http://md5decrypt.net/Api/api.php?hash="+hashVal+"&hash_type=sha512&email=nitinsharmarks_cse13@its.edu.in&code=07014c0e89b17ef2")
    responseString = responseHtml.read()
    if len(responseString) > 0:
        print "\n\033[1;32m[+] Hash Cracked By md5decrypt.net: \033[1;m", responseString
        sys.exit()
    else:
        print "\033[1;31m[-]\033[1;m Hash Not Found"
        sys.exit()

#print all Intro banners

print((56 * '\033[31m-\033[1;m'))
print "\033[1;32m Hash Cracker : Made By Kunal \n Supported Hash Formats: MD5, SHA1 , SHA256 , SHA384 , SHA512 \033[1;m"
print((56 * '\033[31m-\033[1;m'))

#take hash as Input

hashVal = raw_input('\033[1;97mEnter the hash to be Cracked: \033[1;m').lower()

if len(hashVal) == 32:
    print "\033[1;33m[!]\033[1;m Hash function : MD5"
    data = urlencode({"hash":hashVal, "submit":"Decrypt It!"})
    responseHtml = urlopen("http://md5decryption.com",data)
    responseString = responseHtml.read()
    match = search(r"Decrypted Text: </b>[^<]*</font>",responseString)
    if match : #if value is decrypted
        print "\n\033[1;32m[+] Hash cracked by md5Decrypter.com:\033[1;m", match.group().split('b>')[1][:-7]
        sys.exit()
    else:
        data = urlencode({"md5":hashVal,"x":"21","y":"8"})
        responseHtml = urlopen("http://md5.my-addr.com/md5_decrypt-md5_cracker_online/md5_decoder_tool.php",data)
        responseStr = responseHtml.read()
        match = search (r"<span class='middle_title'>Hashed string</span>: [^<]*</div>" , responseStr)
        if match:
            print "\n\033[1;32m[+] Hash Cracked By md5-my-addr.com: \033[1;m" , match.group().split('span')[2][3:-6]
            sys.exit()
        else:
            url = "http://www.nitrxgen.net/md5db/" + hashVal
            responseHtml = urlopen(url).read()
            if len(responseHtml) >0:
                print "\n\033[1;32m[+] Hash Cracked by nitrxgen.com:\033[1;m", responseHtml
                sys.exit()
            else:
                print "\033[1;31m[-]\033[1;m Hash Not Found"
                sys.exit()

if len(hashVal) == 40:
    print "\033[1;33m[!]\033[1;33m Hash Function : SHA1"
    crackSHA()


if len(hashVal) == 64:
    print "\033[1;33m[!]\033[1;m Hash Function : SHA-256"
    crackSHA256()

if len(hashVal) == 96:
    print "\033[1;33m[!]\033[1;m Hash Function : SHA-384"
    crackSHA384()

if len(hashVal) == 128:
    print "\033[1;33m[!]\033[1;m Hash Function : SHA-512"
    crackSHA512()

else:
    print "\033[1;31m[-]\033[1;31m This Hash Is Not Supported."



