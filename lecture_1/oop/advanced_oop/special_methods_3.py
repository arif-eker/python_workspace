#
#
#

class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    # str method is customized for this class
    def __str__(self):
        return f"{self.name} {self.surname}"

    # len method is customized for this class
    def __len__(self):
        return self.age


s = "12"
str(s)  # '12'
len(s)  # 2

person = Person("Arif", "Eker", 24)

# before customized
str(person)  # '<__main__.Person object at 0x000001932075DF88>'

len(person)
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
# TypeError: object of type 'Person' has no len()

# after customized
person_2 = Person("Mehmet", "Taş", 27)
str(person_2)  # 'Mehmet Taş'

len(person_2)  # 27
