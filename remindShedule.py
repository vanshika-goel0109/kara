from datetime import datetime
import os
import speech_recognition as sr
import webbrowser as wb

r2 = sr.Recognizer()

func()

# Function to Store Appointments

def store(date, purpose):
    f = open("sched.txt","a")
    f.append(date+"#"+purpose)

def read(schedList):
    
    now=datetime.now()
    now=now.strftime("%d%m%Y %H:%M")
    
    for sched in schedList:
        if now in sched:
            #inputs for meeting reminder
            purpose=sched.split('#')
            purpose=sched[1]
            # Purpose is to be spoken out along with time
            
            # The assistant telling the purpose part comes here
            
            with sr.Microphone() as source:
            r2.adjust_for_ambient_noise(source, duration=5)
            print('tell me the event please')
            purpose = r2.listen(source)
            print(r2.recognize_google(purpose))
            
             # The assistant telling the date part comes here
            with sr.Microphone() as source:
            r2.adjust_for_ambient_noise(source, duration=5)
            print('tell me date')
            date = r2.listen(source)
            print(r2.recognize_google(date))
 
