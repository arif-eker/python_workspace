#
#

# open() file for add a new things. if the file doesn't exist it creates
# always appends to the end
"D:\\my_projects\\pycharms\\python_workspace\\lecture_1\\file_operations\\txt_files\\"
file = open("D:\\my_projects\\pycharms\\python_workspace\\lecture_1\\file_operations\\txt_files\\new_file.txt", "a",
            encoding="utf-8")
file.write("new add a new line with append 'a'\n")
file.close()

# If not specified, update to the beginning. not append, only update! so, it's changing first line :)
file2 = open("D:\\my_projects\\pycharms\\python_workspace\\lecture_1\\file_operations\\txt_files\\new_file.txt", "r+",
             encoding="utf-8")
file2.write("aaa new append new line with 'r+'")
file2.close()

file3 = open("D:\\my_projects\\pycharms\\python_workspace\\lecture_1\\file_operations\\txt_files\\new_file.txt", "a+",
             encoding="utf-8")
file3.write("append new line with 'a+'")
file3.seek(20)
file3.write("seek(20) append new line with 'a+'")
file3.close()
