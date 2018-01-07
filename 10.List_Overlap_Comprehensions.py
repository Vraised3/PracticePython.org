import random
a_size = random.randint(1, 40)
b_size = random.randint(1, 40)

# a = random.sample(range(100), random.randint(1, 100))  ## Does not duplicate
# b = random.sample(range(100), random.randint(1, 100))

############################################## LIST WAY ################################################
a = [random.randint(1, 100) for num in range(1, a_size)] ## Does duplicate
b = [random.randint(1, 100) for num in range(1, b_size)]

print('a = ', a)
print('b = ', b)

common = []

# for val in a:
#     if(val in [val1 for val1 in b]):
#         common.append(val)
common = [val for val in a for val1 in b if(val == val1 and val not in common)]  # Code in 1 line

print('List way: ', common)
print('size of a', len(a), '\n')

################################################ SET WAY ###############################################
a = set(a)  # Convert list a into set a
b = set(b)

print('a = ', a)
print('b = ', b)

common = a & b
print('Set way: ', common)

print('size of a', len(a))
