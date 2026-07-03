


marks = {

"aditya" : 100,
"satyam" : 55,
"manish" : 65,
"tiwari" : 26,

} 

print(marks.items())  #.items convert all the itemes in tuple 

print(marks.keys())  #.keys gives key items from the dictnory

print(marks.values())  # .values gives the values from the dictnory

marks.update({"aditya" : 99, "mahema": 71})  #.update method is used to do changes in the dictnory


print(marks) 


print(marks.get("aditya2"))  #.get method does not give error itd provide none

print(marks["aditya"]) # its provides errror