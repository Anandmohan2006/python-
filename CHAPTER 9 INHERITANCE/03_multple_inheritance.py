class employe:
    company = "bajaj"
    def show(self):
        print(f"the name of the company {self.company}")
        
class coder:
    language = "python"
    def showlanguage(self):
        print(f"the language use in this company is {self.language}")
        
        
class programmer(employe,coder):
    company = "bajaj tech"
    def showboth(self):
        print(f"the employe work in {self.company} with the {self.language} programming language")
        
        
a = employe()
b = coder()
c = programmer()

a.show()
b.showlanguage()
c.showboth()



                