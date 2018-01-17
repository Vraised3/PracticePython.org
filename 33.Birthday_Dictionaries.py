birthdays = {"Albert Einstein": "03/17/1879",
             "Benjamin Franklin": "01/17/1706",
             "George Washington": "03/22/1732",
             "Abraham Lincoln": "03/12/1809"}

print('These are the peoples whose birthday we have')
print(birthdays.keys())
ind = input('Whose birthday do you want: ')
print(birthdays.get(ind, 'Sorry, don\'t have that name'))
