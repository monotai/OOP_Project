import json

# 1. Load the JSON file
file_path = "hoeDirt.json"  # Path to your JSON file
with open(file_path, "r") as file:
    data = json.load(file)  # Load JSON into a Python object (dict or list)

size = data["size"][0]

data["dirts"] = {}
data["dirts"]["small"] = [0, 0]

data["dirts"]["updown"] = {}
updown = data["updown"]

for i in range(updown[3]):
    data["dirts"]["updown"][f"{i}"] = [updown[0], updown[1] + size * i]

data["dirts"]["leftright"] = {}
leftright = data["leftright"]

for i in range(leftright[2]):
    data["dirts"]["leftright"][f"{i}"] = [leftright[0] + size * i, leftright[1]]

data["dirts"]["big"] = {}
big = data["big"]

for i in range(big[2]):
    for j in range(big[3]):
        data["dirts"]["big"][f"{i*big[3] + j}"] = [big[0] + size * i, big[1] + size * j]

# 3. Write the changes back to the JSON file
with open(file_path, "w") as file:
    json.dump(data, file, indent=4)  # Save with indentation for readability

print("JSON file updated successfully!")
