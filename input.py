from datetime import datetime
<<<<<<< HEAD
=======

>>>>>>> 7
def task(n):
    now=datetime.now()
    print("Enter the Today's Task Here:- ")
    i=0
    for i in range(1,n):
        t2=str(input(i))
        if t2=="exit":
            break
<<<<<<< HEAD
        print("Task",i,":-",t2,now.strftime("%d:%m:%Y %H:%M"))
=======
        print("Task",i,":-",t2,now.strftime("%H:%M"))
>>>>>>> 7
task(1000)
