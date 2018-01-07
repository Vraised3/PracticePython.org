    import random


def start(gcount):
    print('Guess count: ', gcount)
    guess = int(input('Guess the number I\'m thinking between 1-9: '))
    if(guess == realval):
        print('You guessed exactly right, heres a cookie.')
        gcount += 1
    elif(guess < realval):
        print('You guessed too low. Try again')
        gcount += 1
        start(gcount)
    else:
        print('You guessed too high. Try again')
        gcount += 1
        start(gcount)


def quit():
    q = int(input('Do you want to quit(0) or play again(1)? '))
    if(q < 1):
        exit(0)
    print('You can do this')


while(1):
    realval = random.randint(1, 9)  # Scope throughout functions
    gcount = 0
    start(gcount)
    quit()
