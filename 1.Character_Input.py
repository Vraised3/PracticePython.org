import datetime
name = input('Hey what\'s your name ')
age = input('Oh hey ' + name + ' how old are you ')
age100 = (100 - 23 + int(datetime.date.today().year))
print('So you\'ll be 100 in ' + str(age100))
print('So you\'re ' + name + ' and you are ' + age + ' years old')
num = int(input('Hey ' + name + ' give me a number: '))
print(num * ('So you\'re ' + name + ' and you are ' + age + ' years old\n'))
