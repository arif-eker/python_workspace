#
# check for default python modules (libraries):
# https://docs.python.org/3/py-modindex.html

####################################################################################
# math module

import math

print(math.sqrt(25))        # Output: 5.0
print(math.pow(2, 5))       # Output: 32.0

print(math.log2(8))         # Output: 3.0
print(math.log10(100))      # Output: 2.0
print(math.log(8, 2))       # Output: 3.0
print(math.log(100, 10))    # Output: 2.0
print(math.log10(100))      # Output: 2.0

print(math.log1p(1))                    # Output: 0.6931471805599453
print(math.expm1(0.6931471805599453))   # Outout: 1.0
print(math.exp(0.6931471805599453))     # Output: 2.0

print(math.factorial(6))                # Output: 720

####################################################################################
# random module

import random

print(random.random())              # All result between 0.0 - 1.0
print(random.uniform(1, 5))         # All result between 1.0 - 5.0
print(random.randint(1, 5))         # Integer number between 1-5
print(random.randrange(1, 5, 2))
print(random.randrange(1, 3, 1))

####################################################################################
# datetime module

import datetime as dt

print(dt.datetime.now())                # Output: Current time : 2022-01-17 01:18:16.870444
print(dt.datetime.now().year)           # Output: 2022
print(dt.datetime.now().month)          # Output: 1
print(dt.datetime.now().weekday())      # Output: 0
print(dt.datetime.now().day)            # Output: 17
print(dt.datetime.now().time())         # Output: 01:18:41.182061
print(dt.datetime.now().hour)           # Output: 1

print(dt.time(12, 25, 13, 1000).hour)           # Output: 12
print(dt.time(12, 25, 13, 1000).minute)         # Output: 25
print(dt.time(12, 25, 13, 1000).second)         # Output: 13
print(dt.time(12, 25, 13, 1000).microsecond)    # Output: 1000

print(dt.date(2022, 1, 2).today())      # Output: 2022-01-17
print(dt.date(2022, 1, 2).weekday())    # Output: 6
print(dt.date(2022, 1, 2).ctime())      # Output: Sun Jan  2 00:00:00 2022
print(dt.date(2022, 1, 2).month)        # Output: 1

print(dt.date(2022, 1, 2).strftime("%Y"))  # Output: 2022
print(dt.date(2022, 1, 2).strftime("%y"))  # Output: 22

print(dt.date(2022, 1, 2).strftime("%D"))  # Output: 01/02/2
print(dt.date(2022, 1, 2).strftime("%d"))  # Output: 02

print(dt.date(2022, 1, 2).strftime("%A"))  # Output: Sunday
print(dt.date(2022, 1, 2).strftime("%a"))  # Output: Sun

print(dt.date(2022, 1, 2).strftime("%B"))  # Output: January
print(dt.date(2022, 1, 2).strftime("%b"))  # Output: Jan

print(dt.date(2022, 1, 2).strftime("%C"))  # Output: 20
print(dt.date(2022, 1, 2).strftime("%c"))  # Output: Sun Jan  2 00:00:00 2022

print(dt.date(2022, 1, 2).strftime("%M"))  # Output: 00
print(dt.date(2022, 1, 2).strftime("%m"))  # Output: 01

print(dt.date(2022, 1, 2).strftime("%X"))  # Output: 00:00:00
print(dt.date(2022, 1, 2).strftime("%x"))  # Output: 01/02/22

####################################################################################
# os module

import os

print(os.name)  # Output: nt (nt= Windows Operating System)

print(os.getcwd())  # Output: current directory path: D:\my_projects\pycharms\python_workspace

# print(os.mkdir("file_with_mkdir"))  # create new directory in current directory
# print(os.makedirs("new_dir/new_new_dir")) # create new directory

print(os.listdir())  # Output: ['.git', '.gitignore', '.idea', 'lecture_1', 'lecture_info']

print(os.stat(os.getcwd()+"\\lecture_1\\args_kwargs.py"))
# Output:
# os.stat_result(st_mode=33206, st_ino=2533274790419798, st_dev=1117851787, st_nlink=1, st_uid=0, st_gid=0,
# st_size=992, st_atime=1642371126, st_mtime=1642371119, st_ctime=1642371049)


print(os.path.abspath("args_kwargs.py"))  # Output: getting full path this file  : D:\my_projects\pycharms\python_exercises\args_kwargs.py

print(os.path.exists(os.getcwd()+"\\lecture_1\\args_kwargs.py"))  # True
print(os.path.exists(os.getcwd()+"\\lecture_1\\hello.py.py"))  # False

####################################################################################
# re module (regular expression)

import re

my_str = "Hello, my name is Arif!"

print(re.findall("l", my_str))      # Output: ['l', 'l']
print(re.split(" ", my_str))        # Output: ['Hello,', 'my', 'name', 'is', 'Arif!']
print(re.split("m", my_str))        # Output: ['Hello, ', 'y na', 'e is Arif!']
print(re.sub("l", "L", my_str))     # Output: HeLLo, my name is Arif! : chance "l" to "L"

print(re.search("my", my_str))              # Output: <re.Match object; span=(7, 9), match='my'>
print(re.search("my", my_str).span())       # Output: (7, 9)
print(re.search("my", my_str).start())      # Output: 7
print(re.search("my", my_str).end())        # Output: 9

my_str2 = "This is my 1st time!"

print(re.findall("[a-zA-Z]", my_str2))  # Output: ['T', 'h', 'i', 's', 'i', 's', 'm', 'y', 's', 't', 't', 'i', 'm', 'e']

print(re.findall("[^a-zA-Z]", my_str2))  # Output: [' ', ' ', ' ', '1', ' ', '!']
print(re.findall("[1-9]", my_str2))      # Output: ['1']
print(re.findall("[^1-9]", my_str2))     # Output: ['T', 'h', 'i', 's', ' ', 'i', 's', ' ', 'm', 'y', ' ', 's', 't', ' ', 't', 'i', 'm', 'e', '!']

print(re.findall("^T", my_str2))  # Does the sentence start with "T"
print(re.findall("!$", my_str2))  # Does the sentence end with "!"

my_str3 = "Hello 1234 Hello"
print(re.findall("[0-9]{1,4}", my_str3))  # Output: ['1234']
print(re.findall("[0-9]{1,3}", my_str3))  # Output: ['123', '4']
print(re.findall("[0-9]{2,3}", my_str3))  # Output: ['123']

