def task(n):
    #n=int(input("Enter the number of today's Tasks:- "))
    print("Enter the Today's Task Here:- ")
    i=0
    for i in range(1,n):
        t2=str(input(i))
        if t2=="exit":
            break
        print("Task",i,":-",t2)
        
task(1000)
