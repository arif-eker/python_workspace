#
#
class Product:
    # __init__ : like constructor
    def __init__(self, name, price):
        self.product_name = name
        self.product_price = price


product1 = Product("iPhone 12 Mini", 12999)
product2 = Product("iPhone 13 Mini", 14999)
product3 = Product("iPhone 11 Mini", 10999)

print(f"Product Name {product1.product_name} -->> Product Price {product1.product_price}")
# Product Name iPhone 12 Mini -->> Product Price 12999

print(f"Product Name {product2.product_name} -->> Product Price {product2.product_price}")
# Product Name iPhone 13 Mini -->> Product Price 14999

print(f"Product Name {product3.product_name} -->> Product Price {product3.product_price}")
# Product Name iPhone 11 Mini -->> Product Price 10999