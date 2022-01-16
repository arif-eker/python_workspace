#
#

# Serialize
import json

path = "D:\\my_projects\\pycharms\\python_workspace\\lecture_1\\json\\"

my_val = {"name": "Selim", "surname": "Öner", "age": 32}

# convert dict to json string
new_person = json.dumps(my_val, ensure_ascii=False,
                        indent=2)  # use Ascii for Turkish characters

# if you try to use file.write(). it raise error becaouse write method need str type not dict type
# you can convert dict to json string then you can use file.write() ----> file.write(new_person)
# or try to json.dump(my_val, file) for write dict to file ---> my_val is dict type value

# write example
with open(path + "person2.json", "w", encoding="utf-8") as file:
    file.write(new_person)

with open(path + "person2.json") as file:
    write_json_data = json.load(file)
print(write_json_data["name"])  # Selim
print(write_json_data["age"])  # 32

#

# dump example:
with open(path + "person3.json", "w", encoding="utf-8") as file:
    json.dump(my_val, file, ensure_ascii=False, indent=2)

with open(path + "person3.json") as file:
    json_data = json.load(file)

print(json_data["name"])  # Selim
print(json_data["age"])  # 32
