#
#

class User:
    active_user = 0

    @classmethod
    def display_user_counts(cls):
        print(cls.active_user)

    @classmethod
    def from_string(cls, data_str):
        name, surname, age = data_str.split(",")
        return cls(name, surname, age)

    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
        User.active_user += 1


print(User.display_user_counts())
# 0
# None

user_A = User("Arif", "Eker", 24)
user_B = User("Cenk", "Aydın", 30)

print(User.display_user_counts())
# 2
# None


user_C = User.from_string("Mahmut,Kaya,19")

print(User.display_user_counts())
# 3
# None