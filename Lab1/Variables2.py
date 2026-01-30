x = "Python" #Output variables
y = "is"
z = "awesome"
print(x, y, z) 

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)


x = 5
y = 10
print(x + y)

""" 
x = 5
y = "John"        it's not correct
print(x + y)

"""

x = 5
y = "John"
print(x, y)
#My examples
a="I"
b='like'
c='music'
print(a,b,c) 

a="I "
b='like '
c='music'
print(a + b + c) 

x=50
y=60
print(x+y) 

x='Python'
y='is'
c="cool"
print(x+" " + y+ " "+ c)

x="Euro" 
y=2016
print(x,y) 

#Global variables 
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc() 


x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)


def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)


x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x) 
#My examples
w='Messi' 
w='Neymar' 
def myfunc(): 
  global w 
  w='Raphinha' 
myfunc()  
print('He is now the goat of Barcelona, and his name is ' + w) 

x="good " 
def myfunc():
  x="bad " 
  print("Grades are " + x)
myfunc()
print("Grades are " + x)   

def myfunc(): 
  global q 
  q=80
myfunc() 
print(20+q+q)  


x = "awesome"  #global

def myfunc():
  x = "fantastic" #local
  print("Python is " + x)  

myfunc()

print("Python is " + x )

def myfunc(): 
  global x
  x=125
  print("I like this number: ",x) 
myfunc() 

print("This is my favourite number: ",x)