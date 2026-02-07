# Logical Operators
x = 5
print(x > 0 and x < 10) 

x = 5
print(x < 5 or x > 10)

x = 5
print(not(x > 3 and x < 10))
#My examples
x=4
print(x>1 and x<222) 

x=50
print(x>60 or x<100) 

x=1 
print(not(x<0 and x>2))
#Identity Operators 
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
print(x is y)  #x и y → разные объекты, даже если содержимое одинаковое поэтому False 
print(x == y)  #сравнение содержимого


x = ["apple", "banana"]
y = ["apple", "banana"]

print(x is not y)


x = [1, 2, 3]
y = [1, 2, 3]

print(x == y)
print(x is y)
#My examples
x=[1,2,3,4,5] 
y=[1,2,3,4,5] 
z=x 

print(x is z) 
print(x is y) 
print(x==y) 

a=['LY','RL','R'] 
b=['LY','RL','R'] 
c=a
print(a is b)
print(a==b) 
print(a is c ) 
print(c is a ) 
print(a is not b)  

q=[100,200]
b=[100,200] 
if q is not b: 
    print('You right') 
else: 
    "You have a problem" 
#Membership operators 
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)    

fruits = ["apple", "banana", "cherry"]
print("pineapple" not in fruits)

text = "Hello World"

print("H" in text)
print("hello" in text)
print("z" not in text)
#My examples 
TEXT="Hello dear students" 
print("H" in TEXT) 
print("s" in TEXT) 
print("hello" in TEXT) 
print("Messi" not in TEXT) 

teams=["Barcelona", "Real Madrid", "Manchester United"] 
print("Barcelona" in teams) 
print('Arsenal' in teams) 

cities=['LA','New York', 'Atlanta'] 
print("Miami" in cities) 
#Bitwise Operators
# Два числа
x = 5   # 0101
y = 3   # 0011

# Побитовые операторы
print("Побитовые операторы:")
print("x & y =", x & y)   # AND 
print("x | y =", x | y)   # OR  
print("x ^ y =", x ^ y)   # XOR 
print("~x =", ~x)         # NOT → -6 (двойное отрицание в Python)

# Сдвиги
print("\nСдвиги:")
print("x << 2 =", x << 2)  # Сдвиг влево → 010100 → 20
print("x >> 2 =", x >> 2)  # Сдвиг вправо → 00101 → 1


print(6 & 3)
print(6 | 3)
print(6 ^ 3)
#Operator Precedence 
print((6 + 3) - (6 + 3)) 
print(100 + 5 * 3)
print(5 + 4 - 7 + 3)
#My examples 
print(45*6+6-99) 
print((50+5)-60) 
print(56+34-67-33+4566) 
print((100-4)+(90+3111)) 
print(55*5/7)
 
