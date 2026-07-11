a = int(input("enter the 1st number:"))
b = int(input("enter the 2nd number:"))

if(b==0):
    raise ZeroDivisionError("bro python don't perform the division with zero")


else:
   print(f"the division of a/b is {a/b}")