from datetime import datetime

def task(n):
    now=datetime.now()
    print("Enter the Today's Task Here:- ")
    i=0
    for i in range(1,n):
        t2=str(input(i))
        if t2=="exit":
            break
        print("Task",i,":-",t2,now.strftime("%H:%M"))
task(1000)
