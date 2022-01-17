#
#
#

number = 25


def first_func():
    number = 15
    print(f"First Func Working... Number is : {number}")

    def second_func():
        number = 5
        print(f"Second Func Working... Number is : {number}")

    second_func()
    print(f"First Func Working... Number is : {number}")


print("Number : ", number)
# Number :  25

first_func()
# First Func Working... Number is : 15
# Second Func Working... Number is : 5
# First Func Working... Number is : 15

print("Number : ", number)  # Number :  25

###############################################################################################################################################################

# Global use

number = 25


def first_func():
    number = 15
    print(f"First Func Working... Number is : {number}")

    def second_func():
        global number
        number = 5
        print(f"Second Func Working... Number is : {number}")

    second_func()
    print(f"First Func Working... Number is : {number}")


print("Number : ", number)  # Number :  25

first_func()
# First Func Working... Number is : 15
# Second Func Working... Number is : 5
# First Func Working... Number is : 15

print("Number : ", number)  # Number :  5

###############################################################################################################################################################

# Nonlocal use
number = 25


def first_func():
    number = 15
    print(f"First Func Working... Number is : {number}")

    def second_func():
        nonlocal number
        number = 7
        print(f"Second Func Working... Number is : {number}")

    second_func()
    print(f"First Func Working... Number is : {number}")


print("Number : ", number)  # Number :  25

first_func()
# First Func Working... Number is : 15
# Second Func Working... Number is : 7
# First Func Working... Number is : 7

print("Number : ", number)  # Number :  25
