#
#
#
import json

path = "D:\\my_projects\\pycharms\\python_workspace\\lecture_1\\json\\"


class Product:
    def __init__(self, name, category, price):
        self.name = name
        self.category = category
        self.price = price


prod1 = Product("IPhone 13 Pro Max", "Phone", 1200)
prod2 = Product("Xiaomi ", "Phone", 450)
prod3 = Product("Samsung Oled TV", "TV", 2700)

print(prod1.__dict__)  # {'name': 'IPhone 13 Pro Max', 'category': 'Phone', 'price': 1200}

products = {
    1: prod1.__dict__,
    2: prod2.__dict__,
    3: prod3.__dict__
}

with open(path + "products.json", "w", encoding="utf-8") as file:
    json.dump(products, file, ensure_ascii=False, indent=2)

with open(path + "products.json", encoding="utf-8") as file:
    prods = json.load(file)

print(prods["1"])
# {'name': 'IPhone 13 Pro Max', 'category': 'Phone', 'price': 1200}
