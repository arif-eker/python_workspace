#
#
# topic title numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# CTRL + F and enter --topic title number-- for jump topic to topic
# for example "--5--"

#########################################################################################################################################################
# Topic: --1--

"""

If we put the letter "r" at the beginning of a string, there is no need to use escape characters.
that is, we can define the string in its raw form with escape characters.

some escape characters:
# \n,  \t,  \',  \",  \r,  \
"""

# Example_1:
# use r"path " if you dont want to use "\\" (double \)
path = r"D:\my_projects\pycharms\python_workspace\lecture_2\basics\strings"
with open(path + r"\deneme1.txt", "w") as file:
    file.write("hello")  # it's create a file and write hello

# Example_2:
# no use r""
# it's will throw error
path2 = "D:\my_projects\pycharms\python_workspace\lecture_2\basics\strings"
with open(path2 + "\deneme2.txt", "w") as file:
    file.write("hello")

# ...
# Traceback (most recent call last):
#   File "<input>", line 2, in <module>
# OSError: [Errno 22] Invalid argument: 'D:\\my_projects\\pycharms\\python_exercises\\lecture_2\x08asics\\deneme2.txt'


# Example_3:
# with escape characters

path3 = "D:\\my_projects\\pycharms\\python_workspace\\lecture_2\\basics\\strings"
with open(path3 + "\\deneme3.txt", "w") as file:
    file.write("hello")  # worked!

#########################################################################################################################################################
# Topic: --2--

my_str = "Hello, my name is Arif."

print(my_str)  # Hello, my name is Arif.

# does not change the variable, it converts all letters to lowercase.
print(my_str.lower())  # hello, my name is arif.

# does not change the variable, it converts all letters to uppercase.
print(my_str.upper())  # HELLO, MY NAME IS ARIF.

# does not change the variable, capitalizes the first letter of each word
print(my_str.title())  # Hello, My Name Is Arif.

# does not change the variable, capitalizes the first letter of the sentence
print(my_str.capitalize())  # Hello, my name is arif.

# converts uppercase letters to lowercase and lowercase letters to uppercase.
print(my_str.swapcase())  # hELLO, MY NAME IS aRIF.

#########################################################################################################################################################
# Topic: --3--

lower_str = "lower"
upper_str = "UPPER"
title_str = "My Title"

# Are all letters of the given text lowercase?
print(lower_str.islower())  # True
print(lower_str.isupper())  # False

# Are all letters of the given text uppercase?
print(upper_str.islower())  # False
print(upper_str.isupper())  # True

# Is the given text in the title structure?
print(title_str.istitle())  # True
print(lower_str.istitle())  # False
print(upper_str.istitle())  # False

#########################################################################################################################################################
# Topic: --4--

decimal = "0123456789"
digit = "0123456789⁰¹²³⁴⁵⁶⁷⁸⁹"
numeric = "0123456789⁰¹²³⁴⁵⁶⁷⁸⁹⅓⅔⅛"

# is decimal?
# (numbers)
print(decimal.isdecimal())  # True
print(digit.isdecimal())  # False
print(numeric.isdecimal())  # False

# is digit?
# (numbers, exponential numbers)
print("is digit?", decimal.isdigit())  # True
print("is digit?", digit.isdigit())  # True
print("is digit?", numeric.isdigit())  # False

# is numeric?
# (numbers, exponential numbers, fractional numbers)
print("is numeric?", decimal.isnumeric())  # True
print("is numeric?", digit.isnumeric())  # True
print("is numeric?", numeric.isnumeric())  # True

#########################################################################################################################################################
# Topic: --5--

my_str = "_my name is arif. what is your name?"

len(my_str)  # 36

# finds the index of the entered substring in the string.
print(my_str.find("name"))  # 4
print(my_str.find("name", 5))  # 31

# searched substring not found between start index (5) and end index (9)
print(my_str.find("name", 5, 9))  # -1 #

print(my_str.rfind("name"))  # 31

"""
index() is similar to find(). If it can't find the difference, the substring, it will throw a ValueError error.
"""
print(my_str.index("name"))  # 4

