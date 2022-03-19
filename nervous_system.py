import datetime
import time
import os
import warnings
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

##JAY's speaking function
def speaker(speak):
    import pyttsx3
    eng = pyttsx3.init('espeak')
    eng.setProperty('voice', 'english+f1')
    eng.say(speak)
    eng.runAndWait()

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
    elif "networking" in verify:
        os.system("packettracer &")
        time.sleep(1)

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






#nervous functions to execute specific tasks
def about():
    jay("My name is " + about_jay["name"] + " and I am " + about_jay["age"] + ", I was created to " + about_jay["use"])


#greeting function for intent response
def greet():
    greet_speech = speech_randomizer()
    timecheck(greet_speech + ", Good Morning", 
            greet_speech + ", Good Evening", 
            greet_speech + ", Good Evening")
#bye function for intent response   
def bye():
    timecheck("Have a great day, Sir", "Have a good evening, Sir", "Have a good night, Sir")
    exit()
#conversation function for intent response
def convo():
    jay("I am fine sir, what can i do for you today?")

#gratitude function for intent response
def gratitude():
    jay("No problem sir, happy to help")

#joke generartor function for intent response
def joke():
    import pyjokes
    jay(pyjokes.pyjokes.get_joke('en'))

#study session manager function for intent response
def study():
    jay("Ok sir, do you want some music with your study")
    task_checker("Opening your notebook", "chill lofi")
    env_check("")
    jay("Have a nice study sir.")

#work session manager function for intent response
def work():
    jay("Setting up workstation")
    jay("Will you be working on programming or networking")
    env_check("https://nigussolomon.atlassian.net/jira/your-work")
    jay("Do you want any music while working?")
    task_checker("||-JAY-|| => Setting up work station", "night time chill lofi")
    jay("Have a nice work session sir")

#movie manager function for intent response
def movies():
    type = input("||-JAY-|| => Movies or Shows, Sir: ")
    if type.lower() == "shows":
        openbrowser(f"https://hdtoday.tv/filter?type=tv&quality=all&release_year={datetime.datetime.now().year}&genre=all&country=all")
    elif type.lower() == "movies":
        openbrowser(f"https://hdtoday.tv/filter?type=movie&quality=all&release_year={datetime.datetime.now().year}&genre=all&country=all")

#yt music manager function for intent response
def music():
    jay("What shall i play for you sir")
    title = input("||NIGUS||: ")
    if title.lower() == "cancel":
        pass
    else:
        jayyt(title)

#google search function for intent response
def search():
    searchtitle = input("||-JAY-|| => What do you want to search for: ")
    if searchtitle.lower() == "cancel":
        pass
    else:
        jay("Searching...")
        googlesearch(searchtitle)
        search()

#wiki or google search for people function for intent response
def people_search():
    value = 0
    name = input("||-JAY-|| => Full Name of the person your looking for: ")
    for i in ["cancel", "stop", "leave it", "leave"]:
        if i in name:
            value+=1

    if value > 0:
        pass
    else:
        reply = input("||-JAY-|| => Do you need details: ")
        if "yes" in reply:
            googlesearch(name)
            print("")
            people_search()
        else:
            try:
                import wikipedia
                print(wikipedia.summary(name))
            except:
                error = input("||-JAY-|| => Can't find the person\nDo you want to do a google search: ")
                if "yes" in error:
                    googlesearch(name)
                    people_search()
                else:
                    people_search()

#dictionary function for intent response
def dictionary():
    import json
    from difflib import get_close_matches
    def check():
        reply = input("||-JAY-|| => Do you want to search for another word: ")
        if "yes" in reply:
            dictionary()
        else:
            pass
    words_data = json.load(open("words.json"))
    word = input("||-JAY-|| => Enter a word: ")

    word = word.lower()
    if word in words_data or word.title() in words_data or word.upper() in words_data:
            res = words_data[word][0]
            print(f"{str(res)}\n")
            check()
    elif len(get_close_matches(word, words_data.keys())) >0:
        similar_words_list = list(map(str, get_close_matches(word, words_data.keys())))
        ans = input("||-JAY-|| => Did you mean %s instead: " % similar_words_list)
        if "no" in ans:
            jay("Sorry, I don't understand you!!!!")
            check()
        else:
            jay(words_data[ans][0] + "\n")
            check()
                
    else:
        jay("I can't find the word. Please double check it!!!")
        check()

#time teller function for intent response
def timefun():
    jay("The time is" + time.strftime('%l:%M'))

#network ping and speedtest function for intent response
def net():
    net_mes = input("||-JAY-|| => Is it your home network sir: ")
    if "yes" in net_mes.lower():
        os.system("ping -c4 8.8.8.8")
        print("")
        os.system("speedtest --no-upload")
    else:
        ip = input("||-JAY-|| => Please input the gateway of the network your on: ")
        os.system(f"ping -c4 {ip}")
        print("")
        os.system("speedtest --no-upload")
        
#google calendar checker function for intent response
def calendar():
    jay("Here is your google calendar....")
    openbrowser("https://calendar.google.com/calendar")

#gmail checker function for intent response
def gmail():
    reply = input("||-JAY-|| => Personal or School account: ")
    if reply == "cancel":
        pass
    else:
        if "personal" in reply.lower():
            openbrowser(personal_account["email"])
            gmail()
        elif "school" in reply.lower():
            openbrowser(school_account["email"])
            gmail()

#weather checker function for intent response
def weather():
    jay("Here is the weather sir")
    openbrowser("https://www.tomorrow.io/weather/")

#error handler when the JAY isn't familiar with the request
def error():
    jay("Sorry sir, I couldn't understand that, can ypu please repeat that")