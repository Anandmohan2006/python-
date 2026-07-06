str = " this is an example foe writting in file"

f = open("writting_file.txt", "a") # a = append mode that is use to add teh text in the end of the file


f.write(str)

f.close()