import json

file_path_crops = "Crops.json" 
file_path_objects = "Objects.json" 
file_path_plant_stardew = "plants_stardew.json"
file_path_harvest = "harvest_plant.json"
final_path = "Plant_Stardew.json"

with open(file_path_crops, "r") as file:
    crops = json.load(file)

with open(file_path_objects, "r") as file:
    objects = json.load(file)  

with open(final_path, "r") as file:
    data = json.load(file)
# data = {}
# data["Items_image"] = {
#     "path": "../graphics/Plants/Image/springobjects.png",
#     "size": [384, 624],
#     "sprite_size": [16, 16],
# }

# data["Crops_Image"] = {
#     "path": "../graphics/Plants/Image/crops.png",
#     "size": [256, 1024],
#     "sprite_size": [16, 32],
#     "type": 2
# }
# data["Crops"] = {}
# data["Harvest"] = {}
# for crop_name, crop_data in crops.items():
#     harvest = crop_data["HarvestItemId"]
#     if crop_name in objects:
#         data["Crops"][crop_name] = {
#             "SpriteIndex_Crop": crop_data["SpriteIndex"],
#             "SpriteIndex_Seed": objects[crop_name]["SpriteIndex"],
#             "Name": objects[crop_name]["Name"],
#             "Price": objects[crop_name]["Price"],
#             "HarvestItemId": crop_data["HarvestItemId"],
#             "Seasons": crop_data["Seasons"],
#             "DaysInPhase": crop_data["DaysInPhase"],
#             "Frames": len(crop_data["DaysInPhase"]) + 2,
#             "RegrowDays": crop_data["RegrowDays"],
#             "TintColors": crop_data["TintColors"]
#             }
        
#         if crop_data["RegrowDays"] > 0:
#             data["Crops"][crop_name]["Frames"] += 1
#         if len(crop_data["TintColors"]) > 0:
#             data["Crops"][crop_name]["Frames"] += 1

#     if harvest in objects:
#         data["Harvest"][harvest] = {
#             "Name":objects[harvest]["Name"],
#             "Price":objects[harvest]["Price"]
#         }

for typeData, datas in data["Crops"].items():
    datas["HarvestName"] = data["Harvest"][datas["HarvestItemId"]]["Name"]

with open(final_path, "w") as file:
    json.dump(data, file, indent=4)

print("JSON file updated successfully!")
