#
#
#

class Animal:

    def __init__(self, name):
        self.animal_name = name

    @classmethod
    def write_animal_name(cls):
        print(cls.animal_name)


bird = Animal("bird")
bird.write_animal_name()


# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
#   File "<input>", line 9, in write_animal_name
# AttributeError: type object 'Animal' has no attribute 'animal_name'

#
# class method cant use instance variables
#

class Animal:
    animal_name = "Animal"

    def __init__(self, name):
        self.name = name

    def write_name(self):
        print(self.name)

    @classmethod
    def write_animal_name(cls):
        print(cls.animal_name)


dog = Animal("dog")
dog.write_animal_name()  # Animal
dog.write_name()  # dog

