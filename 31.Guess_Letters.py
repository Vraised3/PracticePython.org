import random

with open('sowpods.txt', 'r') as sowpods:
    text = sowpods.read()

words = text.split()

hangman = random.choice(words).strip()
hang_len = len(hangman)

print('I\'m guessing a word ')
blank = ['_' for parse in range(hang_len)]
print(blank)
guess_scratch = []
x = 0

print('You have 6 guesses of the letters and then you have to guess the word ')
while(x < 6):
    guess = input('Guess ' + str(x + 1) + ': ').upper()
    if(guess not in guess_scratch):
        guess_scratch.append(guess)
    else:
        print('Letter already used, guess again ')
        continue

    if(guess in hangman):
        for let in range(hang_len):
            if(guess == hangman[let]):
                blank[let] = guess
    else:
        print('You have ' + str(6 - (x + 1)) + ' more guesses ')

    print(blank)

    if(blank == hangman):
        print('You guessed right')
        print(hangman)
        exit(0)

    x = x + 1

guess_word = input('So what is the word: ')
if(guess_word == hangman):
    print('You are right ')
    print(hangman)
else:
    print('You guessed wrong ')
    print('The right word is ' + hangman)
