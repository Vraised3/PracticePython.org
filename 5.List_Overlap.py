from random import randint
a = [randint(1, 100) for i in range(1, 50)]
print('a = ' + str(a))
b = [randint(1, 100) for i in range(1, 50)]
print('b = ' + str(b), '\n')
c = []
for i in a:
    for j in b:
        if(i == j and i not in c):
            c.append(i)

print('c = ' + str(c))
