import os
import time
import sys
os.system('clear')
os.system('xdg-open https://www.facebook.com/ISSAM.RAHMOUNI.999')

v ='\033[0;35m'
print(''' \033[0;31m
┈┈┈┈╱▔▔▔▔╲┈┈┈┈   
┈┈┈▕▕╲┊┊╱▏▏┈┈┈   
┈┈┈▕▕▂╱╲▂▏▏┈┈┈   
┈┈┈┈╲┊┊┊┊╱┈┈┈┈   
┈┈┈┈▕╲▂▂╱▏┈┈┈┈   
╱▔▔▔▔┊┊┊┊▔▔▔▔╲   
''')
print(v)
def ond(s):
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(2. / 100)
ond('\033[0;32mＴＯＯＬＳ  ＴＥＲＭＵＸ ☠️ ')
print(v)
ond('''
1: pkg update

2: pkg upgrade

3: pkg install python

4: pkg install python2

5: pkg install python3

6: pkg install ruby

7: pkg install git

8: pkg install php

9: pkg install java

10: pkg install google

11: pkg install bash

12: pkg install perl

13: pkg install nmap

14: pkg install clang

15: pkg install macchanger

16: pkg install nano

17:pkg install figlet

18: pkg install cowsay

19: pkg install curl

20: pkg install tar

21: pkg install zip

22: pkg install unzip

23: pkg install tor

24: pkg install sudo

25: pkg install wget

26: pkg install wcalc

27: pkg install openssl

28: pkg install bmon
''')
bak = input('\033[0;101m ENTER y/n \033[0;32m==> ')
if bak == 'y':
    os.system('clear')
    os.system('pkg update -y')
    os.system('pkg upgrade -y')
    os.system('pkg install python -y')
    os.system('pkg install python2 -y')
    os.system('pkg install python3 -y')
    os.system('pkg install ruby -y')
    os.system('pkg install git -y')
    os.system('pkg install php -y')
    os.system('pkg install java -y')
    os.system('pkg install google -y')
    os.system('pkg install bash -y')
    os.system('pkg install perl -y ')
    os.system('pkg install nmap -y')
    os.system('pkg install figlet -y')
    os.system('pkg install cowsay -y')
    os.system('pkg install curl -y')
    os.system('pkg install tar -y')
    os.system('pkg install zip -y')
    os.system('pkg install unzip -y')
    os.system('pkg install tor -y')
    os.system('pkg install sudo -y')
    os.system('pkg install wget -y')
    os.system('pkg install wcalc -y')
    os.system('pkg install openssl -y')
    os.system('pkg install bmon -y')
    os.system('clear')
    print(' GOOOOOD 🌹 ') 
elif bak =='n':
    os.system('exit')
else:
    print('EROOR'*5050)    
