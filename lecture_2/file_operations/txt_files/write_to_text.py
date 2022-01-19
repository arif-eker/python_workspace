#
#
#

path = r"D:\my_projects\pycharms\python_workspace\lecture_2\file_operations\txt_files"

file = open(path + r"\sample.txt", "tw+", encoding="utf-8")
file.write("sample 1\n")
file.close()  # worked

#

data = ["123", "456"]
file = open(path + r"\sample_2.txt", "tw+", encoding="utf-8")
file.writelines([line + "\n" for line in data])
file.close()  # worked

#

file = open(path + r"\sample_3.txt", "tw+", encoding="utf-8")
print("hello, writing to txt with print", file=file)
print(r"second line with no \n ...", file=file)
print(data, file=file)
file.close()  # worked

#

file = open(path + r"\sample_4.txt", "tw+", encoding="utf-8")
var1 = 10
var_list = [11, 12, 13, 14, 15]

file.write(var1)  # can't write integers
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
# TypeError: write() argument must be str, not int

# try with print()
print(var1, var_list, file=file)
file.close()
