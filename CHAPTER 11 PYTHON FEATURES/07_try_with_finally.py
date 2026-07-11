def main():

 try: 
     a = int(input("Enter a number:"))
     print(a)
     
 except Exception as e:  
    print("int (numbers) dalna ha tha")
    
    
 finally:    # its ececutes even in error 
           # error me v run hota ha         
    
    print("now its a finally method with try ")
      
#finally is mainly used foe the function 
#agar function ke bhar rahega ho tab finallly se se the code ka wo finally wala hissa caalega      
      
      
main()      
      