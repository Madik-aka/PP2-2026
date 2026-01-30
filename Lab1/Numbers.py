x = 1    # int
y = 2.8  # float
z = 1j   # complex 

print(type(x))
print(type(y))
print(type(z))
#My examples
x=567
y=8.9
z=7j 
print(type(x)); print(type(y)); print(type(z)) 

x=5 
y=99595595
z=1000 
print(type(x)) 
print(type(y)) 
print(type(z))  



x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z)) 



q=66/9
print(type(q))
print(q)
z=0.44444
print(type(z)) 


x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))


x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))


x = 35e3
y = 12E4         #Float can also be scientific numbers with an "e" to indicate the power of 10.  *10^ e=E
y = 12E4
z = -87.7e100
print(x) 
print(type(x))
print(type(y))
print(type(z)) 
#My example
x=56e4 
y=777E10
z=567e3
print(type(x)) 
print(type(y)) 
print(y) 
print(type(z))  


x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)        #You cannot convert complex numbers into another number type.
print(c)

print(type(a))
print(type(b))
print(type(c))  
#My example 
x=78
y=89.6
z=8+9j 

a=float(x) 
b=int(y) 
c=complex(y) 

print(a) 
print(b) 
print(c) 

print(type(a))
print(type(b)) 
print(type(c)) 




import random

print(random.randrange(1, 10))

#My examples
import random 
print(random.randrange(1,100)) 

import random 
print(random.randrange(45,77)) 

import random 
a=100
b=300
print(random.randrange(a,b)) 

import random
print(random.randrange(5,677777777))