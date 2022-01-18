#
#
#

class Human:
    kind = "Human"

    def __init__(self):
        self.name = "Human"

    def walk(self):
        print("Human walking...")

    def speak(self):
        print("Human speaking...")

    @staticmethod
    def human_static():
        print("Human static method.")

    @property
    def nationality(self):
        return self.__nationality

    @nationality.setter
    def nationality(self, new_nation):
        self.__nationality = new_nation


human = Human()
human.speak()  # Human speaking...
human.walk()  # Human walking...

print(human.name)  # Human
print(human.kind)  # Human


class Parent(Human):
    pass


father1 = Parent()
father2 = Parent()

father1.speak()  # Human speaking...

print(father1.name)  # Human
print(father2.name)  # Human

father2.name = "Father 2"
print(father1.name)  # Human
print(father2.name)  # Father 2

father1.human_static()  # Human static method.

print(father1.nationality)  # AttributeError: 'Parent' object has no attribute '_Human__nationality'
print(father2.nationality)  # AttributeError: 'Parent' object has no attribute '_Human__nationality'

father1.nationality = "German"
father2.nationality = "English"

print(father1.nationality)  # German
print(father2.nationality)  # English
