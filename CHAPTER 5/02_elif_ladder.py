# vote eligibility program using
# elif ladder statement 

a = int(input("Enter your age: "))


if (a>= 18):
    print("You are eligible to vote.")

elif(a<0):
    print("you entering negative age which is not possible")

elif(a==0):
    print("you are entering zero pagal ho gaye ho kya")


else:

    print("You are a minor.")
