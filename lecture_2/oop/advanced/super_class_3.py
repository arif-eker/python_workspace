#
#
#

# super() is represents a higher (parent) class.


class Parent:
    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2

    def write(self):
        print(f"var1: {self.var1}  var2: {self.var2}")


class Child(Parent):
    def __init__(self, name):
        self.name = name

    def write_name(self):
        print(self.name)


child = Child("Arif")
child.write_name()

child.write()
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
#   File "<input>", line 8, in write
# AttributeError: 'Child' object has no attribute 'var1'

child.var1 = "My"
child.var2 = "Name"
child.write()  # var1: My  var2: Name


###########################

# True form:


class Parent:
    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2

    def write(self):
        print(f"var1: {self.var1}  var2: {self.var2}")


class Child(Parent):
    def __init__(self, name, var1, var2):
        super().__init__(var1, var2)
        # Parent.__init__(var1, var2) -----> another use form
        self.name = name

    def write_name(self):
        print(self.name)


child = Child("Arif", "a", "b")
child.write()  # var1: a  var2: b

child.var1 = "K"
child.var2 = "L"
child.write()  # var1: K  var2: L
