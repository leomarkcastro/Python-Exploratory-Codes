import json

x = {
    'name': 'leo',
    'score': 36,
    'level': (1,6,5)
}

if True:
    with open("Save.json", "w+") as write_file:
        json.dump(x, write_file)

if True:
    with open("Save.json", "r") as read_file:
        data = json.load(read_file)

    print (data)
