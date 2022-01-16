#
#

# if you use with, you dont need to use file.close()
with open("D:\\my_projects\\pycharms\\python_workspace\\lecture_1\\file_operations\\txt_files\\myfile.txt") as file:
    for i in file.readlines():
        print(i, end="")

# line1
# line2
# line3
# line4