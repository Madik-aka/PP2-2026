def my_generator():
  yield 1 #Keyword,  what makes a function a generator.
  yield 2
  yield 3

for value in my_generator():
  print(value)
#генератор — это автоматический итератор.

""" 
Когда Python видит yield, он:

Превращает функцию в генератор

Автоматически создаёт __iter__() и __next__()

Сам управляет состоянием

Сам вызывает StopIteration

To есть yield = автоматический итератор.
"""

def count_up_to(n):
  count = 1
  while count <= n:
    yield count
    count += 1

for num in count_up_to(5):
  print(num) 



def large_sequence(n):
  for i in range(n):
    yield i

# This doesn't create a million numbers in memory
gen = large_sequence(1000000)
print(next(gen))
print(next(gen))
print(next(gen)) 


def simple_gen():
  yield "Emil"
  yield "Tobias"
  yield "Linus"

gen = simple_gen()
print(next(gen))
print(next(gen))
print(next(gen))


def simple_gen():
  yield 1
  yield 2

gen = simple_gen()
print(next(gen))
print(next(gen))
#print(next(gen))  это уже выйдут как ошибка 


# List comprehension - creates a list
list_comp = [x * x for x in range(5)]
print(list_comp)

# Generator expression - creates a generator
gen_exp = (x * x for x in range(5))  #0,1,2,3,4
print(gen_exp) 
print(list(gen_exp))



# Calculate sum of squares without creating a list
total = sum(x * x for x in range(10))   # 0*0+1*1+2*2+...+9*9=285 
print(total) 

def fibonacci():
  a, b = 0, 1
  while True:
    yield a
    a, b = b, a + b

# Get first 100 Fibonacci numbers
gen = fibonacci()
for _ in range(10):
  print(next(gen))


def echo_generator():
  while True:
    received = yield
    print("Received:", received)

gen = echo_generator()
next(gen) # Prime the generator
gen.send("Hello")
gen.send("World")


def my_gen():
  try:
    yield 1
    yield 2
    yield 3
  finally:
    print("Generator closed")

gen = my_gen()
print(next(gen))
gen.close()
#My examples 
def mygenerator(): 
  yield 1 
  yield 2
  yield 0 
for x in mygenerator(): 
  print(x) 


def mygenerator(): 
  while True:
    y=yield 
    print("Received:", y) 

b=mygenerator() 
next(b) 
b.send("Hello") 
b.send("every one, ") 
b.send("my name is Bektybayev Madiyar!")      


def my_barca():
  try: 
    yield 11
    yield 22
    yield 33
    yield 44
  finally: 
    print("Generator is closed") 

x=my_barca() 
print(next(x))
print(next(x)) 
x.close() 


x=(y*y for y in range(6)) 
print(x) 
print(list(x)) 


SUM=sum(x+x for x in range(10)) 
print(SUM)


def Mygenerator(): 
  yield "Era" 
  yield "Madi" 
  yield "Hatef" 

gen = Mygenerator() 
print(next(gen))
print(next(gen)) 
print(next(gen))      
#iterators and generators exercise 
#1 
def square_generator(n):
    for i in range(n + 1):
        yield i * i

n = int(input("Enter N: "))

for value in square_generator(n):
    print(value)

#2 
def even_numbers(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i

n = int(input("Enter n: "))

print(",".join(str(num) for num in even_numbers(n)))  
#3 
def divisible_by_3_and_4(n):
    for i in range(n + 1):
        if i % 12 == 0:
            yield i

n = int(input("Enter n: "))

for num in divisible_by_3_and_4(n):
    print(num)

#4 
def squares(a, b):
    for i in range(a, b + 1):
        yield i * i

a = int(input("Enter a: "))
b = int(input("Enter b: "))

for value in squares(a, b):
    print(value)

#5 
def countdown(n):
    while n >= 0:
        yield n
        n -= 1

n = int(input("Enter n: "))

for number in countdown(n):
    print(number)          


