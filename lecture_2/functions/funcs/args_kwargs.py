#
#

def my_sum(a, b):
    print("Result: ", a + b)


my_sum(3, 5)  # Result:  8


def args_sum(*numbers):
    print("args lenght: ", len(numbers))
    result = ""
    total = 0
    for num in numbers:
        if type(num) == str:
            result += num

        else:
            total += num

    if result:
        print("Result: ", result)
    elif total:
        print("Total: ", total)
    else:
        raise Exception("Error.")


args_sum(1, 2, 3)
# args lenght:  3
# Total:  6

args_sum(1, 2, 3, 4, 5)
# args lenght:  5
# Total:  15


args_sum("a", "b", "c")


# args lenght:  3
# Result:  abc


def mixed(arg, *args):
    if arg:
        print("arg worked!")
        print(arg)

    if args:
        print("args worked!")
        print(args)


mixed(3)
# arg worked!
# 3

mixed(1, 2, 3)


# arg worked!
# 1
# args worked!
# (2, 3)


def my_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"Key: {key} ------> Value: {value}")


my_kwargs(name="Arif", surname="Eker")
# Key: name ------> Value: Arif
# Key: surname ------> Value: Eker

person = {"name": "Selin",
          "surname": "Arabacı"}

my_kwargs(**person)
# Key: name ------> Value: Selin
# Key: surname ------> Value: Arabacı

my_kwargs({"name": "Yasemin", "age": 32})


# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
# TypeError: my_kwargs() takes 0 positional arguments but 1 was given


def args_kwargs(*args, **kwargs):
    if args:
        print("args worked!", "\n", args)
    if kwargs:
        print("kwargs worked!", "\n", kwargs)


args_kwargs(1, 2, 3, 4)
# args worked!
#  (1, 2, 3, 4)

args_kwargs([1, 2, 3, 4])
# args worked!
#  ([1, 2, 3, 4],)

args_kwargs(name="Arif", surname="Eker")
# kwargs worked!
#  {'name': 'Arif', 'surname': 'Eker'}


args_kwargs(1, 2, 3, **{"name": "Sultan", "age": 26})
# args worked!
#  (1, 2, 3)
# kwargs worked!
#  {'name': 'Sultan', 'age': 26}
