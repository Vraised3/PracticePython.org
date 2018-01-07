x = int(input('Enter a Number: '))
print([num for num in range(2, int(x / 2)) if x % num == 0])
