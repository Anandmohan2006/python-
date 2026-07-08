#parnet class

class animal:
    def speak(self):
        print("animal make sound")
        
    #child class    
class dog(animal):
    def bark(self):    
        print("bog can bark")  
        
        
#createing object   
d = dog()


d.speak()
d.bark()          