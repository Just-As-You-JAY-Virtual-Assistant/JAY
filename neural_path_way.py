from getpass import getpass
from neuralintents import GenericAssistant
import os
import nervous_system
import angel_protocol
from static_impulses import jay
import speech
#import nltk
#nltk.download('omw-1.4')



#connections between the brain and the nervous system
mappings = {"greet": nervous_system.greet, 
                "bye":nervous_system.bye, 
                "movies":nervous_system.movies, 
                "music":nervous_system.music, 
                "time":nervous_system.timefun, 
                "study":nervous_system.study, 
                "work":nervous_system.work,
                "search":nervous_system.search,
                "jokes":nervous_system.joke,
                "convo":nervous_system.convo,
                "network":nervous_system.net,
                "gartitude":nervous_system.gratitude,
                "about":nervous_system.about,
                "people":nervous_system.people_search,
                "calendar":nervous_system.calendar,
                "email":nervous_system.gmail,
                "weather":nervous_system.weather,
                "dictionary":nervous_system.dictionary,
                "error":nervous_system.error,
                "angel_protocol":angel_protocol.angel_protocol,
                "sad":speech.sad
                }


#directing the nervous system to the brain
assistant = GenericAssistant('brain.json', intent_methods=mappings ,model_name="test_model")

#starting to read all data in the brain training according to that data
assistant.train_model()
assistant.save_model()
os.system("clear")
print("JAY VIRTUAL ASSISTANT")
def passer():
        username = input("|Username|: ")
        password = getpass("|Password|: ")
        print("")
        if username == "nigus" and password == "tony stark":
                os.system("clear")
                nervous_system.timecheck("All systems are up and running, Good morning", "All systems are up and running, Good evening", "All systems are up and running, Good evening")
                #starting to listen to user
                def requesting(message):
                        assistant.request(message)

                while True:
                        mes = input("|:NIGUS:| => ")
                        requesting(mes)
        else:
                jay("Wrong credentials you have no access")
                passer()

passer()