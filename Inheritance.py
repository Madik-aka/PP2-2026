class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()



class Student(Person):
  pass

x = Student("Mike", "Olsen")
x.printname()


class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)


class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2019

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)


#My examples 
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("My name is", self.name)

class Dog(Animal):
    pass

d1 = Dog("Buddy")
d1.speak()


class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def show(self):
        print("Brand:", self.brand)

class Car(Vehicle):
    def __init__(self, brand):
        super().__init__(brand)

c1 = Car("Toyota")
c1.show()



class Employee:
    def __init__(self, name):
        self.name = name

    def info(self):
        print("Employee:", self.name)

class Manager(Employee):
    def __init__(self, name, department):
        super().__init__(name)
        self.department = department

m1 = Manager("Alice", "IT")
m1.info()
print("Department:", m1.department)



class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello,", self.name)

class Teacher(Person):
    def subject(self, subject_name):
        print(self.name, "teaches", subject_name)

t1 = Teacher("Mr.Smith")
t1.greet()
t1.subject("Math")



class Shape:
    def describe(self):
        print("This is a shape")

class Circle(Shape):
    def describe(self):
        print("This is a circle")

s1 = Shape()
c1 = Circle()

s1.describe()
c1.describe()
