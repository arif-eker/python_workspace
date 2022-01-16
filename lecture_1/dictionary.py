#
#
#

cities = {"Istanbul": 34,
          "Bursa": 16,
          "Ankara": 6}

print(cities)
# Output:
# {'Istanbul': 34, 'Bursa': 16, 'Ankara': 6}
##################################################################################
print(cities["Istanbul"])
# Output:
# 34

##################################################################################
cities["Rize"] = 53
print(cities)
# Output:
# {'Istanbul': 34, 'Bursa': 16, 'Ankara': 6, 'Rize': 53}

##################################################################################
students = {
    100: {
        "Name": "Süleyman",
        "SchoolNumber": 164,
        "Age": 14
    },
    101: {
        "Name": "Mehmet",
        "SchoolNumber": 187,
        "Age": 14},
    102: {
        "Name": "Kasım",
        "SchoolNumber": 148,
        "Age": 14}
}

print(students)
# Output:
# {100: {'Name': 'Süleyman', 'SchoolNumber': 164, 'Age': 14}, 101: {'Name': 'Mehmet', 'SchoolNumber': 187, 'Age': 14}, 102: {'Name': 'Kasım', 'SchoolNumber': 148, 'Age': 14}}

##################################################################################
print(students[100])
# Output:
# {'Name': 'Süleyman', 'SchoolNumber': 164, 'Age': 14}

##################################################################################
print(students[100]["Name"])
# Output:
# Süleyman

##################################################################################
students[103] = {"Name": "Mustafa", "SchoolNumber": 178, "Age": 14}
print(students[103])
# Output:
# {'Name': 'Mustafa', 'SchoolNumber': 178, 'Age': 14}

##################################################################################
products = {}

for i in range(1, 4):
    products[i] = {"ProductName": i ** i,
                   "ProductPrice": 0.18 * i + i}

print(products)
# Output:
# {1: {'ProductName': 1, 'ProductPrice': 1.18}, 2: {'ProductName': 4, 'ProductPrice': 2.36}, 3: {'ProductName': 27, 'ProductPrice': 3.54}}

##################################################################################
for x in products:
    print(x)
# Output:
# 1
# 2
# 3

##################################################################################
for x in products:
    print(f"""Key :{x}, Values : {products[x]}""")
# Output:
# Key :1, Values : {'ProductName': 1, 'ProductPrice': 1.18}
# Key :2, Values : {'ProductName': 4, 'ProductPrice': 2.36}
# Key :3, Values : {'ProductName': 27, 'ProductPrice': 3.54}

##################################################################################

products.keys()  # dict_keys([1, 2, 3])
products.values()  # dict_values([{'ProductName': 1, 'ProductPrice': 1.18}, {'ProductName': 4, 'ProductPrice': 2.36}, {'ProductName': 27, 'ProductPrice': 3.54}])
products.items()  # dict_items([(1, {'ProductName': 1, 'ProductPrice': 1.18}), (2, {'ProductName': 4, 'ProductPrice': 2.36}), (3, {'ProductName': 27, 'ProductPrice': 3.54})])

##################################################################################
for key, value in products.items():
    print(f"""Key: {key} ---> Value: {value}""")
# Output:
# Key: 1 ---> Value: {'ProductName': 1, 'ProductPrice': 1.18}
# Key: 2 ---> Value: {'ProductName': 4, 'ProductPrice': 2.36}
# Key: 3 ---> Value: {'ProductName': 27, 'ProductPrice': 3.54}

##################################################################################
is_True = 1 in products  # looking key in product dict
is_False = 4 in products

print(is_True)  # Output : True
print(is_False)  # Output : False

print("Istanbul" in cities)  # Output : True
print("Istanbul" not in cities)  # Output : False

##################################################################################

products.pop(1)
products.pop(3)
print(products)
# Output:
# {2: {'ProductName': 4, 'ProductPrice': 2.36}}

# products.popitem()  # delete last item

##################################################################################
products.update({4: {"ProductName": 4 ** 4, "ProductPrice": 0.18 * 4 + 4}})
# Output:
# {2: {'ProductName': 4, 'ProductPrice': 2.36}, 4: {'ProductName': 256, 'ProductPrice': 4.72}}
