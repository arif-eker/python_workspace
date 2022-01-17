#
#
# topic numbers = [1, 2, 3, 4, 5]
# CTRL + F and enter --topic number-- for jump topic to topic
# for example "--5--"

#########################################################################################################################################################
# Topic: --1--

my_set = {4, 5, 1, 2, 3, 6, 1, 2, 3}
print(my_set)

my_list = ["a", "b", "c", "a"]
my_set = set(my_list)
print(my_set)

#########################################################################################################################################################
# Topic: --2--

set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

# Union
print(set_a | set_b)  # {1, 2, 3, 4, 5, 6, 7, 8}

# Intersection
print(set_a & set_b)  # {4, 5}

# Difference
print(set_a - set_b)  # {1, 2, 3}
print(set_b - set_a)  # {8, 6, 7}

# Symmetric Difference
print(set_a ^ set_b)  # {1, 2, 3, 6, 7, 8}  >>>>>>> union - intersection = (a | b) - (a & b)

#########################################################################################################################################################
# Topic: --3--

set_a = {1, 2, 3, 4}

set_a.add(5)
print(set_a)  # {1, 2, 3, 4, 5}

set_b = {3, 4, 5, 6}

set_a.update(set_b)
print(set_a)  # {1, 2, 3, 4, 5, 6}

set_b.clear()
print(set_b)  # set()

set_a.discard(1)
print(set_a)  # {2, 3, 4, 5, 6}
set_a.discard(1)  # no error

set_a.remove(2)
print(set_a)  # {3, 4, 5, 6}
set_a.remove(2)  # KeyError: 2

print(set_a)  # {3, 4, 5, 6}
pop_value = set_a.pop()
print(set_a)  # {4, 5, 6}
print(pop_value)  # 3

#########################################################################################################################################################
# Topic: --4--

set_a = {1, 2, 3, 4, 5}
set_b = {3, 4, 5, 6, 7}
set_c = {1, 2, 3}
set_d = {11, 12, 13}

print(set_a.isdisjoint(set_c))  # False
print(set_a.isdisjoint(set_d))  # True

print(set_a.issubset(set_c))  # False
print(set_c.issubset(set_a))  # True

print(set_a.issuperset(set_c))  # True
print(set_c.issuperset(set_a))  # False

#########################################################################################################################################################
# Topic: --5--

set_a = {1, 2}
set_b = {3, 4}

print(set_a.union(set_b))  # {1, 2, 3, 4}

#

set_a = {1, 2, 3}
set_b = {2, 3, 4}

result = set_a.difference(set_b)
print(result)  # {1}

set_a.difference_update(set_b)
print(set_a)  # {1}

#

set_a = {1, 2, 3}
set_b = {2, 3, 4}

result = set_a.intersection(set_b)
print(result)  # {2, 3}

set_a.intersection_update(set_b)
print(set_a)  # {2, 3}

#

set_a = {1, 2, 3}
set_b = {2, 3, 4}

result = set_a.symmetric_difference(set_b)
print(result)  # {1, 4}

set_a.symmetric_difference_update(set_b)
print(set_a)  # {1, 4}
