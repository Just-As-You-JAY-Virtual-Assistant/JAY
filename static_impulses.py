import datetime
from distutils.log import error
import os
import time
import pyttsx3

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

times = time.strftime('%H')
audio = 'speech.mp3'
language = 'en'
sound = 'co.za'


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
        jay(message1)
    elif int(times) >= 12 and int(times) < 18:
        jay(message2)
    elif int(times) >= 18 or int(times) < 6:
        jay(message3)


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
        error()

##JAY's texting and speaking ability
def jay(msg):
    from gtts import gTTS
    from playsound import playsound

    sp = gTTS(text = msg, lang='en', tld='com.au')
    sp.save(audio)
    playsound(audio)

    print(f"||-JAY-|| => {msg}")


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