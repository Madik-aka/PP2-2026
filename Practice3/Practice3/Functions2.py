"""
Function definition and calling
Function arguments (positional, default, *args, **kwargs)
Return values and statements
Passing lists and other data types as arguments
Function documentation with docstrings
""" 
#Python *args and **kwargs
def my_function(*kids):  # используем когда не знаем сколько аргументов передадут нам 
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")


def my_function(*args):
  print("Type:", type(args))
  print("First argument:", args[0])
  print("Second argument:", args[1])
  print("All arguments:", args)

my_function("Emil", "Tobias", "Linus")  


def my_function(greeting, *names):
  for name in names:
    print(greeting, name)

my_function("Hello", "Emil", "Tobias", "Linus")


def my_function(*numbers):
  total = 0
  for num in numbers:
    total += num
  return total

print(my_function(1, 2, 3))
print(my_function(10, 20, 30, 40))
print(my_function(5)) 


def my_function(*numbers):
  if len(numbers) == 0:
    return None
  max_num = numbers[0]
  for num in numbers:
    if num > max_num:
      max_num = num
  return max_num

print(my_function(3, 7, 2, 9, 1))


def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")


def my_function(**myvar):
  print("Type:", type(myvar))
  print("Name:", myvar["name"])
  print("Age:", myvar["age"])
  print("All data:", myvar)

my_function(name = "Tobias", age = 30, city = "Bergen") 

#Python Scope 
def myfunc():
  x = 300
  print(x)

myfunc()


def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()   # если мы создали функцию внутри функции то х нам доступен за внутренней 


x = 300  # global scope 
def myfunc():
  print(x)

myfunc()
print(x)


def myfunc():
  global x
  x = 200

myfunc()
print(x)


def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x
print(myfunc1())


x = "global"

def outer():
  x = "enclosing"
  def inner():
    x = "local"
    print("Inner:", x)
  inner()
  print("Outer:", x)

outer()
print("Global:", x)
#My examples 
x=100 
def myfunction(): 
  global x 
  x=101 
  print(x) 
myfunction()  
print(x) 


x=150 
def myfunction(): 
  x=100 
  print(x) 
myfunction() 
print(x) 


def myfunction(): 
  x=100 
  def myfunction2(): 
    print(x) 
  myfunction2()
myfunction() 


def myfunc(): 
  x="Jenna" 
  def myfunc2(): 
    nonlocal x 
    x="Watson" 
  myfunc2() 
  return x
print(myfunc())   
