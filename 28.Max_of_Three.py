print('Gimme 3 numbers')
x = [int(input()) for i in range(3)]
a = x[0]
for i in range(3):
    if(x[i] > a):
        a = x[i]
print(str(a) + ' is the biggest. ')
