import remindMedicine

while(True):
    f=open("sched.txt","a")
    schedList=f.readlines()
    remindMedicine.read(schedList)