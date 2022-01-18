#
#
#

# Public Members
# Private Members
# Protected Members


# Public Members

class MyClass:
    class_att = "class_attribute"  # public variable

    def ins_method(self):  # public method
        print("Instance Method.")

    @classmethod
    def class_method(cls):  # public method
        print("Class Method.")

    @staticmethod
    def static_method():  # public method
        print("Static Method.")


myclass = MyClass()
print(myclass.class_att)

myclass.ins_method()

MyClass.class_method()

MyClass().static_method()


################################################################################################################################################

# Private Members


class Person:
    __private_att = "private variable"
    # use "__" for define private variables

    public_att = "public variable"

    @classmethod
    def print_private(cls):
        print(cls.__private_att)

    def print_private_var(self):
        print(self.__private_att)


person = Person()
print(person.public_att)  # public variable

person.print_private_var()  # private variable

print(person.__private_att)
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
# AttributeError: 'Person' object has no attribute '__private_att'

person.print_private()  # private variable

print(dir(Person))  # ['_Person__private_att', '__class__', '__delattr__', ......]

print(person._Person__private_att)  # private variable


################################################################################################################################################

# Protected Members

class Product:
    _protected_att = "protected variable"
    # use "_" for define protected variables

    __private_att = "private variable"
    public_att = "public variable"


prod = Product()

print(prod._protected_att)  # protected variable
