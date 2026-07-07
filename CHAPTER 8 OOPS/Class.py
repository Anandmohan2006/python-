class employee:
                        # this is a class attributes 
    language = "python"
    salary = 6000000
    age = 20
    
    
satyam = employee()
satyam.name = "satyam"   # this is a object attributes


print(satyam.name, "\n" ,satyam.language, "\n",satyam.age,"\n" ,satyam.salary)

print("")

aditya = employee()
aditya.name = "aditya" 
print(aditya.name, "\n" ,satyam.language, "\n",satyam.age,"\n" ,satyam.salary)   



# in this code the class is ( employee) and the objects are the (satyam,aditya, python etc)