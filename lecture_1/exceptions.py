#
#

def divide_(a, b):
    try:

        print(int(a) / int(b))

    except ZeroDivisionError as err:
        print(f"Error message : {err}")
        print("Second value cannot be 0...")
        # continue
    except ValueError as err:
        print(f"Error message: {err}")
        print("Values must be numeric...")

    except Exception as err:
        print(f"Error message: {err}")
        print("Unknow exception...")

    finally:
        print("Always works...")


divide_(2, 1)  # Output: 2.0

divide_(2, 0)
# Error message : division by zero
# Second value cannot be 0...
# Always works...

divide_(5, "a")
# Error message: invalid literal for int() with base 10: 'a'
# Values must be numeric...
# Always works..


##########################

def my_func(a, b):
    if a * b > 1000:
        raise BaseException("a*b must be less than 1000")
    else:
        print(a * b)


my_func(50, 10)  # Output: 500
my_func(100, 100)  # Output: BaseException: a*b must be less than 1000


try:
    my_func(50, 50)
except Exception as bs:
    print(bs)
# Traceback (most recent call last):
# File "<input>", line 3, in <module>
# File "<input>", line 4, in my_func
# BaseException: a*b must be less than 1000


try:
    my_func(50, 50)
except BaseException as bs:
    print(bs)               # a*b must be less than 1000