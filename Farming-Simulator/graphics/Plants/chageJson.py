import json

# 1. Load the JSON file
file_path = "plants.json"  # Path to your JSON file
with open(file_path, "r") as file:
    data = json.load(file)  # Load JSON into a Python object (dict or list)
data["plants"] = {}
data["plants"]["path"] = data["crops"]["path"]
data["plants"]["size"] = data["crops"]["imageSize"]
data["plants"]["data"] = {}
k = 0
for i in range(2):
    for j in range(26):
        if not data["crops"]["frames"][i][j] == 0:
            k += 1
            data["plants"]["data"][f"{k}"] = {}
            data["plants"]["data"][f"{k}"]["pos"] = [i * 128, j * 32]
            data["plants"]["data"][f"{k}"]["frame"] = data["crops"]["frames"][i][j]

# 3. Write the changes back to the JSON file
with open(file_path, "w") as file:
    json.dump(data, file, indent=4)  # Save with indentation for readability

print("JSON file updated successfully!")
