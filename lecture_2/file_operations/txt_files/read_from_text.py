#
#
#

path = r"D:\my_projects\pycharms\python_workspace\lecture_2\file_operations\txt_files"

file = open(path + r"\read_sample.txt", "tr+", encoding="utf-8")

data = file.read()
print(data)
# hello!
# line 2
# line 3
# line 4
# line 5

file.close()

file = open(path + r"\read_sample.txt", "tr+", encoding="utf-8")
data = file.read(3)
print(data)
# hel
file.close()

file = open(path + r"\read_sample.txt", "tr+", encoding="utf-8")
data1 = file.readline()
data2 = file.readline()

print(data1)  # hello!
print(data2)  # line 2

data3 = file.readline(3)
print(data3)  # lin
print(file.readline())  # e 3

file.close()

file = open(path + r"\read_sample.txt", "tr+", encoding="utf-8")
print(file.readlines())  # ['hello!\n', 'line 2\n', 'line 3\n', 'line 4\n', 'line 5\n']
file.close()








