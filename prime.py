class prime():

    def num(self, n):
        
        n = int(input("Enter the number: "))
        s= True
        if n==0 or n==1:
            print("This is not a prime nor composite number")
            return 

        for i in range(2,n):
            if n%i==0:
                s=False

        if s==True:
                print("This number was prime number.")
        else:
            print("This number was not prime number.")

prime_object = prime()

s = prime_object.num(1)
#print(s)

#print(s)


'''
num = int(input("Enter a number: "))  
  
if num > 1:  
   for i in range(2,num):  
       if (num % i) == 0:  
           print(num,"is not a prime number")  
           print(i,"times",num//i,"is",num)  
           break  
   else:  
       print(num,"is a prime number")  
         
else:  
   print(num,"is not a prime number")  '''