thisset = {"apple", "banana", "cherry"}
print(thisset)     # Наборы неупорядочены, поэтому вы не можете быть уверены, в каком порядке будут отображаться элементы.

thisset = {"apple", "banana", "cherry", "apple"}      
print(thisset) 

thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)

thisset = {"apple", "banana", "cherry", False, True, 0}
print(thisset) 

thisset = set(("apple", "banana", "cherry")) # note the double round-brackets  {}
print(thisset) 
#My examples
fruits1 = {"mango", "orange", "kiwi"}
print(fruits1)  # порядок может быть любым

fruits2 = {"mango", "orange", "kiwi", "mango", "kiwi"}
print(fruits2)  # повторяющиеся элементы удаляются

myset1 = {"apple", 1, 2, 3, True, False}
print(myset1)  # числа и булевы значения могут смешиваться

myset2 = {True, False, 0, 1, 2, 3}
print(myset2)  # True=1, False=0 → дубли удаляются

myset3 = set(("cat", "dog", "mouse"))  # двойные скобки
print(myset3)
#Access Set Items
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

thisset = {"apple", "banana", "cherry"}
print("banana" not in thisset)  
#Add Set Items 
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")     # .append() in lists, .add() in sets 
print(thisset) 


thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)


thisset = {"apple", "banana", "cherry"}
mytuple = ("kiwi", "orange")
thisset.update(mytuple)
print(thisset)
#My examples 
x={1,2,3,4,5,6} 
x.add(7) 
print(x) 

x={"Apple","BMW","School","Garden"} 
y={"J"} 
x.update(y) 
i=(1,2,4) 
x.update(i) 
print(x) 
#Remove Set Items 
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset) 


thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset) 


thisset = {"apple", "banana", "cherry"}
x = thisset.pop()     # Remove a random item
print(x)  
print(thisset) 


thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)


thisset = {"apple", "banana", "cherry"}
del thisset
#My examples 
thisset={"A","B" ,"N"} 
thisset.pop() 
print(thisset) 

set4={"Nan","May","Chai"} 
set4.remove("Nan") 
print(set4) 
set4.discard("May") 
print(set4) 

set4={"Nan","May","Chai"} 
del set4 

set4={"Nan","May","Chai"}
set4.clear() 
print(set4) 

#Loop Sets
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x) 
# Join Sets 
# Объединение множеств
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)  # вариант с union()
print("union():", set3)

set3 = set1 | set2        # короткая запись через |
print("| :", set3)

#Обновление множества на месте
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set1.update(set2)
print("update():", set1)

#Пересечение множеств
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print("intersection():", set3)

#Симметричная разница (элементы, которых нет в обоих одновременно)
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 ^ set2
print("symmetric_difference (^):", set3)

#Симметричная разница с обновлением на месте
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.symmetric_difference_update(set2)
print("symmetric_difference_update():", set1)  


x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x)) 
