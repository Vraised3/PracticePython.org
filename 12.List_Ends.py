import random


def firstlast(a):
    print('First = ', a[0])
    print('Last = ', a[-1])


a = random.sample(range(1, 100), random.randint(1, 50))
print('a = ', a)
firstlast(a)
