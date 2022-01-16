#
#
#
import csv

path = "D:\\my_projects\\pycharms\\python_workspace\\lecture_1\\file_operations\\csv_files\\"
headers = ["Name", "Surname", "Age"]

with open(path + "person_dict.csv", "w", newline="") as file:
    csv_writer = csv.DictWriter(file, headers)
    csv_writer.writeheader()

# Use newline argument!
with open(path + "person_dict.csv", "a", newline="") as file:
    csv_writer = csv.DictWriter(file, headers)
    csv_writer.writerow({"Name": "Arif",
                         "Surname": "Eker",
                         "Age": 24})

with open(path + "person_dict.csv", "a", newline="", encoding="utf-8") as file:
    csv_writer = csv.DictWriter(file, headers)
    csv_writer.writerows([{"Name": "Mehmet", "Surname": "Keskin", "Age": 33},
                          {"Name": "Mustafa", "Surname": "Yılmaz", "Age": 22}])

#
with open(path + "person_dict.csv", "r", newline="") as file:
    csv_reader = csv.DictReader(file)
    for p in csv_reader:
        print(p)
        print(p["Name"])

# OrderedDict([('Name', 'Arif'), ('Surname', 'Eker'), ('Age', '24')])
# Arif
# OrderedDict([('Name', 'Mehmet'), ('Surname', 'Keskin'), ('Age', '33')])
# Mehmet
# OrderedDict([('Name', 'Mustafa'), ('Surname', 'YÄ±lmaz'), ('Age', '22')])
# Mustafa
