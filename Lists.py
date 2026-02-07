mylist = ["apple", "banana", "cherry"] 
thislist = ["apple", "banana", "cherry"]
print(thislist)   #Элементы списка упорядочены, изменяемы и допускают дублирование значений.
 #в целом: порядок расположения элементов не изменяеться 

thislist = ["apple", "banana", "cherry", "apple", "cherry"]  
print(thislist)

thislist = ["apple", "banana", "cherry"]
print(len(thislist))


list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
list4 = [5.6, 3.4, 6.0] 
print(list4) 

list1 = ["abc", 34, True, 40, "male"]
#My examples 
list5=["Madiyar", 89, 4.3, 6j, None, True, 0] 
print(list5) 
print(len(list5)) 
if "Madiyar" in list5: 
    print(f'Yes Madiyar in this list') 

list1= [1,2,34,5,5,6767,000] 
list2=['m', 'n', 'm', 'jdncls'] 
print(list1); print(list2) 
print(type(list1)) 


mylist = ["apple", "banana", "cherry"]
print(type(mylist))

thislist =list(("apple", "banana", "cherry"))
print(thislist)  

thislist=list(('Apple', 'Banana', 'Cherry')) 
print(thislist) 

#Access List Items
thislist = ["apple", "banana", "cherry"]
print(thislist[1]) 

thislist = ["apple", "banana", "cherry"]
print(thislist[-1]) # -1 refers to the last item, -2 refers to the second last item etc.

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])  #с 2 индекса включительно до 5 индекса не включительного 
#My examples 
list=['Almaty', 'Shymkent', 'Aturay', 'Aktau', 'Aktobe'] 
print(list[3]) 
print(list[-3]) 
print(list[1:4]) 
print(list[-3:-1]) #-1 не вклюсительно
print(list[0]) 

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
#My examples
list=[1,2,3,4,5,6] 
print(list[:2]) 
print(list[1:])
print(list[-3:]) 
print(type(list))
print(len(list)) 
if 1 in list: 
   print("Yeap") 
else: 
   print("Noo")      

#Change List Items 
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)


thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)


thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)
#My examples 
list=[1,2,3,4,5,6,7,8,9,10] 
list[3]="Suiiiii" 
print(list)

list[0:2]="M", "N" 
print(list)

list7=["TVgirl", "Tavis", 'Don Toliver', 'XXXtentasion'] 
list7[0:3]= ['Kairat']  
print(list7) 

#Add list items 
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")   # add an item to the end of the list
print(thislist)


thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)
#My examples 
x=["bread", "button", "milk"] 
x.append("chocolate") 
print(x) 

y=[1,2,3,4,5] 
y.append(6) 
print(y) 

z=['A', 'B', 'C', 'D']    #первый элемент 1, второй 2 и т.д. 
z.insert(3, "O") 
print(z) 

v=['USA','CANADA','RUSSIA','CHINA'] 
v.insert(0, 'KZ') 
print(v) 

p=['Neymar','Iniesta','Xavi'] 
p.insert(0,"Messi") 
p.append("Pique") 
print(p) 


thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical) 
print(thislist)


thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)     # во первых он добавляет все элементы в конец и без разницы tuples,dict,sets,list
print(thislist) 
#My examples 
list0=['o','u','i'] 
list99=['a','b','c'] 
list0.extend(list99) 
print(list0) 

list=[1,2,3,4,5] 
list23={"N","K","J"} 
list.extend(list23) 
print(list) 