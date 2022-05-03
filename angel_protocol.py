from static_impulses import *
import os

def angel_protocol():
    from getpass import getpass
    jay("please input pass phrase for angel protocol...")
    check = 0
    while check < 3:
        check+=1
        pass_phrase = getpass("||$PASS-PHRASE$||: ")
        if pass_phrase.lower() == "tony stark":
            jay("Activating angel protocol")
            jay("welcome to angel protocol sir, what would you like to do today")
        else :
            jay("Sorry that is the wrong pass phrase")
    jay("too many wrong tries, initiating system lockdown protocol")