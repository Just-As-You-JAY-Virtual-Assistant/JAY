import datetime
import pyttsx3
import pywhatkit
import webbrowser
import pyjokes
import time
import os
import wikipedia
import warnings


warnings.catch_warnings()
warnings.simplefilter("ignore")

#permanent nervous system data, unchangable while awake
if int(datetime.datetime.now().year <= 2022):
    age_now = "a few months "
    if int(datetime.datetime.now().year <= 2022) and int(datetime.datetime.now().month) >= 8 <=12:
        age_now = "almost 1 year"
else:
    age = int(datetime.datetime.now().year) - 2021
    if age <= 1:
        age_now = str(age) + " year "
    else:
        age_now = str(age) + " years "

personal_data = {
    "name":"JAY",
    "age": f"{age_now} old",
    "use": "assist in simple daily task automation."
}

times = time.strftime('%H')



#naturan nerve impulses
def speaker(speak):
    eng = pyttsx3.init('espeak')
    eng.setProperty('voice', 'english+f1')
    eng.say(speak)
    eng.runAndWait()



def task_checker(message1, music_title):
    reply_mes = input("\t=> reply: ")
    if reply_mes.lower() in ["yes", "sure", "yup", "yeaa", "yeah"]:
        pywhatkit.playonyt(music_title)
        time.sleep(5)
    else:
        print("{JAY}=>" + message1)


def timecheck(message1, message2, message3):
    if int(times) < 12 and int(times) >=6:
        print("{JAY} => " + message1)
    elif int(times) >= 12 and int(times) < 18:
        print("{JAY} => " + message2)
    elif int(times) >= 18 or int(times) < 6:
        print("{JAY} => " + message3)


    

#nervous functions to execute specific tasks
def about():
    print("{JAY} => My name is " + personal_data["name"] + 
            " and I am " + personal_data["age"] + 
            ", I was created to " + personal_data["use"])

def greet():
    timecheck("Good Morning, Sir", "Good Evening, Sir", "Good Evening sir")
    
def bye():
    timecheck("Have a great day, Sir", "Have a good evening, Sir", "Have a good night, Sir")
    time.sleep(2)
    os.system("clear")
    exit()

def study():
    print("{JAY} => Ok sir, do you want some music with your study: ")
    task_checker("{JAY} => Opening your notebook", "chill lofi")
    webbrowser.open("https://keep.google.com/")
    print("{JAY} => Have a nice study sir.")

def movies():
    print("{JAY} => Time to relax")
    type = input("{JAY} => Movies or Shows, Sir: ")
    if type.lower() == "shows":
        webbrowser.open(f"https://hdtoday.tv/filter?type=tv&quality=all&release_year={datetime.datetime.now().year}&genre=all&country=all")
    elif type.lower() == "movies":
        webbrowser.open(f"https://hdtoday.tv/filter?type=movie&quality=all&release_year={datetime.datetime.now().year}&genre=all&country=all")

def music():
    print("{JAY} => What shall i play for you sir")
    title = input("{JAY} => input title for music: ")
    pywhatkit.playonyt(title)

def search():
    searchtitle = input("{JAY} => what do you want to search for: ")
    if searchtitle.lower() == "cancel":
        pass
    else:
        pywhatkit.search(searchtitle)
        search()

def timefun():
    print("{JAY} => The time is " + time.strftime('%l:%M'))

def work():
    print("{JAY} => Setting up workstation")
    print("{JAY} => Do you want any music while working")
    task_checker("{JAY} => Opening your Jiraboard", "night time chill lofi")
    webbrowser.open("https://nigussolomon.atlassian.net/jira/your-work")
    print("{JAY} => Have a nice work session sir")

def joke():
    print("{JAY} =>" + pyjokes.pyjokes.get_joke('en'))

def convo():
    print("{JAY} => I am fine sir, what can i do for you today?")
    
def net():
    os.system("ping -c2 8.8.8.8")
    os.system("speedtest --no-upload")

def gratitude():
    print("{JAY} => No problem sir, happy to help")

def people_search():
    name = input("{JAY} => Full Name of the person your looking for: ")
    if name == "cancel":
        pass
    else:
        reply = input("{JAY} => Do you need details: ")
        if reply == "yes":
            pywhatkit.search(name)
            print("")
            people_search()
        else:
            try:
                print(wikipedia.summary(name))
            except:
                error = input("{JAY} => Can't find the person\nDo you want to do a google search: ")
                if error == "yes":
                    pywhatkit.search(name)
                    people_search()
                else:
                    people_search()

    
