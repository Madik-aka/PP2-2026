#1 
import re
s = input()
if re.fullmatch(r'ab*', s):
    print("Match")
else:
    print("No match")


#2 
import re
s = input()
if re.fullmatch(r'ab{2,3}', s):
    print("Match")
else:
    print("No match")


      
#3
import re
s = input()
matches = re.findall(r'[a-z]+_[a-z]+', s)
print(matches)




#4
import re
s = input()
matches = re.findall(r'[A-Z][a-z]+', s)
print(matches)



#5
import re
s = input()
if re.fullmatch(r'a.*b', s):
    print("Match")
else:
    print("No match")



#6
import re
s = input()  # example: "snake_case_string"
parts = s.split('_')
camel = parts[0] + ''.join(word.capitalize() for word in parts[1:])
print(camel)



#7
import re
s = input()  # example: "snake_case_string"
parts = s.split('_')
camel = parts[0] + ''.join(word.capitalize() for word in parts[1:])
print(camel)



#8
import re
s = input()  # example: "CamelCaseString"
parts = re.split(r'(?=[A-Z])', s)
print(parts)



#9
import re
s = input()  # example: "HelloWorld"
result = re.sub(r'([A-Z])', r' \1', s).strip()
print(result)



#10    
import re
s = input()  # example: "CamelCaseString"
snake = re.sub(r'([A-Z])', r'_\1', s).lower().lstrip('_')
print(snake)