#
#

from csv import DictReader

with open("D:\\my_projects\\pycharms\\python_workspace\\lecture_1\\file_operations\\csv_files\\products.csv") as file:
    csv_reader = DictReader(file)
    for p in csv_reader:
        print(p)

# OrderedDict([('ProductName', 'IPhone 6'), ('Price', '3000'), ('IsPublished', 'False'), ('Category', 'Telefon'), ('Reviews', '4.6')])
# OrderedDict([('ProductName', 'IPhone 8'), ('Price', '4000'), ('IsPublished', 'True'), ('Category', 'Telefon'), ('Reviews', '4.6')])
# OrderedDict([('ProductName', 'IPhone 8 Plus'), ('Price', '5000'), ('IsPublished', 'True'), ('Category', 'Telefon'), ('Reviews', '4.5')])
# OrderedDict([('ProductName', 'IPhone XR'), ('Price', '6000'), ('IsPublished', 'True'), ('Category', 'Telefon'), ('Reviews', '4.7')])
# OrderedDict([('ProductName', 'IPhone 11'), ('Price', '7000'), ('IsPublished', 'True'), ('Category', 'Telefon'), ('Reviews', '4.8')])
# OrderedDict([('ProductName', 'Macbook Pro'), ('Price', '9000'), ('IsPublished', 'True'), ('Category', 'Bilgisayar'), ('Reviews', '4.7')])
# OrderedDict([('ProductName', 'Macbook Air'), ('Price', '7000'), ('IsPublished', 'True'), ('Category', 'Bilgisayar'), ('Reviews', '4.6')])


import pandas as pd
file = open("D:\\my_projects\\pycharms\\python_workspace\\lecture_1\\file_operations\\csv_files\\products.csv")
csv_reader = DictReader(file)

df = pd.DataFrame(csv_reader)
df.head()
#      ProductName Price IsPublished Category Reviews
# 0       IPhone 6  3000       False  Telefon     4.6
# 1       IPhone 8  4000        True  Telefon     4.6
# 2  IPhone 8 Plus  5000        True  Telefon     4.5
# 3      IPhone XR  6000        True  Telefon     4.7
# 4      IPhone 11  7000        True  Telefon     4.8

df.columns
# Index(['ProductName', 'Price', 'IsPublished', 'Category', 'Reviews'], dtype='object')

file.close()