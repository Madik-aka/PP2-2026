#Copy Lists 
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()  
print(mylist)

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)   
print(mylist)  

thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]     # все три функции делает одно и тоже 
print(mylist)
#My examples 
list1=["Cilian", "Kylian", "Pitt"] 
list2=list1.copy() 
print(list2) 

list1=[1,2,3,4,5,6,7] 
list3=list(list1) 
print(list3)


teams=["Chicago Bulls", "Lakers", "New York"] 
new_teams=teams[:] 
print(new_teams) 

x=[1,2,43,54545,667] 
x.sort() 
y=x.copy() 
print(y) 

list=["Apple","Banana","Cherry","Mango"] 
list2=[x for x in list] 
list3=list2[:] 
print(list3) 
#Join Lists
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3) 


list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]  
for x in list2:
  list1.append(x)

print(list1)


list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)
#My examples 
a=[1,2,3,4] 
b=[5,6,7,8] 
c=a+b 
print(c) 

t=["Lamine Yamal", "Pedri", "Frenkie"] 
y=["Raphinha", "Robert"] 
for x in y: 
  t.append(x)     

print(t) 

list1=[10,20,30,40,50] 
list2=[60,70,80,90] 
list1.extend(list2) 
print(list1) 