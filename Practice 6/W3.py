#The open() function takes two parameters; filename, and mode.
f=open("demofile.txt","x")
"""

"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist   удадяет старый файл и записывает заново

"x" - Create - Creates the specified file, returns an error if the file exists

"""





""" 

"t" - Text - Default value. Text mode

"b" - Binary - Binary mode (e.g. images)


"""

f = open("demofile.txt") 
f = open("demofile.txt", "rt") #The code above is the same 


f = open("demofile.txt")
print(f.read())


#f = open("D:\\myfiles\welcome.txt")
#print(f.read())       it is possible to open file on a different location 


with open("demofile.txt") as f:
  print(f.read())


f = open("demofile.txt")
print(f.readline())
f.close()   #If you are not using the with statement, you must write a close statement in order to close the file 


with open("demofile.txt") as f:
  print(f.read(5))  #первые 5 букв


with open("demofile.txt") as f:
  print(f.readline())  #return one line
  print(f.readline())
  print(f.readline()) 



with open("demofile.txt") as f:
  for x in f:
    print(x)


#My examples 
f=open("megaknight.txt") 
f=open("megaknight.txt", "rt")
print(f.read()) 

f=open("megaknight.txt") 
print(f.readline())  
f.close() 


with open("megaknight.txt") as f: 
  print(f.read) 
  print(f.readline()) 
  print(f.readline()) 
  print(f.read(5))



with open("megaknight.txt") as f: 
  for x in f: 
    print(x) 

with open("megaknight.txt","a") as f:
  f.write("Congratulations!\n") 





with open("demofile.txt", "a") as f:
  f.write("Now the file has more content!")

#open and read the file after the appending:
with open("demofile.txt") as f:
  print(f.read())



with open("demofile.txt", "w") as f:
  f.write("Woops! I have deleted the content!")

#open and read the file after the overwriting:
with open("demofile.txt") as f:
  print(f.read())


 



import os
os.remove("demofile.txt")    # deleted this file


import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist") 


import os
#os.rmdir("myfolder")  #Удалять можно только пустые папки.




from functools import reduce 
numbers=[1000,2000,3000,5000] 
skidka=list(map(lambda x: x*0.9, numbers)) 
c=list(filter(lambda x: x>2000, numbers)) 
print("Цены со скидкой:", skidka) 
print("Подходящий под требование:", c) 
         