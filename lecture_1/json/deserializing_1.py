#
#

# Deserialize
import json

path = "D:\\my_projects\\pycharms\\python_workspace\\lecture_1\\json\\"

with open(path + "person.json") as file:
    json_data = json.load(file)

print(json_data["name"])  # "Arif"
print(json_data["age"])  # 24

data = """ { "name": "Arif", "surname": "Eker", "age": 24 } """
val = json.loads(data)
print(val["surname"])  # Eker
