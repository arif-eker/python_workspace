#
#
#

def my_range(*args):
    start = 0
    stop = 1
    try:
        if len(args) == 1:
            stop = args[0]
        elif len(args) == 2:
            start = args[0]
            stop = args[1]

        while start < stop:
            yield start
            start += 1

    except Exception as err:
        print(err)


type(my_range())  # <class 'generator'>

my_list = my_range(1)
for i in my_list:
    print(i)

# 0

type(my_list)  # <class 'generator'>

my_list = my_range(1, 5)
for i in my_list:
    print(i)

# 1
# 2
# 3
# 4

my_list = my_range(4)
for i in my_list:
    print(i)

# 0
# 1
# 2
# 3


for num in my_range(1, 6):
    print(num)

# 1
# 2
# 3
# 4
# 5


new_gen = (num for num in range(3, 6))

type(new_gen)  # <class 'generator'>

for x in new_gen:
    print(x)
