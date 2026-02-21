x = lambda a : a + 10
print(x(5))

x = lambda a, b : a * b
print(x(5, 6))

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))


def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)


students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)
#My examples 
people = [("Ali", 20), ("Dana", 18), ("Maksat", 22)]

sorted_people = sorted(people, key=lambda x: x[1])

print(sorted_people)


words = ["apple", "kiwi", "banana", "pear"]

sorted_words = sorted(words, key=lambda x: len(x))

print(sorted_words)



numbers = [1, 2, 3, 4, 5, 6]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(even_numbers)



words = ["cat", "tiger", "dog", "elephant"]

long_words = list(filter(lambda x: len(x) > 4, words))

print(long_words)



square = lambda x: x ** 2

print(square(5))
