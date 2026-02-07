b = "Hello, World!"
print(b[2:5])   #get the characters from position 2 to position 5, which is not included
#My example 
x='I like swimming' 
print(x[0:7]) 

c='0123456'
print(c[4:6])    #4 учитываеться а 6 нет

b = "Hello, World!"
print(b[:5])  #By leaving out the start index, the range will start at the first character:
#My example 
c='Astana' 
print(c[:4]) 

b = "Hello, World!"
print(b[2:])   # тоже самое только наоборот 
#My example 
v='993344556677'
print(v[7:]) 
f='Harvard' 
print(f[1:]) 

b = "Hello, World!"
print(b[-5:-2])    #-5 учитываеться а -2 индексы не учитываються 
#My example 
x='All eyez on me?' 
print(x[-4:-1]) 

y='almaty' 
print(y[-4:-1]) 


a = "Hello, World!"
print(a.upper())
#My example 
x='Bukayo Saka'
print(x.upper()) 

y='jfbsdkfj'
print(y.upper()) 


a = "Hello, World!"
print(a.lower())
#My example 
x='Orange' 
print(x.lower()) 

l="KANTE"
print(l.lower()) 

a = " Hello, World! "
print(a.strip()) # returns "Hello, World1!" Удаляет пробелы до и после текста 
#My example 
v='        I love listen to music           ' 
print(v.strip()) 


a = "Hello, World!"
print(a.replace("H","J")) 
#My example 
c="1234567" 
print(c.replace("1", "7")) 


a = "Hello, World!"
print(a.split(",")) # split-расщеплять, делит на два независимых 
#My example 
z='I like you too'
print(z.split(" "))
u='Mbappe, no'
print(u.split(","))


a = "Hello"
b = "World"
c = a + b
print(c) 

a = "Hello"
b = "World"
c = a + " " + b
print(c)
#My example 
x='Capital'
y='Astana' 
print(x + " " + y) 


age = '37' # если убрать кавычки то выйдет ошибка 
#This will produce an error:
txt = "My name is John, I am " + age
print(txt) 

age = 36
txt = f"My name is John, I am {age}"
print(txt)
#My example
x=50
print(f"In this year my dad will be {x} years old")

c=90
x=f"I like {c}'s years say Julieta"
print(x) 


price = 59
txt = f"The price is {price} dollars"
print(txt) 

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)
#My example
value=100
x=f"This bottle worth {value:.2f} dollars" 
print(x) 

a=5
b=f"Barcelona won {a:.1f} champlins league titles"
print(b) 

txt = f"The price is {20 * 59} dollars"
print(txt)
#My example
x=f"Arsenal won {1*0} uecl "
print(x) 


txt = "We are the so-called \"Vikings\" from the north."
print(txt) 
#My example 
x="The Black Panther is so \"Cool\" for my opinion."
print(x) 
x="Idk what are \"you\" say"
print(x) 

x='We\nare' 
print(x) 
m='i\nlive\nin\nnew\nyork' 
print(m) 

