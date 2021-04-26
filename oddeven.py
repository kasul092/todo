class odd(:):
    
    def even(self, number):
        self.number = number

        if (number % 2) == 0:  
            print("This number was even number")
        else:
            print("This number is odd number.")
            

odd_object = odd()

m = int(input("Enter the number: "))

s = odd_object.even(m)
#print(s)
