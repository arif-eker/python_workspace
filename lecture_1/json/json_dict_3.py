#
#
import json

path = "D:\\my_projects\\pycharms\\python_workspace\\lecture_1\\json\\"

data = {
    "arif_eker": {
        "name": "Arif",
        "surname": "Eker"
    },
    "letsee": {
        "name": "Metin",
        "surname": "Kara"
    }
}

with open(path + "users.json", "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=2)

with open(path + "users.json", encoding="utf-8") as file:
    users = json.load(file)

print((users["arif_eker"]["name"]))  # Arif
print((users["arif_eker"]["surname"]))  # Eker

# dict better than list.
# if you want to search any value, you should write key, but if you use list, it's not possible.
