num1 = input('Hey give me two numbers: ')
num2 = input()
if(int(num1) % int(num2) == 0):
    print(num2 + ' divides ' + num1 + ' evenly')
else:
    if(int(num1) % 4 == 0):
        print(num1 + ' is a multiple of 4')
    else:
        if(int(num1) % 2 == 0):
            print(num1 + ' is an even number')
        else:
            print(num1 + ' is an odd number')
