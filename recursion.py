'''#To find factorial no using recurssion
def myfun(n):
    if n==1:
        return 1
    else:
        return(n*myfun(n-1))
n= int(input("enter the number:"))
z=myfun(n)
print(z)
'''


''' chech if sting is palindrom or not
def pal(n):

    #n="121"
    #n= n.casefold()
    rev=reversed(n)
    if list(n)==list(rev):
        print("PALINDROME")
    else:
        print("not palindrome")

n = int(input("Enter the number: "))        
z=pal(n)
print(z)'''

'''def pal(n):
   
    rev_n=0
    while(n>0):
        remainder=n%10
        rev_n=(rev_n*10)+remainder
        n=n//10
    if n==rev_n:
        print("palindrome")
    else:
        print("not palindrome")

n=int(input("enter the number: "))
temp=pal(n)
print(temp)

'''

'''
def pal():
    n=int(input('enter a number'))
    rev=0
    x=n>0
    #while(n>0):
    rev=(rev*10)+n%10
    n=n//10
    if(x==rev):
        print('its a palindrome number')
    else:
        print("its not a palindrome number")
        return 
        pal()
pal()'''


a=input("enter a string: ")
b=a[-1::-1]

if(a==b):
    print("its a palindrom")
else:
    print("its not palindrom")

'''
def pal():
    n = int(input("enter the number: "))
    rev=0
    x=n>0
    rev=(rev*10)+(n%10)
    n=n//10
    if x==rev:
        print(n,"the number is palindrome")
    else:
        print(n,"the number is not palindorme")
        return 
        pal()
pal()'''

'''
def pri():
    n=int(input("enter the number:"))
    temp=True
    if n==0 or n==1:
        print("the number is not prime nor composite.")
        return

    for i in range(2,n):
        if n%i==0:
            temp=False

    if temp==True:
        print("the number is prime number")
    else:
        print("the number is composite number")

pri()
'''