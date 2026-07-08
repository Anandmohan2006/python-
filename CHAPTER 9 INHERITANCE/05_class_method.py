class school:
    s = "st andrews"
    @classmethod # this is a class method that is used to give the class attributes even if instance attributes is present
    
    
    def show(cls):
        print(f"the collage name is   {cls.s}")
        
        
        
a = school()


a.show()        
    
