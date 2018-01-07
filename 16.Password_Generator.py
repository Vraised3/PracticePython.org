import random
import string
# print(chr(random.randint(97, 122)))


def Chara(choice):
    if(choice == 1):  # Lower Case
        # Chr = chr(random.randint(97, 122))
        Chr = random.choice(string.ascii_lowercase)
    elif(choice == 2):  # Upper Case
        # Chr = chr(random.randint(65, 90))
        Chr = random.choice(string.ascii_uppercase)
    else:
        # Chr = str(random.randint(1, 10))
        Chr = random.choice(string.digits)
    return Chr


def strength(val):
    word = []
    for a in range(1, val):
        choice = random.choice([1, 2, 3])
        word.append(Chara(choice))
    word = "".join(word)
    return word


Cmplx = input('How complex do you want your password to be, weak, medium or strong: ')
val = {'weak': 5, 'medium': 10, 'strong': 25}
print(strength(val[Cmplx]))
