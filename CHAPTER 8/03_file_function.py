f = open("file.txt")
# lines = f.readline()   # its just read the lines from files and return a list
 
 
# print(lines,type(lines))

line1 = f.readline()
print(line1)


line4 = f.readline()
print(line4)


line2 = f.readline()
print(line2)
2
line3 = f.readline() 
print(line3)


line5 = f.readline() 
print(line5 == "")

line6 = f.readline() 
print(line6 == "") # this == "" tells that line is empty or not 

f.close()

  # agar next line me kush v nahi ha tho kuch v print nahi hoga 