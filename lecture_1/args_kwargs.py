#
#

def basic_func(arg):
    print(arg)


def args_func(*args):
    print(args)


def kwargs_func(**kwargs):
    print(kwargs)


def args_kwargs_func(*args, **kwargs):
    if args:
        print("args worked: ", args)
    if kwargs:
        print("kwargs worked: ", kwargs)


args_func(1, 3, 5, 7)  # Output: (1, 3, 5, 7)

kwargs_func(name="Arif", surname="Eker")  # Output: {'name': 'Arif', 'surname': 'Eker'}

args_kwargs_func(1, 2, 3, 4)  # Output: (1, 2, 3, 4)

args_kwargs_func(name="Arif", surname="Eker")  # Output: {'name': 'Arif', 'surname': 'Eker'}

args_kwargs_func(1, 2, 3, 4, name="Arif", surname="Eker")
# Output:
# (1, 2, 3, 4)
# {'name': 'Arif', 'surname': 'Eker'}


args_ = 1, 2, 3, 4
args_kwargs_func(*args_)  # Output: (1, 2, 3, 4)

kwargs_ = {"name": "Arif",
           "surname": "Eker"}

args_kwargs_func(*kwargs_)  # Output: ('name', 'surname')
args_kwargs_func(**kwargs_)  # Output: {'name': 'Arif', 'surname': 'Eker'}


