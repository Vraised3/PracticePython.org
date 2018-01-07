import random


def cows_bulls(usr_num, num_rand):
    cow_count = 0
    bull_count = 0
    for a, b in zip(usr_num, num_rand):
        if(a == b):
            cow_count += 1
        elif(a in num_rand):
            bull_count += 1
    print('cow count: ', cow_count, ' bull count: ', bull_count)


num_rand = [i for i in str(random.randint(1000, 9999))]
# print(num_rand)
usr_num = []

while(usr_num != num_rand):
    usr_num = [j for j in input('Give me a number: ')]
    cows_bulls(usr_num, num_rand)
