from datetime import datetime
import os
from gtts import gTTS

language='en'

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
            purpose=sched.split('#')
            purpose=purpose[1]
            output=gTTS(text=purpose,lang=language,slow=false)
            output.save("output.mp3")
            os.system("start output.mp3")
            
