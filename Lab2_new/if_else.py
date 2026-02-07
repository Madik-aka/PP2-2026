a = 33
b = 200
if b > a:
  print("b is greater than a")

number = 15
if number > 0:
  print("The number is positive")

age = 20
if age >= 18:
  print("You are an adult")
  print("You can vote")
  print("You have full legal rights")       #  All statements must be indented at the same level.


is_logged_in = True   # то есть строка не пустая и поэтому все норм
if is_logged_in:
  print("Welcome back!")

#My examples
x=0 
if x: 
  print("Yes") 
else: 
  print("No") 

""" 
Ноль (0), пустые строки (""), None и пустые коллекции обрабатываются как False. Все остальное обрабатывается как True.

"""       

x=False # пустая строка 
if x: 
  print("icb but yes") 
else: 
  print("Nahh")   

if 5==6: 
  print("Math is gone")
else: 
  print("Math") 
# Elif Statement
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a==b:
  print("a and b are equal")


score = 75

if score >= 90:
  print("Grade: A")
elif score >= 80:
  print("Grade: B")
elif score >= 70:    # You can have as many elif statements as you need.
  print("Grade: C")
elif score >= 60:
  print("Grade: D")    


age = 25
if age < 13:
  print("You are a child")
elif age < 20:
  print("You are a teenager")
elif age < 65:
  print("You are an adult")
elif age >= 65:
  print("You are a senior")
#My examples 
x=4+5
if x>=100:
  print(100) 
elif x>=333: 
  print(333) 
elif x>=6: 
  print("Yeah,you right")      
else: 
  print(0) 

x="Messi" 
y=len(x) 
if y>10: 
  print(10) 
elif y>20: 
  print(20) 
elif y<0: 
  print(0) 
elif y%2==0: 
  print("Even number")
elif y*2==56: 
  print(4) 
elif y==5: 
  print("Yeaaah")
#Else Statement 
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

number = 7
if number % 2 == 0:
  print("The number is even")
else:
  print("The number is odd")                
#My examples 
x=(1,2,3,4,5,6,7) 
if x is int: 
  print("Integer type") 
else: 
  print(type(x)) 
#Shorthand If 
a = 5
b = 2
if a > b: print("a is greater than b") 

a = 2
b = 330
print("A") if a > b else print("B")


a = 10
b = 20
bigger = a if a > b else b
print("Bigger is", bigger)


a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")
#My examples 
a=222 
b=444 
if b/a==2: print(1)  

x=555
y=5
if y+x==560: print("Yes")

x=50
y=10
print(1) if x<y else print("X is bigger") 

a=40
b=10 
c=b if a<b else a 
print(c) 

a=200 
b=400 
if b/a==2: print(1)

x = 15
y = 20
max_value = x if x > y else y
print("Maximum value:", max_value)

username = ""
display_name = username if username else "Guest"
print("Welcome,", display_name)