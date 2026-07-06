# **File I/O (Input/Output) in Python** is the process of reading data from a file and writing data to a file. It allows a program to store, retrieve, and manage data permanently, even after the program has ended.


#we use file because the file run in the ram that not stored permanantly 


#writting a code to get the data from the (file.txt)


f = open("file.txt") 
data = f.read()
print(data)
f.close()



