"""
Function definition and calling
Function arguments (positional, default, *args, **kwargs)
Return values and statements
Passing lists and other data types as arguments
Function documentation with docstrings
""" 
def my_function():
  print("Hello from a function") 
my_function() 
my_function() 
my_function() 


temp1 = 77
celsius1 = (temp1 - 32) * 5 / 9
print(celsius1)

temp2 = 95
celsius2 = (temp2 - 32) * 5 / 9    # exercise without function()
print(celsius2)

temp3 = 50
celsius3 = (temp3 - 32) * 5 / 9
print(celsius3)


def fahrenheit_to_celsius(fahrenheit):
  return (fahrenheit - 32) * 5 / 9   #если функция что-то вычисляет — почти всегда нужен return.

print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(95))
print(fahrenheit_to_celsius(50)) 


def get_greeting():
  return "Hello from a function"

message = get_greeting()
print(message) 


def get_greeting():
  return "Hello from a function"

print(get_greeting())

def my_function(): pass 
#My examples  
def my_function(): 
  print("Hello,Aryn!") 
my_function()   
my_function() 


def celsius_to_Kelvin(celsius): 
  return(celsius+273) 

print(celsius_to_Kelvin(10)) 
print(celsius_to_Kelvin(-12)) 
print(celsius_to_Kelvin(-146)) 
print(celsius_to_Kelvin(77))  


def example():
    print("Start")
    return 10    #return немедленно завершает выполнение функции. Это означает, что функция останавливается прямо здесь.
    print("End")  # никогда не выполнится
example()  

def barcelona(): 
  a=10 
  b=20 
  return a+b 
  c=a+b 
  print(c) 
result=barcelona()  
print(result)  

def i_will(): 
  return "I promise i will study late" 
result=i_will() 
print(result) 
# Function Arguments 
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")


def my_function(name): # name is a parameter
  print("Hello", name)

my_function("Emil") # "Emil" is an argument


def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")   #function expects 2 arguments, and gets 2 arguments 


def my_function(name = "friend"):
  print("Hello", name)

my_function("Emil")
my_function("Tobias")
my_function()
my_function("Linus")


def my_function(country = "Norway"):
  print("I am from", country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil") 
#My examples 
def myfunction(age=19):
  print("I am", age, "years old!") 

myfunction(20) 
myfunction(10) 
myfunction() 

def myfunction(mname): 
  print(mname + "Sergio") 

myfunction("Ramos ") 
myfunction("Busquetes ") 
myfunction("Aguero ")  

def myfunction(mname, fname): 
  print(mname + " " + fname)

myfunction("Madiyar", "Aruzhan") 
myfunction("Erasyl", "Zere") 
myfunction("Dashon", "Chel") 



def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function(animal = "dog", name = "Buddy")


def my_function(animal, name, age):
  print("I have a", age, "year old", animal, "named", name)

my_function("dog", name = "Buddy", age = 5) 


def my_function(fruits):
  for fruit in fruits:
    print(fruit)

my_fruits = ["apple", "banana", "cherry"]
my_function(my_fruits) 


def my_function(person):
  print("Name:", person["name"])
  print("Age:", person["age"])

my_person = {"name": "Emil", "age": 25}
my_function(my_person)  #переменная = значение
#My examples 
def myfunction(Barcelona): 
  for x in Barcelona: 
    print(x) 

myplayers=["Messi", "Neymar", "Iniesta"]     
myfunction(myplayers) 

def myfunction(age, subject, name): 
  print("My name is " + name, "I'm ",  age, "years old" + " and i like " + subject) 

myfunction(19, "physics", "Madiyar")  

def myfunction(age, name): 
  print(f"I'm " , age, "and my name is " , name) 

myfunction(age=19, name="Madiyar")  



