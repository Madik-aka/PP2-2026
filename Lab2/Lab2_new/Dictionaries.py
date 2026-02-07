thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict) 


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])


thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)

#Access Dictionary Items
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.add["color:"]="red"
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("model") 



car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.clear()



#1
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
#2
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])
#3
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)
#4
print(len(thisdict))
#5
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
#6
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict))
#7
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)



#1
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
#2
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
#3
print(myfamily["child2"]["name"])


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
#1
for x in thisdict:
    print(x)
  
#2
for x in thisdict:
    print(thisdict[x])
#3
for x in thisdict.values():
    print(x)
#4
for x in thisdict.keys():
    print(x)
#5
for x, y in thisdict.items():
    print(x, y) 
      
my_dict=dict(name="Madiyar", age=18, city="Almaty")
print(my_dict) 
print(type(my_dict))  


person=dict(name="Arman", age=34,city="London" ) 
person["occupation"]=("Engineer")  
print(f"After adding occupation: {person}")
person["age"]=(31) 
print(person ) 

del person["city"] # deleted, то есть удаляем city 
print(person) 
person.pop("name")  
print(person) 


persons=dict(name= "Leo", age= 37, city= "Miami") # создаем словарь 
for value in persons.values(): 
    print(value) 

for key, value in persons.items():
    print(f"Key: {key}, Value: {value}")    # f- Позволяет вставлять переменные прямо в текст.