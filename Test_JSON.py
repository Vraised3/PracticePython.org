import json

val_dict = {'bot': 2,
            'mid': 1,
            'top': 1}

with open('My_Test_JSON.json', 'w') as wr_json:
    json.dump(val_dict, wr_json)

new_key = input('Add new key to dictionary: ')
new_val = input('Add new val to dictionary key: ')

val_dict[new_key] = new_val

with open('My_test_JSON.json', 'w') as wr_json:
    json.dump(val_dict, wr_json)

with open('My_test_JSON.json', 'r') as rd_json:
    json_rd = json.load(rd_json)

print(json_rd)
