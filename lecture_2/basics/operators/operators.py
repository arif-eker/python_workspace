#
#
# topic numbers = [1, 2, 3, 4, 5, 6]
# CTRL + F and enter --topic number-- for jump topic to topic
# for example "--5--"

#########################################################################################################################################################
# Topic: --1--

val = 20
new_val = ~val

print("Value: ", val, "Ones' complement: ", new_val)  # Value:  20 Ones' complement:  -21

#########################################################################################################################################################
# Topic: --2--

val_1 = 14
val_2 = 4

print(pow(2, 5))  # 32
print(pow(val_1, val_2))  # 38416

print(divmod(val_1, val_2))  # (3, 2)

print(abs(-5))  # 5

print(round(2.35))  # 2
print(round(2.55))  # 3
print(round(2.5567, 3))  # 2.557

#########################################################################################################################################################
# Topic: --3--

a = 1
b = 1
print(a == b)  # True
print(a != b)  # False
print(a > b)  # False
print(a < b)  # False

#########################################################################################################################################################
# Topic: --4--

# Bitwise
a = 0b_00_00_00_11
print(a)  # 3

# shifting 1 bit to the left means multiplying the number by 2.

b = a << 4  # shifts left 4 bits
# ------>  3*2*2*2*2 = 48
print(bin(b))  # 0b110000   -----> 0b__11_00_00_00
print(b)  # 48

c = b >> 3  # ------>  48/2/2/2
print(c)  # 6
print(bin(c))  # 0b110   ------> 0b_00_00_01_10

#########################################################################################################################################################
# Topic: --5--

a = 2
a <<= 4
print(a)  # 32

b = 3
c = 24
c &= b
print(c)

d = 5
e = 27
e |= d
print(e)  # 31

#########################################################################################################################################################
# Topic: --6--

my_val_1 = "a"
my_val_2 = "A"
my_val_3 = "a"

print("\nmy_val_1, id value: ", id(my_val_1),
      "\nmy_val_2, id value: ", id(my_val_2),
      "\nmy_val_3, id value: ", id(my_val_3))

str_1 = "M"
str_1 += "y"
str_2 = "My"

print("str_1, id value: ", id(str_1))  # str_1, id value:  2787448782384
print("str_2, id value: ", id(str_2))  # str_2, id value:  2787448780464
print(str_1 is str_2)  # False

#

str_1 = "hello"
str_2 = "hello"

print("str_1, id value: ", id(str_1))  # str_1, id value:  2787437234224
print("str_2, id value: ", id(str_2))  # str_2, id value:  2787437234224
print(str_1 is str_2)  # True

# so, "is" operator looks id values

a = 5
print(type(a) is float)  # False
print(type(a) is int)  # True

b = 5.1
print(type(b) is float)  # True
print(type(b) is int)  # False

c = 510.2
print(type(b) is type(c))  # True
