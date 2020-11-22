'''

Program goal is to write a data, dump it as a JSON then export it as a JSON file

'''

print("Do something")

print("Input the list separated by colon, the things you want to export")

list_input = input().split(",")

list_processed = dict()

for entry in list_input:
    y = entry.split(":")
    list_processed[y[0]] = y[1]

print (list_processed)
