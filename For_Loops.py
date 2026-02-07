fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

for x in "banana":
  print(x)


fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
  

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x) 
#My examples 
list3=["Pear","Mango","Melon"] 
for x in list3: 
  print(x)   

teams=["Como","Juventus","Milan","Inter","Lazio"] 
for x in teams: 
  print(x) 
  if x=="Inter": 
    break    
  
teams=["Como","Juventus","Milan","Inter","Lazio"] 
for x in teams: 
  if x=="Milan": 
    break
  print(x) 

team="Como" 
for x in team: 
  print(x) 

uni="Alma" 
for x in uni: 
  print(x)  


fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)


for x in range(6):   # 6 не включительно
  print(x)


for x in range(2, 6):
  print(x)  


for x in range(2, 30, 3):   # start,stop,step
  print(x)  


for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")


adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
  for y in fruits:
    print(x, y)


for x in [0, 1, 2]:
  pass 
#My examples 
teams=["Bayern", "Bayer", "Borussia Dortmund", "Uion Berlin"] 
for x in teams: 
  if x=="Borussia Dortmund": 
    continue
  print(x) 

for x in range(7): 
  print(x) 
for x in range(2,8): 
  print(x)      

for x in range(1,10,2): 
  print(x) 

list1=["Supreme","Amazing","Unbelievably"] 
list2=["Brad","Christian","Timothee"] 
for x in list1: 
  for y in list2: 
    print(x,y)     