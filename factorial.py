class fact():

    def mult(self, n):
        X= 1
        for i in range(n):
            x = n-i
            X=X*x
            if x==1:
                X=X*x
                return X

f_object = fact()

n = int(input("Enter the number: "))

s = f_object.mult(n)
print("the factorial of ",n, "is", s)

