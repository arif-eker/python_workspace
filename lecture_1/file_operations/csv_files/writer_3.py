#
#

import csv

path = "D:\\my_projects\\pycharms\\python_workspace\\lecture_1\\file_operations\\csv_files\\"

with open(path + "person.csv", "w", newline="") as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(["Name", "Surname"])

with open(path + "person.csv", "a", newline="") as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(["Arif", "Eker"])

# add line with "," ---> 'Arif','Eker'

with open(path + "person.csv", "a", newline="") as file:
    csv_writer = csv.writer(file, delimiter=";")
    csv_writer.writerow(["Arif", "Eker"])

# add line with ";" ---> 'Arif','Eker'


# if you dont use newline="" or newline="\n"
# writerows writes 3 rows, not 1