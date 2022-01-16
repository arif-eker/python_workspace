#
#

class Product:
    def __init__(self, name, price):
        self.name = name
        if price < 0:
            raise ValueError("Price must be bigger zero")
        else:
            self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price must be bigger zero")
        else:
            self._price = value


product_1 = Product("iPhone 12", 13999)  # No error

product_2 = Product("iPhone 12", -13999)
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
#   File "<input>", line 6, in __init__
# ValueError: Price must be bigger zero

product_3 = Product("iPhone 12", 15999)
print(product_3.price)  # 15999

product_3.price = 12000
print(product_3.price)  # 12000