print(my_str.index("hello"))
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
# ValueError: substring not found

#########################################################################################################################################################
# Topic: --6--

my_str = "this, is, amazing, wonderful"

# default: " " (space character)

print(my_str.split())  # ['this,', 'is,', 'amazing,', 'wonderful'] ----> 4 items

print(my_str.split(","))  # ['this', ' is', ' amazing', ' wonderful'] ----> 4 items

print(my_str.split(",", maxsplit=1))  # ['this', ' is, amazing, wonderful'] ----> 2 items
print(my_str.split(",", maxsplit=2))  # ['this', ' is', ' amazing, wonderful'] --> 3 items

print(my_str.split(";"))  # ['this, is, amazing, wonderful'] -----> 1 item

#########################################################################################################################################################
# Topic: --7--

my_str = "hello world"
print("".join(my_str))  # hello world
print(",".join(my_str))  # h,e,l,l,o, ,w,o,r,l,d
print("-".join(my_str))  # h-e-l-l-o- -w-o-r-l-d
print(" ".join(my_str))  # h e l l o   w o r l d

numbers = ["1", "2", "3", "4"]
print("-".join(numbers))  # 1-2-3-4
print("*".join(numbers))  # 1*2*3*4

#########################################################################################################################################################
# Topic: --8--

my_str = "abc_abc_abc_abc_abc"

# does not change the string.
print(my_str.replace("_", "-"))  # abc-abc-abc-abc-abc

# makes changes as many as the entered number
print(my_str.replace("_", "-", 1))  # abc-abc_abc_abc_abc
print(my_str.replace("_", "-", 2))  # abc-abc-abc_abc_abc

#########################################################################################################################################################
# Topic: --9--

my_str = "my name is arif, what is your name?"
# finds the number of times the subtext occurs in the text
print(my_str.count("arif"))  # 1
print(my_str.count("is"))  # 2
print(my_str.count("a"))  # 4

print(my_str.count("a", 8))  # 3

#########################################################################################################################################################
# Topic: --10--

my_str = "hello world"

print(my_str.startswith("h"))  # True
print(my_str.startswith("he"))  # True

print(my_str.startswith("her"))  # False
print(my_str.startswith("e"))  # False

print(my_str.endswith("d"))  # True
print(my_str.endswith("ld"))  # True

print(my_str.endswith("old"))  # False
print(my_str.endswith("e"))  # False

#########################################################################################################################################################
# Topic: --11--

my_str = "Arif"
print(my_str.center(14, "*"))  # *****Arif*****
print(my_str.center(20, "-"))  # --------Arif--------

print("Name".ljust(20), "Surname".ljust(20), "\n", "Arif".ljust(20), "Eker".ljust(20))
# Name                 Surname
#  Arif                 Eker

print("Name".rjust(20), "Surname".rjust(20), "\n", "Arif".rjust(20), "Eker".rjust(20))
#                 Name              Surname
#                  Arif                 Eker

#########################################################################################################################################################
# Topic: --12--

my_str = "[(1, 2, 3, 4, 5, 6)]"

print(my_str.strip("["))  # (1, 2, 3, 4, 5, 6)]
print(my_str.strip("]"))  # [(1, 2, 3, 4, 5, 6)

print(my_str.strip("[]"))  # (1, 2, 3, 4, 5, 6)
print(my_str.strip("]["))  # (1, 2, 3, 4, 5, 6)
#

my_str = "++--//--++name++--//--++"

print(my_str.strip("+"))  # --//--++name++--//--

print(my_str.strip("+-"))  # //--++name++--//

print(my_str.strip("+-/"))  # name
print(my_str.strip("/-+"))  # name

#########################################################################################################################################################
# Topic: --13--

val = 6.257
print(f"Value: {val:.1f}")  # Value: 6.3
print(f"Value: {val:.2f}")  # Value: 6.26
print(f"Value: {val:.3f}")  # Value: 6.257

val = 4
print(f"Value: {val:#b}")  # Value: 0b100
print(f"Value: {val:#o}")  # Value: 0o4
print(f"Value: {val:#x}")  # Value: 0x4
