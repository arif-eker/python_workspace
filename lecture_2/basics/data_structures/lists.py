#
#
# topic numbers = [1, 2, 3, 4, 5, 6]
# CTRL + F and enter --topic number-- for jump topic to topic
# for example "--5--"

#########################################################################################################################################################
# Topic: --1--

# Reference type example:

list_a = [10, 20, 30]
list_b = list_a
list_c = list_a.copy()

print(list_a)  # [10, 20, 30]
print(list_b)  # [10, 20, 30]
print(list_c)  # [10, 20, 30]

print("List A's Memory Address: ", id(list_a))  # List A's Memory Address:  2_838_621_861_832
print("List B's Memory Address: ", id(list_b))  # List B's Memory Address:  2_838_621_861_832
print("List C's Memory Address: ", id(list_c))  # List C's Memory Address:  2_838_621_867_848

list_b[0] = 48
list_c[2] = 75

print(list_a)  # [48, 20, 30]
print(list_b)  # [48, 20, 30]
print(list_c)  # [10, 20, 75]

# list_a and list_b have the same memory address, so a change to one affects the other.
# But list_c's memory address is different. Because it was created with the copy() method.
# So the changes don't affect list_c.


#########################################################################################################################################################
# Topic: --2--

numbers = [1, 3, 7, 5, 10]
mixed = [1, 3, 7, 5, 10, "a"]

print(min(numbers))  # 1
print(max(numbers))  # 10

print(min(mixed, key=str))  # 1
print(max(mixed, key=str))  # a

mixed2 = [1, 3, 7, 5, 10, "a", "ab", "abc", "abb", "acb"]
print(min(mixed2, key=str))  # 1
print(max(mixed2, key=str))  # acb

print(ord("xyz"))

#########################################################################################################################################################
# Topic: --3--

numbers = [1, 2, 3]
print(sum(numbers))  # 6
print(sum(numbers, 100))  # 106

numbers = [1, 3, 2, 4, 7]
print(sorted(numbers))  # [1, 2, 3, 4, 7]
print(numbers)  # [1, 3, 2, 4, 7]

print(sorted(numbers, reverse=True))  # [7, 4, 3, 2, 1]

#########################################################################################################################################################
# Topic: --4--

numbers1 = [4, 5, 6]
numbers2 = [1, 2, 3]

print(numbers1)  # [4, 5, 6]

numbers1.append(7)
print(numbers1)  # [4, 5, 6, 7]

print(numbers1[2])  # 6
print(numbers1[3])  # 7

numbers1.insert(2, 8)
print(numbers1[2])  # 8
print(numbers1[3])  # 6

numbers1.extend(numbers2)
print(numbers1)  # [4, 5, 8, 6, 7, 1, 2, 3]

numbers1.append(1)
numbers1.remove(1)
print(numbers1)  # [4, 5, 8, 6, 7, 2, 3, 1]

numbers1.insert(4, 8)
print(numbers1)  # [4, 5, 8, 6, 8, 7, 2, 3, 1]
numbers1.remove(8)
print(numbers1)  # [4, 5, 6, 8, 7, 2, 3, 1]

numbers1.pop(2)  # delete 2. index value
print(numbers1)  # [4, 5, 8, 7, 2, 3, 1]

numbers1.clear()
print(numbers1)  # []

numbers1 = [1, 3, 2, 4]
numbers1.reverse()
print(numbers1)

numbers1.sort()
print(numbers1)  # [1, 2, 3, 4]
numbers1.sort(reverse=True)
print(numbers1)  # [4, 3, 2, 1]

#########################################################################################################################################################
# Topic: --5--

chars = ["a", "b", "c", "a", "b", "a", "a", "d", "e"]

numbers = [1, 2, 3, 4, 1, 3, 2, 5, 2, 1]
print(chars.count("a"))  # 4
print(chars.count("e"))  # 1
print(chars.count("b"))  # 2

print(numbers.count(1))  # 3
print(numbers.count(10))  # 0

print(chars.index("a"))  # 0
print(chars.index("a", 2))  # 3
print(chars.index("b", 5))  # ValueError: 'b' is not in list
print(chars.index("b"))  # 1

#########################################################################################################################################################
# Topic: --6--

# Unpacking
my_list = ["A", "B", "C", 15]
a, b, c, d = my_list
print(a, b, c, d, sep="-")  # A-B-C-15

my_list = [10, 20, 30, 40, 50, 60]
a, b, *c = my_list
print("a: ", a, "  b: ", b, "  c: ", c)  # a:  10   b:  20   c:  [30, 40, 50, 60]

a, *b, c = my_list
print("a: ", a, "  b: ", b, "  c: ", c)  # a:  10   b:  [20, 30, 40, 50]   c:  60
len(b)  # 4

#
a = []
b = [1, 2, 3]
c = [4, 5, 6]
a = [*b, *c]
print(a)  # [1, 2, 3, 4, 5, 6]

b = [1, 2, 3]
*d, = b  # <------>  d = b.copy()
print(d)  # [1, 2, 3]
