
class employee:

    language = "python"
    salary = 6000000
    age = 20
    
    
    def __init__(self):
      print( "i am crating an object")

    def getinfo(self):
        print(f"The language is {self.language} and the salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good Morning")


satyam = employee()
satyam.name = "satyam"
print(satyam.name,satyam.salary)


rohan = employee()