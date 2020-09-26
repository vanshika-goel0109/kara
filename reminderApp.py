import remindShedule

while(True):
    f=open("sched.txt","a")
    schedList=f.readlines()
    remindShedule.read(schedList)