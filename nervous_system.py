import datetime
import time
import os
import warnings
warnings.catch_warnings()
warnings.simplefilter("ignore")
from static_impulses import *


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
    jay("Do you want any music while studying?")
    task_checker("Opening your notebook", "chill lofi")
    openbrowser("https://docs.google.com/document/u/1/?tgif=d")
    jay("Have a nice study session sir.")

#work session manager function for intent response
def work():
    jay("Setting up workstation")
    jay("Will you be working on programming or networking")
    env_check("https://nigussolomon.atlassian.net/jira/your-work")

#movie manager function for intent response
def movies():
    type = input("||-JAY-|| => Movies or Shows, Sir: ")
    if type.lower() == "shows":
        openbrowser(f"https://hdtoday.tv/filter?type=tv&quality=all&release_year={datetime.datetime.now().year}&genre=all&country=all")
    elif type.lower() == "movies":
        openbrowser(f"https://hdtoday.tv/filter?type=movie&quality=all&release_year={datetime.datetime.now().year}&genre=all&country=all")
    else:
        jay("Didn't understand that sir!")
        movies()

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
    jay("What do you want to search for, sir?")
    searchtitle = input("||-SEARCH-|| =>  ")
    if searchtitle.lower() == "cancel":
        pass
    else:
        jay("Searching...")
        jay("Here are the search results sir")
        googlesearch(searchtitle)
        search()

#wiki or google search for people function for intent response
def people_search():
    value = 0
    jay("Please, the full Name of the person your looking for")
    name = input("||-NAME-|| => ")
    for i in ["cancel", "stop", "leave it", "leave"]:
        if i in name:
            value+=1

    if value > 0:
        pass
    else:
        jay("Do you need details")
        reply = input("||-CONFIRMATION-|| => : ")
        if "yes" in reply:
            googlesearch(name)
            print("")
            people_search()
        else:
            try:
                import wikipedia
                print(wikipedia.summary(name))
            except:
                jay(f"Can't find {name}, Sir, Do you want to do a google search")
                error = input("||-CONFIRMATION-|| => ")
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
        jay("Do you want to search for another word, Sir?")
        reply = input("||-CONFIRMATION-|| => ")
        if "yes" in reply:
            dictionary()
        else:
            pass
    words_data = json.load(open("words.json"))
    jay("Please enter a word, Sir")
    word = input("||-SEARCH KEY-|| => ")

    word = word.lower()
    if word in words_data or word.title() in words_data or word.upper() in words_data:
            res = words_data[word][0]
            jay(f"{str(res)}\n")
            check()
    elif len(get_close_matches(word, words_data.keys())) >0:
        similar_words_list = list(map(str, get_close_matches(word, words_data.keys())))
        jay("Did you mean %s instead: " % similar_words_list)
        ans = input("||-CONFIRMATION-|| => ")
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

#network ping function for intent response
def net():
    jay("Is it your home network, Sir?")
    net_mes = input("||-CONFIRMATION-|| =>  ")
    if "yes" in net_mes.lower():
        jay("Checking local network")

        net_local_res = (os.system("ping -c4 192.168.1.1"))
        if net_local_res == 0:
            jay("Local network is up and running")
            jay("Pinging Google servers")
            net_remote = (os.system("ping -c4 192.168.1.1"))

            if net_remote == 0:
                jay("Internet is up and running too sir")
            else:
                jay("There seems to be an Internet failure sir.")
        else:
            jay("There seems to be a network failure sir.")
        
        

    else:
        jay("Please input the gateway address of the network your on")
        ip = input("||-GATEWAY-|| => ")
        jay("Checking local network")

        net_res = (os.system(f"ping -c4 {ip}"))
        if net_res == 0:
            jay("Local network is up and running")
            jay("Pinging Google servers")
            net_remote = (os.system("ping -c4 192.168.1.1"))

            if net_remote == 0:
                jay("Internet is up and running too sir")
            else:
                jay("There seems to be an Internet failure sir.")
        else:
            jay("There seems to be a network failure sir.")
        
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
    openbrowser("https://www.tomorrow.io/weather/ET/AA/Addis_Ababa/038587/")

#error handler when the JAY isn't familiar with the request
def error():
    jay("Sorry sir, I couldn't understand that, can ypu please repeat that")