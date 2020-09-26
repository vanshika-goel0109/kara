from datetime import datetime
from gtts import gTTS
import speech_recognition as sr
import webbrowser as wb
import os

language='en'
r2 = sr.Recognizer()

def getData():
    # Write the code to get the date and purpose here
    # Store them in date and pupose respectively
    # both must be of str type when they get stored
    
   with sr.Microphone() as source:#stores the purpose 
     r2.adjust_for_ambient_noise(source, duration=5)
     print('tell me the event please')
     purpose = r2.listen(source)
     print(r2.recognize_google(purpose))
    
   with sr.Microphone() as source:#stores the date
     r2.adjust_for_ambient_noise(source, duration=5)
     print('tell me date')
     date = r2.listen(source)
     print(r2.recognize_google(date))
 

def store(date, purpose):
    f = open("sched.txt","a")
    f.append(date+"#"+purpose)

def read(schedList):
    
    now=datetime.now()
    now=now.strftime("%d%m%Y %H:%M")
    
    for sched in schedList:
        if now in sched:
            purpose=sched.split('#')
            purpose=purpose[1]
            output=gTTS(text=purpose,lang=language,slow=false)
            output.save("output.mp3")
            os.system("start output.mp3")
