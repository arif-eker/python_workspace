#
#

class Pet:
    species = ["Cat", "Dog", "Fish"]

    def __init__(self, pet_name, pet_species):
        if pet_species not in Pet.species:
            raise ValueError(f"{pet_species} is not a pet species.")

        self.name = pet_name
        self.species = pet_species


petA = Pet("Kuro", "Dog")
petB = Pet("Myne", "Cat")

petC = Pet("Leo", "Lion")
# Output :
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
#   File "<input>", line 7, in __init__
# ValueError: Lion is not a pet species.

Pet.species.append("Wolf")
petD = Pet("Gray", "Wolf")  # no Error
