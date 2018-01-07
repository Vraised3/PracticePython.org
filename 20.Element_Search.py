import random


def bin_search(lst, val):
    begin = 1
    end = len(lst)
    step = 0
    for a in range(begin, end):
        if(val == lst[a]):
            print('Index val: ', a)
            print('Step count: ', step)
            exit()
        if(val >= lst[int(end / 2)]):
            begin = int(end / 2)
        else:
            end = int(end / 2)
        step += 1
    print('No Value')


num = random.randint(1, 100)
print('num = ', num)
lst = sorted(random.sample(range(1, 100), 50))
print(lst)
# print(num in lst)
# print('Index tru: ', lst.index(num))

bin_search(lst, num)
