#
#
#

class Father:
    def father_speak(self):
        print("Father speaking.")


class Mother:
    def mother_speak(self):
        print("Mother speaking.")


class Child(Mother, Father):
    pass


child = Child()

child.father_speak()  # Father speaking.
child.mother_speak()  # Mother speaking.


###############################################################################################################################


class Father:
    def speak(self):
        print("Father speaking.")


class Mother:
    def speak(self):
        print("Mother speaking.")


class Child(Mother, Father):
    pass


class Child2(Father, Mother):
    pass


child = Child()
child.speak()  # Mother speaking.

child2 = Child2()
child2.speak()  # Father speaking.

# The first given class overrides other methods.

# for child, Mother overrides father's speak
# for child2, Father overrides mother's speak

###################################################################################################################################################


class Father:
    def speak(self):
        print("Father speaking.")

    def write(self):
        print("Father writing.")


class Mother:
    def speak(self):
        print("Mother speaking.")

    def write(self):
        print("Mother writing.")


class Child(Mother, Father):
    def speak(self):
        Father.speak(self)

    def write(self):
        super().write()
        # Mother.write(self)
        # Since the first class is the mother, it automatically selects her as the super class.


c = Child()
c.speak()  # Father speaking.
c.write()  # Mother writing.
