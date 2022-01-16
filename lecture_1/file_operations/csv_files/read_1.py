#
#
import csv

with open("D:\\my_projects\\pycharms\\python_workspace\\lecture_1\\file_operations\\csv_files\\products.csv") as file:
    csv_reader = csv.reader(file)
    for p in csv_reader:
        print(p)


# ['ProductName', 'Price', 'IsPublished', 'Category', 'Reviews']
# ['IPhone 6', '3000', 'False', 'Telefon', '4.6']
# ['IPhone 8', '4000', 'True', 'Telefon', '4.6']
# ['IPhone 8 Plus', '5000', 'True', 'Telefon', '4.5']
# ['IPhone XR', '6000', 'True', 'Telefon', '4.7']
# ['IPhone 11', '7000', 'True', 'Telefon', '4.8']
# ['Macbook Pro', '9000', 'True', 'Bilgisayar', '4.7']
# ['Macbook Air', '7000', 'True', 'Bilgisayar', '4.6']
