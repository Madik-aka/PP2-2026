class MyClass:
  x = 5 

p1 = MyClass()
print(p1.x)
del p1 


p1 = MyClass()
p2 = MyClass()
p3 = MyClass()

print(p1.x)
print(p2.x)
print(p3.x)
#_init_method 
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Emil", 36)

print(p1.name)
print(p1.age)

class Person:
  def __init__(self, name, age=18):
    self.name = name
    self.age = age

p1 = Person("Emil")
p2 = Person("Tobias", 25)

print(p1.name, p1.age)
print(p2.name, p2.age)
#My examples 
class Movie:
    def __init__(self, title, year=2020):
        self.title = title
        self.year = year

m1 = Movie("Inception")
m2 = Movie("Interstellar", 2014)

print(m1.title, m1.year)
print(m2.title, m2.year)

class Course:
    def __init__(self, name, students=0):
        self.name = name
        self.students = students

c1 = Course("Python")
c2 = Course("Math", 25)

print(c1.name, c1.students)
print(c2.name, c2.students)

class Phone:
    def __init__(self, model, battery=100):
        self.model = model
        self.battery = battery

ph1 = Phone("Samsung")
ph2 = Phone("iPhone", 80)

print(ph1.model, ph1.battery)
print(ph2.model, ph2.battery)
# self Parameter
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def greet(self):
    print("Hello, my name is " + self.name)

p1 = Person("Emil", 25)
p1.greet()


class Person:
  def __init__(self, name):
    self.name = name

  def printname(self):
    print(self.name)

p1 = Person("Tobias")
p2 = Person("Linus")

p1.printname()
p2.printname()


class Person:
  def __init__(self, name):
    self.name = name

  def greet(self):
    return "Hello, " + self.name

  def welcome(self):
    message = self.greet()
    print(message + "! Welcome to our website.")

p1 = Person("Tobias")
p1.welcome()
#My examples 
class Student:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        return "My name is " + self.name

    def speak(self):
        text = self.introduce()
        print(text + " and I am a student.")

s1 = Student("Ali")
s1.speak()


class Book:
    def __init__(self, title):
        self.title = title

    def info(self):
        return "This book is called " + self.title

    def display(self):
        description = self.info()
        print(description + ".")

b1 = Book("Python Basics")
b1.display()


class User:
    def __init__(self, username):
        self.username = username

    def login(self):
        return "User " + self.username + " logged in"

    def show_status(self):
        status = self.login()
        print(status + " successfully.")

u1 = User("Emil123")
u1.show_status()


class Student:
    school = "High School"   # class variable

    def __init__(self, name):
        self.name = name     # instance variable

s1 = Student("Ali")
s2 = Student("Sara")

print(s1.school)
print(s2.school)

Student.school = "New School"

print(s1.school)
print(s2.school)


class Car:
    wheels = 4   # class variable

    def __init__(self, brand):
        self.brand = brand

c1 = Car("Toyota")
c2 = Car("BMW")

c1.brand = "Honda"

print(c1.brand)
print(c2.brand)


class Phone:
    category = "Electronics"

    def __init__(self, model):
        self.model = model

p1 = Phone("iPhone")
p2 = Phone("Samsung")

p1.category = "Smart Device"

print(p1.category)
print(p2.category)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Tom", 25)

del p1.age

# print(p1.age)  # будет ошибка


class Game:
    type = "Online"

    def __init__(self, name):
        self.name = name

g1 = Game("Dota")

del Game.type

# print(g1.type)  # будет ошибка

