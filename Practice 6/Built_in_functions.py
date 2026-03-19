from functools import reduce

# 1. map и filter
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
even = list(filter(lambda x: x % 2 == 0, numbers))
print(squared)
print(even)

# 2. reduce
total = reduce(lambda x, y: x + y, numbers)
print("Сумма чисел через reduce:", total)

# 3. enumerate и zip
names = ["Ali", "Bob", "Charlie"]
ages = [20, 21, 22]                       

print("С индексами через enumerate:")
for i, name in enumerate(names):
    print(i, name)

print("Сочетание имён и возрастов через zip:")
for name, age in zip(names, ages):
    print(name, age)

# 4. Проверка типов и преобразование
x = "123"
if isinstance(x, str):
    x = int(x)
print (x, type(x)) 



