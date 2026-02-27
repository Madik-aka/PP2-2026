import json 


import json
# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'   #JSON пишеться весь в один строку, не как словарь
# parse x:
y = json.loads(x)
# the result is a Python dictionary:
print(y["name"])
print(y)



import json
# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}
# convert into JSON:
y = json.dumps(x)
# the result is a JSON string:
print(y)



import json
print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))



import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
json.dumps(x, indent=4)
json.dumps(x, indent=4, separators=(". ", " = "))
json.dumps(x, indent=4, sort_keys=True)
print(json.dumps(x))
#My examples 
import json
data = '{"student": "Madiyar", "grade": 95}'
result = json.loads(data)
print(result["student"]) 


import json
person = {"name": "Anna", "age": 22}
json_data = json.dumps(person)
print(json_data)


import json
numbers = [1, 2, 3, 4]
print(json.dumps(numbers))


import json
data = {
    "user": "Bektybayev",
    "active": True,
    "scores": [90, 85, 88],
    "address": None
}

print(json.dumps(data, indent=4))



import json
data = {"a": 1, "b": 2, "c": 3}
print(json.dumps(data, indent=2))
#JSON exercise 
import json

with open(r"C:\Users\Acer-\OneDrive\Рабочий стол\PP2 Labs\Practice 4\sample-data.json") as f:
    data = json.load(f)

print("Interface Status")
print("=" * 80)
print("{:<50} {:<20} {:<8} {:<6}".format("DN", "Description", "Speed", "MTU"))
print("-" * 80)

for item in data["imdata"]:
    attr = item["l1PhysIf"]["attributes"]
    
    dn = attr.get("dn", "")
    descr = attr.get("descr", "")
    speed = attr.get("speed", "")
    mtu = attr.get("mtu", "")
    
    print("{:<50} {:<20} {:<8} {:<6}".format(dn, descr, speed, mtu))