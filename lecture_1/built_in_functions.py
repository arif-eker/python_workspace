#
#
##########################
# Lambda #
##########################
# 1.
sum_ = lambda x, y: x + y
print(sum_(1, 2))  # Output: 3

# 2.
import numpy as np

sum_ = lambda *x: np.sum(x)
print(sum_(1, 2, 3))  # Output: 6

# 3.
sum_ = lambda x: np.sum(x)
print(sum_([1, 2, 3]))  # Output: 6

##########################
# Map #
##########################
numbers = [1, 2, 3, 4]
result = list(map(lambda x: x ** x, numbers))
print(result)  # Output: [1, 4, 27, 256]

##########################
# Filter #
##########################
numbers = [1, 3, 5, 7, 4, 2, 9, 11, 8]
result = list(filter((lambda x: x % 2 == 1), numbers))
print(result)  # Output: [1, 3, 5, 7, 9, 11]

result = list(filter((lambda x: x % 2 == 0), numbers))
print(result)  # Output: [4, 2, 8]

result = list(filter((lambda x: x if x % 2 == 0 else False), numbers))
print(result)  # Output: [4, 2, 8]

print(list(map(lambda x: x ** x, filter((lambda x: x % 2 == 0), numbers))))  # Output: [256, 4, 16777216]

##########################
# Any-All #
##########################
print(all([True, True, True]))  # Output: True

print(all([True, True, False]))  # Output: False

print(any([True, False, False]))  # Output: True

print(any([False, False, False]))  # Output: False

##########################
# Round #
##########################

print(round(10 / 3))  # Output: 3
print(round(10 / 4))  # Output: 2
print(round(10.4))  # Output: 10

print(round(10.4, 1))  # Output: 10.4

print(round(10.4366, 2))  # Output: 10.44
print(round(10.4366, 3))  # Output: 10.437
