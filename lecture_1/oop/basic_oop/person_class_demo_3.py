#
#
class Person:
    # constructor
    def __init__(self, name, surname, birth_date):
        # object attributes
        self.name_ = name
        self.surname_ = surname
        self.birth_date_ = birth_date

    def get_info(self):
        return f"""\n Name : {self.name_} \n SurName : {self.surname_} \n Birth Date : {self.birth_date_}"""

    def calculate_age(self):
        import datetime as dt
        return dt.datetime.now().year - self.birth_date_


person_1 = Person("Arif", "Eker", 1998)

print(person_1.get_info())
#  Name : Arif
#  SurName : Eker
#  Birth Date : 1998

print(person_1.calculate_age())
# 24