import random
with open('sowpods.txt', 'r') as sowpods:
    text = sowpods.read()
text = text.split()
num_wrds = len(text)

# print(text)
# print(text[random.randint(0, num_wrds)])
print(random.choice(text).strip())
