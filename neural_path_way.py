from neuralintents import GenericAssistant
import os
import nervous_system
import time
import nltk

nltk.download('omw-1.4')



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
            "error":nervous_system.error
            }


#electric waves for the brain to send messages
assistant = GenericAssistant('brain.json', intent_methods=mappings ,model_name="test_model")
assistant.train_model()
assistant.save_model()
os.system("clear")
print("Waking up....")
time.sleep(1)
print("Warming up neural_pathways.......")
time.sleep(1)
nervous_system.timecheck("All good to go, Good morning sir", "All good to go, Good evening sir", "All good to go, Good evening sir")


while True:
        message = input("\n||NIGUS||: ")
        assistant.request(message)