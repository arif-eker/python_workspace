#
#
# topic numbers = [1, 2]
# CTRL + F and enter --topic number-- for jump topic to topic
# for example "--5--"

#########################################################################################################################################################
# Topic: --1--

person = {"name": "Arif",
          "surname": "Eker"}

print(person)  # {'name': 'Arif', 'surname': 'Eker'}

del person["surname"]
print(person)  # {'name': 'Arif'}

student = {"name": "Mustafa",
           "surname": "Keskin",
           "math": [45, 55, 65]}

print(student)  # {'name': 'Mustafa', 'surname': 'Keskin', 'math': [45, 55, 65]}

lesson = {"math": [75, 85, 90],
          "english": [87, 92, 85]}

student.update(lesson)
print(student)  # {'name': 'Mustafa', 'surname': 'Keskin', 'math': [75, 85, 90], 'english': [87, 92, 85]}

student.update(location="Istanbul")
print(
    student)  # {'name': 'Mustafa', 'surname': 'Keskin', 'math': [75, 85, 90], 'english': [87, 92, 85], 'location': 'Istanbul'}

#########################################################################################################################################################
# Topic: --2--

product = {"name": "IPhone 13",
           "price": 14599,
           "company": "Apple"}

print(product.keys())  # dict_keys(['name', 'price', 'company'])

print(product.values())  # dict_values(['IPhone 13', 14599, 'Apple'])

print(product.items())  # dict_items([('name', 'IPhone 13'), ('price', 14599), ('company', 'Apple')])

for key, value in product.items():
    print(f"Key: {key} >>> Value: {value}")

# Key: name >>> Value: IPhone 13
# Key: price >>> Value: 14599
# Key: company >>> Value: Apple
