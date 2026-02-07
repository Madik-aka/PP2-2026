print(10 > 9)
print(10 == 9)
print(10 < 9) 

a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a") 
#My examples 
print(10==9) 
print(7>8) 
print(1>0.456) 


a=55
b=27

if b<a: 
  print("Yes, a is greater than b") 
else: 
  print("You have a problem")   

x="gggg" 
y="rr" 
a=len(x) 
b=len(y) 
if b>a: 
  print("B") 
else: 
  print("A") 


x=1000/3
y=4444/100
if y>x: 
  print("y is bigger") 
else: 
  print("x is bigger") 

print(100==4)    
print(5>2) 
print(4<5)  


print(bool("Hello"))
print(bool(15))  #Любая непустая строка → True 

x = "Hello"
y = 15

print(bool(x))
print(bool(y))
#My examples 
print(bool(0)) 
print(bool()) 

x=56
y="P" 
print(bool(x)) 
print(bool(y)) 

x=None 
print(bool(x)) 

print(bool([]))  


#Team True
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

#Tean False 
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))


class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj)) 

class myclass(): 
  def __len__(self):  #два тире нижних идет 
    return 1
x=myclass() 
print(bool(x)) 

class myclass(): 
  def __len__(self):
    return 0 
  
x=myclass() 
print(bool(x)) 


def myFunction() :
  return True

print(myFunction())



def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!") 



x = 200
print(isinstance(x, int))
#My examples 
def myfunc(): 
  return False

print(myfunc())


def myFunction(): 
  return True 

print(myFunction()) 

def myfunc(): 
  return True 
if myfunc(): 
  print('Yeah, you right!') 
else: 
  print('Nah, it not correct')  


x=6.7
print(isinstance(x,float))  

a=6j 
print(isinstance(a,complex)) 

c=546
print(isinstance(c,complex)) 
