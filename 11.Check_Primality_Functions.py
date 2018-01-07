num = int(input('Give me a number: '))

if(num in [1, 2, 3]):
    print('Number is Prime')
    exit(0)
elif(num % 2 == 0):
    print('Number is not Prime')
    exit(0)
else:
    div = 3
    while(div < num / 2):
        if(num % div == 0):
            print('Number is not Prime')
            exit(0)
        div += 2
    print('Number is Prime')
