mytuple = ("apple", "banana", "cherry")
""" 
A tuple is a collection which is ordered and unchangeable.

Tuples are written with round brackets. ()

""" 

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

thistuple = ("apple",)    #One item tuple, remember the comma
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))


tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
tuple1 = ("abc", 34, True, 40, "male") 

thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)
#My examples 
mylist = ["apple", "banana", "cherry"]
thistuple = tuple(mylist) 

x=("a",) 
print(x) 
y=("f") 
print(type(y)) 
print(type(x)) 

r=(1,"g",6j,None, 5.6)
print(type(r)) 
#Access Tuple Items 
thistuple = ("apple", "banana", "cherry")
print(thistuple[1]) # first item has index 0  

thistuple = ("apple", "banana", "cherry")
print(thistuple[-1]) 

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])
# Update Tuples
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"          # так как мы не можем что то изменить когда создали tuple, мы его переминовали в лист и дальше делаем что хотим 
x = tuple(y)
print(x) 

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple) 
#My examples 
tuple1=(1,2,3,4,5) 
list2=list(tuple1) 
list2.append(10) 
tuple1=tuple(list2) 
print(tuple1) 


x = ("Spain","Oslo","Chalamet") 
y=list(x) 
y[2]="Timothee" 
x=tuple(y) 
if type(x) is tuple:
    print("Yes") 
else: 
    print("Nahh") 

a=("Ramos","Cristiano","Toni") 
b=("Bale","Marcelo","Modric") 
b=b+a 
print(b) 

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

thistuple = ("apple", "banana", "cherry")
del thistuple 

#Unpack Tuples
fruits = ("apple", "banana", "cherry")


fruits = ("apple", "banana", "cherry") #Слева от = — переменные
(green, yellow, red) = fruits  # Справа от = — значения
print(green)
print(yellow)
print(red) 


fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)   # red присваивает к себе сразу 3 элемента, которые остались и они будут в форме list


fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)
#My examples 
FCB=("Messi","Neymar","Ronaldinho") 
(ten,eleven,nineteenth)=FCB 
print(ten); print(eleven); print(nineteenth) 

food=("banana","pear","rice","chicken") 
(x,*y,z)=food 
print(x); print(y); print(z) 

menu=("Burger","potato","wings") 
(x,*y)=menu 
print(x); print(y)  

colors = ("red", "green", "blue")
(a, b, c) = colors
print(a)
print(b)
print(c)

subjects = ("math", "physics", "chemistry", "biology", "english")
(first, *others, last) = subjects
print(first)
print(others)
print(last)
#Loop Tuples 
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)


thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])


thistuple = ("apple", "banana", "cherry") 
i=0 
while i<len(thistuple): 
   print(thistuple[i]) 
   i+=1  
#Join Tuples 
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3) 


fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)
#My examples 
color=("Red","Orange","Yellow","Brown") 
color*=2 
print(len(color)) 
print(color)  

a=(6j,6.8,56,"A") 
b=("HERO", "Asmr", 80) 
c=a+b
print(c) 

o=("Abai","Akhmet","Dulatov","Wow") 
x=list(o) 
x.append("Shakarim") 
x.remove("Wow")
o=tuple(x) 
print(o)