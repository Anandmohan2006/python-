# multilevel inheritance program 

#purwaj  #grandparnets class

class mammal:
    example = "whale"
    def show(self):
        print(f"the {self.example} is the biggest mammel on the earth")

# parent class
        
class animal(mammal):
    like = "human"
    def showThat(self):
        print(f"we {self.like} are also a mammels")
        
        
# child class

class livingBeing (animal):
    thatIS = "humenity"
    def human(self):
        print(f"these all are the part of {self.thatIS} on this beautiful planet")        
        
        
a = mammal()
b = animal()
c = livingBeing()

a.show()
b.showThat()
c.human()
 
 
          