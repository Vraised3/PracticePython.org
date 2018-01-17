import json
from collections import Counter
import calendar

with open('Birthdays.json', 'r') as Bday:
    Bday = json.load(Bday)

group = []

for person in Bday:
    group.append(Bday[person][:2])
    # print(person, Bday[person])

C = Counter(group)

# print(C['03'])
for month in C.keys():
    print(C[month], 'people in ', calendar.month_name[int(month)])
