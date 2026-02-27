import datetime # подключаем модуль datetime()
x = datetime.datetime.now()
print(x)


import datetime
x = datetime.datetime.now()
print(x.year)
print(x.strftime("%A")) #name of weekday


import datetime
x = datetime.datetime(2020, 5, 17) #year,month and day
print(x)


import datetime
x = datetime.datetime(2018, 6, 1)
print(x.strftime("%B"))

""" 
| Директива | Что делает                           | Пример                   |
| --------- | ------------------------------------ | ------------------------ |
| `%a`      | День недели коротко                  | Wed                      |
| `%A`      | День недели полностью                | Wednesday                |
| `%b`      | Месяц коротко                        | Jun                      |
| `%B`      | Месяц полностью                      | June                     |
| `%m`      | Месяц цифрой                         | 06                       |
| `%Y`      | Год полный                           | 2018                     |
| `%c`      | Локальная дата и время               | Mon Dec 31 17:41:00 2018 |
| `%X`      | Время локально (часы:минуты:секунды) | 17:41:00                 |

"""
#My examples 
import datetime 
a=datetime.datetime
print(a.now())
import datetime 
x=datetime.datetime.now() 
print(x) 


import datetime 
x=datetime.datetime.now() 
print(x.year) 
print(x.month); print(x.day) 
print(x.strftime("%X")) 

import datetime 
i=datetime.datetime.now() 
print(x.strftime("%A")); print(x.strftime("%a"))


import datetime 
y=datetime.datetime.now() 
print(x.strftime("%c")); print(x.strftime("%b"))
#Dates exercise 
#1 
from datetime import datetime, timedelta

today = datetime.now()
new_date = today - timedelta(days=5)

print("Today:", today)
print("5 days ago:", new_date)

#2 
from datetime import datetime, timedelta
today = datetime.now()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)
print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow) 

#3 
from datetime import datetime
now = datetime.now()
without_microseconds = now.replace(microsecond=0)
print("Original:", now)
print("Without microseconds:", without_microseconds)

#4 
from datetime import datetime
date1 = datetime(2025, 1, 1)
date2 = datetime(2025, 1, 10)
difference = date2 - date1
seconds = difference.total_seconds()
print("Difference in seconds:", seconds)