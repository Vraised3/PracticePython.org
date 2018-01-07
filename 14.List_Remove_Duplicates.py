import random

##################################### List Way #################################
num = [random.randint(1, 100) for a in range(1, 100)]  # will have duplicates
print('Initiaized list: ', num)
Init_List = num
print('Set of initialized list: ', set(num))  # Removes duplicates, becomes a set

#################################### Iteration way ###############################
Rem_Dupli = []
for a in Init_List:
    if(a not in Rem_Dupli):
        Rem_Dupli.append(a)

print('Iteration Way: ', Rem_Dupli)

##################################### Set Way ###################################
num = random.sample(range(1, 100), 50)  # Does not have duplicates because it is set
print('Initialized set: ', num)
