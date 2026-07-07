class employee:
                       
    language = "python" 
    salary = 6000000
    age = 20
    
    def  getinfo(self):   #self is  used to 
        print(f"The language is { self.language}. and the salary is {self.salary}")
    
    
satyam  = employee()

satyam.language = "c++"    


print(satyam.language,"\n", satyam.salary)


satyam.getinfo()