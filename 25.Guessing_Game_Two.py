print('Think of a number between 1 - 100, and don\'t tell me. ')
FN = 0
LN = 100
count = 0
while(1):
    count += 1
    guess = int((LN - FN) / 2)
    YN = input('Is it ' + str(guess) + ' yes(1) or no(0) ')
    if(YN in ['1', 'yes', 'YES', 'Yes']):
        print('I see. I guessed right. ')
        break
    elif(YN in ['0', 'no', 'NO', 'No']):
        HL = input('Too high(1) or too low(0) ')
        if(HL in ['0', 'low', 'LOW', 'Low']):
            FN = int((FN - guess) / 2)
        else:
            LN = int((LN + guess) / 2)

print('Took me ' + str(count) + ' guesses')
