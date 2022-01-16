#
#

class User:
    active_users = 0

    def __init__(self, username, usersurname, birth_date):
        self.username_ = username
        self.usersurname_ = usersurname
        self.birth_date_ = birth_date
        User.active_users += 1


print(f"Active User Counts : {User.active_users}")  # Active User Counts : 0

userA = User("Arif", "Eker", 1998)
userB = User("Mustafa", "Doğan", 1993)

print(f"Active User Counts : {User.active_users}")  # Active User Counts : 2
