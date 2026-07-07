
class employee:

    language = "python"
    salary = 6000000
    age = 20

    def getinfo(self):
        print(f"The language is {self.language} and the salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good Morning")


satyam = employee()

satyam.language = "C++"

print(satyam.language)
print(satyam.salary)

satyam.greet()
satyam.getinfo()