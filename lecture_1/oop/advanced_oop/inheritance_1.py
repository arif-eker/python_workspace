#
#
#

class Person:
    def __init__(self, name, surname, age):
        print("Person created.")
        self.name = name
        self.surname = surname
        self.age = age

    def intro(self):
        print(f"Name: {self.name}  Surname: {self.surname}  Age: {self.age}")


class Student(Person):
    def __init__(self, name, surname, age, school_no):
        Person.__init__(self, name, surname, age)
        print("Student created.")
        self.school_no = school_no


class Teacher(Person):
    def __init__(self, name, surname, age, branch):
        # Person.__init__(self, name, surname, age)
        super().__init__(name, surname, age)
        print("Teacher created.")
        self.branch = branch


person = Person("Mustafa", "Kısakulak", 37)  # Person created.
person.intro()  # Name: Mustafa  Surname: Kısakulak  Age: 37

teacher = Teacher("Kemal", "Kaleli", 32, "English")
# Person created.
# Teacher created.
teacher.intro()  # Name: Kemal  Surname: Kaleli  Age: 32

student = Student("Arif", "Eker", 24, 271)
# Person created.
# Student created.
student.intro()  # Name: Arif  Surname: Eker  Age: 24
