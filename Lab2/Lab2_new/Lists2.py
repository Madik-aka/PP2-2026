thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")    #удалять
print(thislist)  

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")   # remove first banana
thislist.remove("banana")   #remove second banana 
print(thislist) 

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)    #apple=0, banana=1
print(thislist)


thislist = ["apple", "banana", "cherry"]    
thislist.pop()  # если не указываем спец индекс то удаляет последний элемент 
print(thislist) 


thislist = ["apple", "banana", "cherry"]
del thislist 


thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist) 
#My examples 
list1=['FCB','RMA','MC','MU','ATM'] 
list1.remove('ATM') 
print(list1) 

list2=['FCB','FCB','RMA'] 
list2.remove('FCB') 
list2.remove('FCB') 
print(list2)  

x=[10,20,30,40,50] 
x.pop(0) 
x.pop(3)
print(x) 
x.pop() 
print(x) 

v=["Dias","Madi","Ayan","Alim","Aldik","Arsen"] 
del v     # прям все удаляеться 

v=["Dias","Madi","Ayan","Alim","Aldik","Arsen"] 
v.clear() 
print(v) 
#Loop lists 
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)  


thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])    # выводит по индексам 


thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist] 
#My examples 
list2=["LA","DS","PP1","PP2"] 
for y in list2: 
  print(y) 

list1=['Madi','Di','Era'] 
for x in list1:
  print(x) 

Barcelona=[10,11,9,6,5,1] 
for x in range (len(Barcelona)): 
  print(Barcelona[x])     
 

list=['Ata',"Gur","Ast"]  
i=0 
while i<len(list):
  print(list[i]) 
  i+=1    # if we are not write this part it just return Ata infinity time

p=["a","b","c"]  
[print(x) for x in p] 
#List Comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist) 


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist) 
newlist = [x for x in fruits if x != "apple"] 
print(newlist) 

newlist = [x for x in fruits]
print(newlist) 
#My examples 
fruits=['Aplle','Pear','Mango','Pineapple'] 
newlist=[x for x in fruits] # добавляет все элементы с одного на другое 
print(newlist) 


teams=['Kairat','Atyrau','Aktobe'] 
newteams=[x for x in teams if "r" in x] 
print(newteams)
newteams=[x for x in teams if x!='Kairat'] 
print(newteams) 

lego=['china','batman','avanegers'] 
newlego=[x for x in lego]
print(newlego) 

newlist = [x for x in range(10)]
print(newlist) 


newlist = [x for x in range(10) if x < 5] 
print(newlist) 

fruits=['Aplle','Pear','Mango','Pineapple'] 
newlist = [x.upper() for x in fruits]
print(newlist)

fruits=['Aplle','Pear','Mango','Pineapple'] 
newlist = ['hello' for x in fruits]
print(newlist)     #Код создаёт новый список той же длины, но все элементы — "hello".


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x != "banana" else "orange" for x in fruits]  # если вместо банана будет что то другое то ничего не измениться 
print(newlist) 
#My examples 
fruits=['apple','orange','melon','pear'] 
newfruits=[x if x!="melon" else "kiwi" for x in fruits] 
print(newfruits) 

n=[x for x in range(20) if x<10] 
print(n) 

list50=[x.upper() for x in fruits] 
print(list50)

fruits=['apple','orange','melon','pear'] 
new=["Hello,Kz!" for x in fruits]
print(new)  
#Sort Lists 
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()  #Сортирует строки по алфавиту
print(thislist) 

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)


thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)  # от Z к A, а не от A к Z.
print(thislist) 

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist) 


def myfunc(n):
  return abs(n - 50)     #abs — это встроенная функция Python, означает модуль числа 

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)  # key - Это специальный параметр функции sort()
print(thislist) 

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist) 

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)   # буз учета больших букв можно делать сортировку 
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()  # меняет порядок элементов на противоположный
print(thislist) 
#My examples
list1=['b','a','c','z','z','u'] 
list1.sort()
print(list1)  

list2=[1,76,450,2222,2,6] 
list2.sort() 
print(list2) 

list3=[1,2,456,0,42,22] 
list3.sort(reverse = True)
print(list3) 

teams=['barcelona','RM','MC'] 
teams.sort(key = str.lower) 
print(teams) 
teams=['barcelona','RM','MC'] 
teams.reverse() 
print(teams) 