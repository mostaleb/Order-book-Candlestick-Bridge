# Opening JSON file
f = open('static/TSXData.json')

# returns JSON object as
# a dictionary
data = json.load(f)

# Iterating through the json
# list
arr  = []
for i in data:
    print(i["MessageType"])
    if i["MessageType"] not in arr:
        arr.append(i["MessageType"])
print(arr)

# Closing file
f.close()