#
#
#

# Before property
class Invoice:

    def __init__(self, product_name, price, vat, quantity):
        self.product_name = product_name
        self.price = price
        self.vat = vat
        self.quantity = quantity
        self.total = (self.price + ((self.price / 100) * self.vat)) * self.quantity

    def set_price(self, price):
        self.price = price
        self.total = (self.price + ((self.price / 100) * self.vat)) * self.quantity

    def get_price(self):
        return self.price

    def print_invoice(self):
        print(f"Total price of {self.quantity} {self.product_name}(s) is {self.total} including %{self.vat} vat.")


pencil = Invoice("Pencil", 7, 10, 20)

pencil.get_price()  # 7
pencil.print_invoice()  # Total price of 20 Pencil(s) is 154.0 including %10 vat.

pencil.set_price(14)
pencil.get_price()  # 14
pencil.print_invoice()  # Total price of 20 Pencil(s) is 308.0 including %10 vat.


# After property
class Invoice:

    def __init__(self, product_name, price, vat, quantity):
        self.product_name = product_name
        self._price = price
        self.vat = vat
        self.quantity = quantity

    @property  # getter
    def __my_total(self):
        return (self._price + ((self._price / 100) * self.vat)) * self.quantity

    @property  # getter
    def price(self):
        return self._price

    @price.setter  # setter.
    def price(self, value):
        self._price = value

    def print_invoice(self):
        print(f"Total price of {self.quantity} {self.product_name}(s) is {self.__my_total} including %{self.vat} vat.")


pencil = Invoice("Pencil", 7, 10, 20)

print(pencil.price)  # 7
pencil.print_invoice()  # Total price of 20 Pencil(s) is 154.0 including %10 vat.

pencil.price = 14
print(pencil.price)  # 14
pencil.print_invoice()  # Total price of 20 Pencil(s) is 308.0 including %10 vat.
