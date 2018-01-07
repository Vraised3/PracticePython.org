a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
list_less_than5 = []
num = int(input('Hey give me a number: '))
for var in a:
    if(var < num):
        list_less_than5.append(var)

print(list_less_than5)
print([val for val in a if val < num]) # List Comprehensions - i.e. {x² : x in {0 ... 9}} Like mathematics
