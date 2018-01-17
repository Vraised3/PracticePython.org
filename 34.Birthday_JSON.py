import json

bir_dict = {"Albert Einstein": "03/17/1879",
            "Benjamin Franklin": "01/17/1706",
            "George Washington": "03/22/1732",
            "Abraham Lincoln": "03/12/1809"}

with open('BDay.json', 'w') as BDay:
    json.dump(bir_dict, BDay)

# update "BDay.json":
with open("BDay.json", 'r') as f:
    s = json.load(f)

name = input('Enter the name to be added to the dictionary ')
bday = input('Enter their Birthday in the format dd/mm/yyyy ')
s[name] = bday

with open('BDay.json', 'w') as f:
    json.dump(s, f)
