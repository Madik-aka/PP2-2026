print(10 + 5)

sum1 = 100 + 50      # 150 (100 + 50)
sum2 = sum1 + 250    # 400 (150 + 250)
sum3 = sum2 + sum2 
print(sum3) 

sum1=65-20 
sum2=sum1-35
sum3=sum2+2+sum1 
print(sum3) 
#Arithmetic Operators
x = 15
y = 4

print(x + y)
print(x - y)
print(x * y)
print(x / y) # returns float
print(x % y) #покахывает остаток 
print(x ** y) #возводит в степень
print(x // y) #отбрасывает дробную часть, оставляя целое число. returns int

x = 12
y = 5
print(x / y) 

x = 12
y = 5
print(x // y)
#My examples 
x=100
z=3 

print(x+z) 
print(x-z) 
print(x*z) 
print(x/z) 
print(x%z) 
print(x//z) 
print(x**z) 

x=33
y=5
print(x/y) 

x=33
y=5
print(x//y) 

b=100
c=2
print(b/c) 

b=100
c=2
print(100//2) 
#Assignment operators
x = 5        # просто присвоение
x += 3       # x = x + 3
x = 5
x -= 3       # x = x - 3
x = 5
x *= 3       # x = x * 3
x = 5
x //= 3      # x = x // 3  (целочисленное деление)
x = 5
x %= 3       # x = x % 3   (остаток от деления)
x = 5
x **= 3      # x = x ** 3  (возведение в степень)
x = 5
x &= 3       # x = x & 3   (побитовое И)
x = 5
x |= 3       # x = x | 3   (побитовое ИЛИ)
x = 5
x ^= 3       # x = x ^ 3   (побитовое XOR)
x = 5
x >>= 1      # x = x >> 1  (сдвиг вправо на 1 бит)
x = 5
x <<= 1      # x = x << 1  (сдвиг влево на 1 бит)
print(x := 3)	

x = 3
print(x) 
#My examples
x=5
x+=5
x-=3
x*=7
x/=3
x//=2


numbers = [1, 2, 3, 4, 5]

if (count := len(numbers)) > 3:
    print(f"List has {count} elements") 
# Считай одно и тоже
count = len(numbers)
if count > 3:
    print(f"List has {count} elements") 


numbers=[5,7,8,9,10,11] 
if(count:=len(numbers))>=6: 
    print(f"All is good and lists have {count} elements") 

x=[1,2,3,4,5] 
if(count:=len(x))>10: 
    print(f'Lists have {count} elements') 
else: 
    print("Nah")         

x=[1,2,3,4,5] 
count=len(x)  
if count>10: 
    print(f"Lists have {count} elements") 
else: 
    print("Nah") 

#Comparison Operators 
x = 5
y = 3

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

x = 5
print(1 < x < 10)

print(1 < x and x < 10) # в and должно работать 2 условие, в or хотя бы одно из них 
#My examples 
x=70
y=80 
print(x<y)
print(x>y) 
print(x>=y)
print(x<=y) 
print(x!=y) 
print(x==y) 

x=10 
print(6.9<x<20) 

print(9.9<x and x>5) 

y=36
print(35<y>37)
print(40<y or y>2) 