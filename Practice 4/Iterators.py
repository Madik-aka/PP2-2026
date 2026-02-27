#Iterators 
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))    #An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.


mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))


mytuple = ("apple", "banana", "cherry")
for x in mytuple:
  print(x)


mystr = "banana"
for x in mystr:
  print(x)
#Цикл for фактически создает объект iterator и выполняет метод next() для каждого цикла.



class MyNumbers:
  def __iter__(self): # start
    self.a = 1 #Это переменная внутри объекта.
    return self

  def __next__(self): #steps 
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))


class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else: 
      raise StopIteration 

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter: 
  print(x) 

#My examples 
barcelona=("Rolton","Ballon D'or","Crystal","Ferminator") 
myiter=iter(barcelona) 
print(next(myiter)) 
print(next(myiter)) 
print(next(myiter)) 
print(next(myiter)) 


city="Detroit" 
nu=iter(city) 
print(next(nu)) 
print(next(nu)) 
print(next(nu)) 
print(next(nu)) 
print(next(nu)) 
print(next(nu)) 
print(next(nu)) 

Students=("Alimzhan","Ayan","Dias","Arsen") 
for x in Students: 
  print(x) 


class EvenNumbers: 
  def __iter__(self):
    self.v=2
    return self 
  
  def __next__(self): 
    if self.v<=20: 
      x=self.v 
      self.v+=2 
      return x 
    else: 
      raise StopIteration 

myclass=EvenNumbers() 
myiter=iter(myclass) 

for x in myiter:
  print(x) 


class Myclass: 
  def __iter__(self): 
    self.a=5 
    return self 

  def __next__(self): 
    if self.a<=50: 
      x=self.a 
      self.a+=3 
      return x 
    else: 
      raise StopIteration 

myclass=Myclass() 
myiter=iter(myclass) 

for x in myiter: 
  print(x) 