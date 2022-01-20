#
#
# topic numbers = [1, 2, 3]
# CTRL + F and enter --topic number-- for jump topic to topic
# for example "--5--"

# topics list:

#########################################################################################################################################################
# Topic: --1--

import random as rnd

# random : Generates a float number between 0-1
print(rnd.random())

# seed : assigns an initial value to the number generator, the first generated number is always the same.
rnd.seed(45)
print(rnd.random())  # 0.2718754143840908
rnd.seed(45)
print(rnd.random())  # 0.2718754143840908

# randint : Generates an integer between two values
print(rnd.randint(3, 10))  # 4

# randrange : Generates an integer between two values
print(rnd.randrange(start=3, stop=10, step=2))

# choice:
numbers = [1, 2, 3, 4, 5]
chars = ["a", "b", "c", "d", "e"]
name = "Python"

print(rnd.choice(numbers))  # 5
print(rnd.choice(numbers))  # 3

print(rnd.choice(chars))  # c
print(rnd.choice(chars))  # b

print(rnd.choice(name))  # P

# choices
print(rnd.choices(numbers, k=10))  # [4, 2, 1, 3, 1, 2, 2, 4, 3, 2]

# shuffle : changes the places of the given list elements
print(numbers)  # [1, 2, 3, 4, 5]
rnd.shuffle(numbers)
print(numbers)  # [5, 3, 1, 4, 2]

# sample : allows to pull subsets from the population
print(rnd.sample(numbers, k=2))  # [2, 3]
print(rnd.sample(numbers, k=2))  # [2, 4]

print(rnd.sample(numbers, k=7))  # ValueError: Sample larger than population or is negative

numbers = [1, 2, 3, 4, 5, 5, 5]
print(rnd.sample(numbers, k=7))  # [5, 5, 2, 3, 5, 4, 1]
