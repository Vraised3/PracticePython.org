
with open('Training_01.txt', 'r') as open_file:
    all_text = open_file.read()

all_split = all_text.split()

Dict_FD = {}
Dict_SD = {}
Count_FD = 0
Count_SD = 0
len_allsp = len(all_split)
for i in range(0, len_allsp):
    FD = all_split[i][1]
    SD = all_split[i][3:all_split[i].find('/sun')]
    if(FD in Dict_FD):
        Count_FD += 1
    else:
        Count_FD = 1 # Count cannot start at 0 if not in dictionaary
    if(SD in Dict_SD):
        Count_SD += 1
    else:
        Count_SD = 1
    Dict_FD[FD] = Count_FD  # Dictionary first directory
    Dict_SD[SD] = Count_SD

print(Dict_FD)
print(Dict_SD)

# with open('Split_file.txt', 'w') as open_file:
#     open_file.write(all_text)
