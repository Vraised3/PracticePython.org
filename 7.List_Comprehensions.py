from random import randint
a = [randint(1, 100) for num in range(1, 20)]
print(a)
b = [] # Just so that there is no repetitions, otherwise one line print is enough.
b = [num for num in a if(num % 2 == 0 and num not in b)]
print(b)
