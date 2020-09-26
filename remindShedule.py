from datetime import datetime
import os

# Function to Store Appointments
def store(date, purpose):
    f = open("sched.txt","a")
    f.append(date+"#"+purpose)

def read(schedList):
    now=datetime.now()
    now=now.strftime("%d%m%Y %H:%M")
    for sched in schedList:
        if now in sched:
            # The assistant telling the purpose part comes here


