from datetime import datetime
from gtts import gTTS
import speech_recognition as sr
import os

language='en'
r2 = sr.Recognizer()

def getData():
    # Write the code to get the date and purpose here
    # Store them in date and pupose respectively
    # both must be of str type when they get stored
    
   with sr.Microphone() as source:#stores the purpose 
     prg='tell me the event please'
     print(prg)
     event=gTTS(text=prg,lang=language,slow=False)
     event.save("event.mp3")
     os.system("start event.mp3")
     r2.adjust_for_ambient_noise(source, duration=5)
     purpose = r2.listen(source)
     print(r2.recognize_google(purpose))
    
   with sr.Microphone() as source:#stores the date
     dte='tell me date'
     print(dte)
     DATE=gTTS(text=dte,lang=language,slow=False)
     DATE.save("DATE.mp3")
     os.system("start DATE.mp3")
     r2.adjust_for_ambient_noise(source, duration=5)
     date = r2.listen(source)
     print(r2.recognize_google(date))
     parseData(date,purpose)
 
def parseData(date,purpose):
  store(date,purpose)

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
            output=gTTS(text=purpose,lang=language,slow=False)
            output.save("output.mp3")
            os.system("start output.mp3")
            
getData()
store()
read()
