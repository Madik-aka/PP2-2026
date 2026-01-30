x = "awesome"   #global variables can be used by everyone, both inside of functions and outside.

def myfunc():
  print("Python is " + x)

myfunc() 
#myexample
y='good' 
def myfunc():
  print('All is ' + y)

myfunc()  

c='best' 
def myfunc(): 
  print('KBTU is the ' + c) 
myfunc() # if we don't write myfunc() we can not see the message   



x = "awesome"  #global

def myfunc():
  x = "fantastic" #local
  print("Python is " + x)  

myfunc()

print("Python is " + x )

#myexample

x="good"
def myfunc():
   x='bad'
   print('All is ' + x) 
myfunc() 

print('All is ' + x) 

x = 55
def myfunc(): 
  x = 65
  print(40 + x)  #print=()  is wrong method 

myfunc() 

print(40 + x)  


z=100

def myfunc(): 
  z=200
  print(100+z) 

myfunc() 
print(100+z)  

#The global Keyword - we can create global variable inside the function and can use it outside the function
def myfunc():
  global x      
  x = "fantastic"

myfunc()

print( 'Python is ' + x)

#myexample 
def myfunc(): 
  global x 
  x=37
  print(60+x) 
myfunc() 
print(63+x)  

def myfunc(): 
  global q 
  q=80
myfunc() 
print(20+q+q)  



x = "awesome"
x='great'
def myfunc():
  global x
  x = "not bad"  #To change the value of a global variable inside a function, refer to the variable by using the global keyword

myfunc()

print("Python is " + x)

#myexample 

x=100
def myfunc(): 
  global x 
  x=1
myfunc() 

print(999+x) 


w='Messi' 
w='Neymar' 
def myfunc(): 
  global w 
  w='Raphinha' 
myfunc()  
print('He is now the goat of Barcelona, and his name is ' + w) 
