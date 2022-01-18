#
#
#

class Employee:
    def report(self):
        print("Employee is reporting.")


class Accountant(Employee):
    def report(self):
        print("Accountant is reporting.")


class HumanResources(Employee):
    def report(self):
        print("HumanResources is reporting.")


worker1 = HumanResources()
worker1.report()

# Human report method overrides parents methods


