from datetime import datetime
import os
from gtts import gTTS

language='en'

def getData():
    # Write the code to get the date and purpose here
    # Store them in date and pupose respectively
    # both must be of str type when they get stored

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
            
