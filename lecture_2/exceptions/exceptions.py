#
#
# topic numbers = [1, 2, 3, 4, 5, 6]
# CTRL + F and enter --topic number-- for jump topic to topic
# for example "--5--"


"""
try:
    Codes that may error when run

except:
    codes to run when an error occurs

except:
...
...
...

"""


#########################################################################################################################################################
# Topic: --1--

def div(a, b):
    print(a / b)


try:
    div(3, 0)
except:
    print("Unknown Error")
    print("End")

# Unknown Error
# End

#########################################################################################################################################################
# Topic: --2--

try:
    div("a", 5)
except ZeroDivisionError:
    print(ZeroDivisionError)
except TypeError:
    print(TypeError)  # <class 'TypeError'>

try:
    div(5, 0)
except ZeroDivisionError:
    print(ZeroDivisionError)  # <class 'ZeroDivisionError'>
except TypeError:
    print(TypeError)
except:
    print("Unknown Error.")

#########################################################################################################################################################
# Topic: --3--

try:
    div(3, 0)
except (ValueError, ZeroDivisionError):
    print("Value or Zero Div Error")  # Value or Zero Div Error

except NameError:
    print(NameError)

#########################################################################################################################################################
# Topic: --4--

try:
    div(6, 0)
except (ValueError, ZeroDivisionError) as err:
    print(err)  # division by zero

try:
    div(6, "a")
except (ValueError, ZeroDivisionError, TypeError) as err:
    print(err)  # unsupported operand type(s) for /: 'int' and 'str'

#########################################################################################################################################################
# Topic: --5--

try:
    my_list = range(5000)
    print("list created...")
    print(my_list[7000])
    print("list will be delete...")
    del my_list
except Exception as err:
    print("\nExcept working...")
    print(f"except message: {err}")

finally:
    print("\nfinally working...")
    print("list deleting...")
    del my_list

# list created...

# Except working...
# except message: range object index out of range

# finally working...
# list deleting...

#########################################################################################################################################################
# Topic: --6--

try:
    count = -5
    if count < 0:
        raise ValueError("Count must be bigger than zero")
    else:
        print(count)

except Exception as err:
    print(f"Error Message: {err}")
    # Error Message: Count must be bigger than zero

