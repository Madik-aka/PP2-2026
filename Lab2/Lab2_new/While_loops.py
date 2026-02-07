i = 1
while i < 6:
  print(i)
  i += 1   #  не забудьте увеличить значение i, иначе цикл будет продолжаться вечно.

i = 1
while i < 6:
  print(i)
  if i == 3:
    break  # с помощью break мы остановили цикл, даже если условие верно
  i += 1  


i = 0
while i < 6:
  i += 1
  if i == 3:    # тройки не будет, но будет цифры те которые после нее 
    continue
  print(i)   



i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")  
#My examples 

x=1 
while x<=4: 
  print(x) 
  x+=1  

x=0
while x<6: 
  print(x) 
  if x==4:
    break
  x+=1 


x=1 
while x<5: 
  x+=1   
  if x==3: 
    continue 
  print(x) 


i=0 
while i<6: 
  print(i) 
  i+=1 
else: 
  print("You can not continue")  
 
x=0
while x<=5:
  x+=1
  if x==2: 
    continue 
  print(x) 