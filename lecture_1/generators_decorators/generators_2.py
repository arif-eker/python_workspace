#
#

import sys

my_list = [i ** 2 for i in range(4000000)]

generator_list = (i ** 2 for i in range(4000000))
my_list.__sizeof__()
sys.getsizeof(my_list) / (1024 * 1024)  # 34.090782165527344 mb
sys.getsizeof(generator_list) / (1024 * 1024)  # 0.00011444091796875 mb

import time

list_start = time.time()
sum([i ** 2 for i in range(40000000)])
list_stop = time.time() - list_start
print(list_stop)  # ~ 14.181675910949707sec

generator_start = time.time()
sum((i ** 2 for i in range(40000000)))
generator_stop = time.time() - generator_start
print(generator_stop)  # ~ 14.15634083747863 sec

# Generators > List for memory and speed
# use it :)
