#
#
# topic numbers = [1, 2, 3, 4, 5, 6]
# CTRL + F and enter --topic number-- for jump topic to topic
# for example "--5--"

# topics:
# map, filter, zip, enumerate, slice, reversed, hash, globals, locals, vars

#########################################################################################################################################################
# Topic: --1--

# map

# map(func, iterable_object)

def cal_power(num):
    return num ** 2


numbers = [1, 2, 3]
numbers2 = [10, 20, 30]

powers = list(map(cal_power, numbers))
print(powers)  # [1, 4, 9]

powers2 = list(map(lambda x: x ** 3, powers))
print(powers2)  # [1, 64, 729]

powers3 = list(map(lambda x, y: y ** x, numbers, numbers2))
print(powers3)  # [10, 400, 27000]

#########################################################################################################################################################
# Topic: --2--

# filter

# filter(func, iterable_object)

numbers = [1, 3, 5, 6, 3, 2, 8, 15, 17, 28]

filters = list(filter(lambda x: x % 2 == 0, numbers))
print(filters)  # [6, 2, 8, 28]

#########################################################################################################################################################
# Topic: --3--

# zip

# zip(iterable_object, iterable_object,...)

nums = [10, 20, 30, 40]
chars = ["a", "b", "c", "d"]
char_ = ["@"]

print(list(zip(nums, chars)))  # [(10, 'a'), (20, 'b'), (30, 'c'), (40, 'd')]

print(list(zip(char_, nums)))  # [('@', 10)]

zipped = list(zip(nums, chars))  # ----> alternative : zip(nums, chars)
print(zipped)  # [(10, 'a'), (20, 'b'), (30, 'c'), (40, 'd')]

unzipped = list(zip(*zipped))
print(unzipped)  # [(10, 20, 30, 40), ('a', 'b', 'c', 'd')]

#########################################################################################################################################################
# Topic: --4--

# enumerate

# enumerate(iterable_object, index_no (default 0))

names = ["Arif", "Senem", "Süleyman", "Coşkun"]

enums = list(enumerate(names))
print(enums)  # [(0, 'Arif'), (1, 'Senem'), (2, 'Süleyman'), (3, 'Coşkun')]

enums = list(enumerate(names, 30))
print(enums)  # [(30, 'Arif'), (31, 'Senem'), (32, 'Süleyman'), (33, 'Coşkun')]

for i in enumerate(names, 5):
    print(i)

# (5, 'Arif')
# (6, 'Senem')
# (7, 'Süleyman')
# (8, 'Coşkun')


#########################################################################################################################################################
# Topic: --5--

# hash

print(hash("name"))  # 5_938_087_064_566_676_320

print(hash("hello"))  # -6989001865321736959

print(hash(tuple([1, 2, 3])))  # 2_528_502_973_977_326_415

#########################################################################################################################################################
# Topic: --6--

# globals, locals, vars


global_var = "GLOBAL_VAR"


def funcs():
    local_var = "LOCAL_VAR"
    print(locals())


print(globals())
funcs()


