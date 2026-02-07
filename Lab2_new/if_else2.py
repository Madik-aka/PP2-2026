a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")  

a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")


a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")
#My examples 
x=40
y=69 
if y%2==0 or x%2==0: 
  print("Yes") 

x=100
y=1000 
if x%10==0 and y%10==0: 
  print("Yes") 

a=2
b=1 
if not b>1: 
  print("It's not correct")     


age = 25
is_student = False
has_discount_code = True
if (age < 18 or age > 65) and not is_student or has_discount_code:   #False or False=False; False and True=False; False or True=True
  print("Discount applies!") 


temperature = 25
is_raining = False
is_weekend = True

if (temperature > 20 and not is_raining) or is_weekend:
  print("Great day for outdoor activities!")


username = "Tobias"
password = "secret123"
is_verified = True
if username and password and is_verified:
  print("Login successful")
else:
  print("Login failed")  


score = 85
if score >= 0 and score <= 100:
  print("Valid score")
else:
  print("Invalid score")
#My examples 
x=100 
y=200
c=20
if (x<y and  not c>x) or c: 
  print(1)
else: 
  print(0) 

uni="KBTU" 
id="25B03" 
subject={} 
if (uni and id and subject) or not subject: 
  print("Welcome to your new home") 
#Nested If 
x = 41
if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")


age = 25
has_license = True
if age >= 18:
  if has_license:
    print("You can drive")
  else:
    print("You need a license")
else:
  print("You are too young to drive") 


score = 85
attendance = 90
submitted = True
if score >= 60:
  if attendance >= 80:
    if submitted:
      print("Pass with good standing")
    else:
      print("Pass but missing assignment")
  else:
    print("Pass but low attendance")
else:
  print("Fail")  


username = "Emil"
password = "python123"
is_active = True

if username:
  if password:
    if is_active:
      print("Login successful")
    else:
      print("Account is not active")
  else:
    print("Password required")
else:
  print("Username required")


score = int(input("Введите число: "))
attendance = int(input())

if score == 100 and attendance == 70:
    print("A")
elif score == 90 and attendance == 70:
    print("A-")
else:
    print("B+ and low")
#Pass Statement 
a = 33
b = 200
if b > a:
  pass #ничего не делает. Он просто проверяет условие и не выполняет никаких действий, потому что pass — заглушка.

age = 16

if age < 18:
  pass #  Add underage logic later
else:
  print("Access granted")  


score = 85
if score > 90:
  pass # This is excellent
print("Score processed")


value = 50
if value < 0:
  print("Negative value")
elif value == 0:
  pass # Zero case - no action needed
else:
  print("Positive value") 


x=30 
if x<0: 
  print("-") 
elif x==0: 
  pass 
else: 
  print(1)      