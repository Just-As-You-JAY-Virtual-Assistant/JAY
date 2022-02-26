import datetime
import pyttsx3
import pywhatkit
import webbrowser
import pyjokes
import time
import os
import wikipedia
import warnings
import random
import json
from body import *
from difflib import get_close_matches


warnings.catch_warnings()
warnings.simplefilter("ignore")

#permanent nervous system data, unchangable while awake
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

jay_speech = {
    "greet": ["hello there sir", "hi sir", "hey sir", "I am here sir"],
}


#natural nerve impulses
def speaker(speak):
    eng = pyttsx3.init('espeak')
    eng.setProperty('voice', 'english+f1')
    eng.say(speak)
    eng.runAndWait()

def task_checker(message1, music_title):
    reply_mes = input("||-JAY-|| => reply: ")
    if reply_mes.lower() in ["yes", "sure", "yup", "yeaa", "yeah"]:
        pywhatkit.playonyt(music_title)
        time.sleep(5)
    else:
        print(print("||-JAY-|| =>" + message1))

def timecheck(message1, message2, message3):
    if int(times) < 12 and int(times) >=6:
        print("||-JAY-|| => " + message1)
    elif int(times) >= 12 and int(times) < 18:
        print("||-JAY-|| => " + message2)
    elif int(times) >= 18 or int(times) < 6:
        print("||-JAY-|| => " + message3)

def speech_randomizer():
    num = random.randint(0, len(jay_speech["greet"]) - 1)
    return jay_speech["greet"][num].capitalize()



#nervous functions to execute specific tasks
def about():
    print("||-JAY-|| => " + "My name is " + about_jay["name"] + " and I am " + about_jay["age"] + ", I was created to " + about_jay["use"])



def greet():
    timecheck(speech_randomizer() + ", Good Morning", 
            speech_randomizer() + ", Good Evening", 
            speech_randomizer() + ", Good Evening")
    
def bye():
    timecheck("Have a great day, Sir", "Have a good evening, Sir", "Have a good night, Sir")
    exit()

def convo():
    print("||-JAY-|| => " + "I am fine sir, what can i do for you today?")

def gratitude():
    print("||-JAY-|| => " + "No problem sir, happy to help")

def joke():
    print(pyjokes.pyjokes.get_joke('en'))



def study():
    print("||-JAY-|| => " + "Ok sir, do you want some music with your study")
    task_checker("||-JAY-|| => Opening your notebook", "chill lofi")
    webbrowser.open("https://keep.google.com/")
    print("||-JAY-|| => Have a nice study sir.")

def work():
    print("||-JAY-|| => Setting up workstation")
    print("||-JAY-|| => Do you want any music while working")
    task_checker("||-JAY-|| => Opening your Jiraboard", "night time chill lofi")
    webbrowser.open("https://nigussolomon.atlassian.net/jira/your-work")
    print("||-JAY-|| => Have a nice work session sir")



def movies():
    print("Time to relax")
    type = input("||-JAY-|| => Movies or Shows, Sir: ")
    if type.lower() == "shows":
        webbrowser.open(f"https://hdtoday.tv/filter?type=tv&quality=all&release_year={datetime.datetime.now().year}&genre=all&country=all")
    elif type.lower() == "movies":
        webbrowser.open(f"https://hdtoday.tv/filter?type=movie&quality=all&release_year={datetime.datetime.now().year}&genre=all&country=all")

def music():
    print("||-JAY-|| => What shall i play for you sir")
    title = input("||NIGUS||: ")
    if title.lower() == "cancel":
        pass
    else:
        pywhatkit.playonyt(title)




def search():
    searchtitle = input("||-JAY-|| => What do you want to search for: ")
    if searchtitle.lower() == "cancel":
        pass
    else:
        print("||-JAY-|| => Searching...")
        pywhatkit.search(searchtitle)
        search()

def people_search():
    name = input("||-JAY-|| => Full Name of the person your looking for: ")
    if name == "cancel":
        pass
    else:
        reply = input("||-JAY-|| => Do you need details: ")
        if reply == "yes":
            pywhatkit.search(name)
            print("")
            people_search()
        else:
            try:
                print(wikipedia.summary(name))
            except:
                error = input("||-JAY-|| => Can't find the person\nDo you want to do a google search: ")
                if error == "yes":
                    pywhatkit.search(name)
                    people_search()
                else:
                    people_search()

def dictionary():
    def check():
        reply = input("||-JAY-|| => Do you want to search for another word: ")
        if reply == "yes":
            dictionary()
        else:
            pass
    words_data = json.load(open("words.json"))
    word = input(print("||-JAY-|| => Enter a word: "))

    word = word.lower()
    if word in words_data or word.title() in words_data or word.upper() in words_data:
            res = words_data[word][0]
            print(print(f"{str(res)}\n"))
            check()
    elif len(get_close_matches(word, words_data.keys())) >0:
        similar_words_list = list(map(str, get_close_matches(word, words_data.keys())))
        ans = input(print("||-JAY-|| => Did you mean %s instead: " % similar_words_list))
        if ans  == 'no':
            print("||-JAY-|| => Sorry, I don't understand you!!!!")
            check()
        else:
            print(f"||-JAY-|| =>{words_data[ans][0]}\n")
            check()
                
    else:
        print("||-JAY-|| => I can't find the word. Please double check it!!!")
        check()



def timefun():
    print("||-JAY-|| => The time is" + time.strftime('%l:%M'))

def net():
    net_mes = input("||-JAY-|| => Is it your home network sir: ")
    if net_mes.lower() == "yes":
        os.system("ping -c2 8.8.8.8")
        print("")
        os.system("speedtest --no-upload")
    else:
        ip = input("||-JAY-|| => Please input the gateway of the network your on: ")
        os.system(f"ping -c2 {ip}")
        print("")
        os.system("speedtest --no-upload")
        


def calendar():
    print("||-JAY-|| => Here is your google calendar....")
    webbrowser.open("https://calendar.google.com/calendar")

def gmail():
    reply = input("||-JAY-|| => Personal or School account: ")
    if reply == "cancel":
        pass
    else:
        if reply.lower() == "personal":
            webbrowser.open(personal_account["email"])
            gmail()
        elif reply.lower() == "school":
            webbrowser.open(school_account["email"])
            gmail()

def weather():
    webbrowser.open("https://www.tomorrow.io/weather/")



def error():
    print("||-JAY-|| => Sorry sir, I couldn't understand that")




    
