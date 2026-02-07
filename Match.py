day = 4
match day:
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case 4:
    print("Thursday")
  case 5:
    print("Friday")
  case 6:
    print("Saturday")
  case 7:
    print("Sunday")   



day = 4
match day:
  case 6:
    print("Today is Saturday")
  case 7:
    print("Today is Sunday")
  case _:
    print("Looking forward to the Weekend")    # The value _ will always match, so it is important to place it as the last case 



day = 4
match day:
  case 1 | 2 | 3 | 4 | 5:
    print("Today is a weekday")
  case 6 | 7:
    print("I love weekends!")




month = 5
day = 4
match day:
  case 1 | 2 | 3 | 4 | 5 if month == 4:
    print("A weekday in April")
  case 1 | 2 | 3 | 4 | 5 if month == 5:
    print("A weekday in May")
  case _:
    print("No match")        

#My examples 
day = 2
match day: 
  case 1:
    print("Monday") 
  case 2: 
    print("Tuesday") 
  case 3: 
    print("Wednesday") 
  case 4: 
    print("Thursday") 
  case 5 | 6 | 7: 
    print("Friday and weekends")       

day = 3 
match day: 
  case 2: 
    print("Tuesday") 
  case 4: 
    print("Thursday") 
  case _:
    print("Look forward") 

day = 6

match day:
    case 1 | 2 | 3 | 4 | 5:
        print("Today is a weekday")
    case 6 | 7:
        print("I love weekends!")


day = 4
month = 5

match day:
    case 1 | 2 | 3 | 4 | 5 if month == 4:
        print("A weekday in April")
    case 1 | 2 | 3 | 4 | 5 if month == 5:
        print("A weekday in May")
    case 6 | 7:
        print("Weekend day")
    case _:
        print("No match")

