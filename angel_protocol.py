from static_impulses import *
import os
from getpass import getpass


def angel_protocol():
    jay("please input pass phrase for angel protocol...")
    check = 0
    while check < 3:
        check+=1
        pass_phrase = getpass("||$PASS-PHRASE$||: ")
        if pass_phrase.lower() == "tony stark":
            jay("Activating angel protocol")
            jay("welcome to angel protocol sir, what would you like to do today")
            check+=5
            angels()
            
        elif check == 3:
            jay("too many wrong tries, initiating system lockdown protocol")
        else :
            jay("Sorry that is the wrong pass phrase")
    
def angels():
    def term_check():
        terminate = input("||CONFIRMATION||: ")
        if terminate.lower() == "yes":
            angels()
        elif terminate.lower() == "no":
            jay("deactivating all angels")
            pass
        else:
            jay("please input yes or no")
            term_check()

    print("----------------")
    print("|ANGEL PROTOCOL|")
    print("----------------\n")
    print("1. Recon")
    print("2. Sniffing")
    print("3. Implant")
    print("4. Scan")
    print("5. Neuclear")
    print("")
    choice = int(input("|\ANGEL/|: "))

    def choice_check():
        if choice == 1:
            recon()
        elif choice == 2:
            sniff()
        elif choice == 3:
            implant()
        elif choice == 4:
            scan()
        elif choice == 5:
            jay("Are you sure you want to activate this angel sir")
            terminate = input("||CONFIRMATION||: ")
            if terminate.lower() == "yes":
                jay("setting up neuclear angel")
                jay("please input pass phrase...")
                nuc_pass = getpass("||$PASS-PHRASE$||: ")
                if nuc_pass == "3000":
                    neuclear()
                else:
                    jay("wrong pass phrase, terminating angel")
                    angels()
            elif terminate.lower() == "no":
                jay("returning to base angels")
                angels()
            else:
                jay("please input yes or no")
                term_check()
        else:
            jay("please input only the coices in the menu")
            choice_check()
    choice_check()
    jay("Do you need another angel sir?")
    term_check()   



def recon():
    jay("starting recon angel")
    jay("please input the ip of your target")
    ip = input("||:IP:||: ")
    os.system(f"sudo nmap -Pn -O -A {ip}")
    

def sniff():
    jay("starting sniffing angel")
    jay("securing you system")
    os.system("protonvpn-cli c -f")
    jay("system secured")
    jay("please input the ip of your target and the gateway of the network your on")
    ip = input("||*IP*||: ")
    gateway = input("||*GATEWAY*||: ")
    os.system(f"sudo ettercap -T -S -i wlo1 -M arp:remote /{gateway}// /{ip}//")
    pass

def implant():
    jay("starting implant angel")
    jay("for what os do you need an implant")
    im_os = input("|||IMPLANT OS|||: ")
    jay("what should i name the implant file")
    im_name = input("|||IMPLANT NAME|||: ")
    jay("getting implant file ready")
    if im_os.lower() == "windows":
        jay("implant file is ready sir")
        pass
    elif im_os.lower() == "linux":
        jay("implant file is ready sir")
        pass
    else:
        jay("sorry but i can only provide implants for windows and linux")
    pass

def scan():
    jay("starting scan angel")
    os.system("sudo arp-scan --localnet")
    pass

def neuclear():
    jay("neuclear angel protocol has started")
    pass
