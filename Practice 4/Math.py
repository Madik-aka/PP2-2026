x = min(5, 10, 25)
y = max(5, 10, 25)
print(x)
print(y)


x = abs(-7.25) # возвращает модуль числа x 
print(x)


x = pow(4, 3) # 4^3=4*4*4=64
print(x)


import math
x = math.sqrt(64)
print(x)


import math
x = math.ceil(1.4) #rounds a number upwards to its nearest integer
y = math.floor(1.4) # rounds a number downwards to its nearest integer
print(x) # returns 2
print(y) # returns 1


import math
x = math.pi # число пи
print(x)
#My examples 
x=max(2,3.4,-2,20) 
print(x) 

u=min(66,-7.7,-444) 
print(u) 

import math 
x=6+3 
print(math.sqrt(x))


import random
x = random.random()
print(x)


import random
x = random.randint(1, 10)
print(x)  


import random
colors = ["red", "green", "blue"]
x = random.choice(colors)
print(x) 


import random
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(numbers)  # например: [3, 5, 1, 4, 2]
#Math execise 
#1
import math

degree = float(input("Input degree: "))
radian = degree * math.pi / 180

print("Output radian:", round(radian, 6))

#2 
height = float(input("Height: "))
base1 = float(input("Base, first value: "))
base2 = float(input("Base, second value: "))

area = (base1 + base2) / 2 * height

print("Expected Output:", area)
#3 
import math

n = int(input("Input number of sides: "))
s = float(input("Input the length of a side: "))

area = (n * s**2) / (4 * math.tan(math.pi / n))

print("The area of the polygon is:", round(area, 2))

#4 
base = float(input("Length of base: "))
height = float(input("Height of parallelogram: "))

area = base * height

print("Expected Output:", area)