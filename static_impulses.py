import datetime
import os
import time

if int(datetime.datetime.now().year <= 2022):
    age_now = "a few months"
    if int(datetime.datetime.now().year <= 2022) and int(datetime.datetime.now().month) >= 8 <=12:
        age_now = "almost 1 year"
else:
    age = int(datetime.datetime.now().year) - 2021
    if age <= 1:
        age_now = str(age) + " year "
    else:
        age_now = str(age) + " years "


about_jay = {
    "name":"JAY",
    "age": f"{age_now} old",
    "use": "assist in simple daily task automation."
}

personal_account = {
    "email":"https://mail.google.com/mail/u/0/#inbox",
}

school_account = {
    "email": "https://mail.google.com/mail/u/1/#inbox",
}

jay_speech = {
    "greet": ["hello there sir", "hi sir", "hey sir", "I am here sir", "Always a pleasure to see you sir"],
}

times = time.strftime('%H')


##JAY's task confirmation function
def task_checker(message1, music_title):
    reply_mes = input("|:NIGUS:| => ")
    if reply_mes.lower() in ["yes", "sure", "yup", "yeaa", "yeah"]:
        jayyt(music_title)
        time.sleep(5)
    else:
        jay(message1)

##JAY's time checking function
def timecheck(message1, message2, message3):
    if int(times) < 12 and int(times) >=6:
        print("||-JAY-|| => " + message1)
    elif int(times) >= 12 and int(times) < 18:
        print("||-JAY-|| => " + message2)
    elif int(times) >= 18 or int(times) < 6:
        print("||-JAY-|| => " + message3)

##JAY's greeting randomizer
def speech_randomizer():
    import random
    num = random.randint(0, len(jay_speech["greet"]) - 1)
    return jay_speech["greet"][num].capitalize()

##JAY's study or work session checker
def env_check(url):
    verify  = input("|:NIGUS:| => ")
    if "programming" in verify:
        os.system("code")
        if url == "":
            pass
        else:
           openbrowser(url)
           jay("Do you want any music while working?")
           task_checker("||-JAY-|| => Setting up work station", "night time chill lofi")
           jay("Have a nice work session sir")
    elif "networking" in verify:
        os.system("packettracer &")
        time.sleep(2)
        jay("Do you want any music while working?")
        task_checker("||-JAY-|| => Setting up work station", "night time chill lofi")
        jay("Have a nice work session sir")
    elif "cancel" in verify:
        pass
    else:
        jay("Sorry sir, I couldn't understand that, can ypu please repeat that")

##JAY's texting ability
def jay(msg):
    print("||-JAY-|| => "  + msg)

##JAY's youtube system
def jayyt(title):
    import pywhatkit
    pywhatkit.playonyt(title)

##JAY's url opener
def openbrowser(search):
    import webbrowser
    webbrowser.open(search)

##JAY's google searcher
def googlesearch(search):
    import pywhatkit
    pywhatkit.search(search)