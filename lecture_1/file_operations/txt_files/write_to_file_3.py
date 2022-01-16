#
#

# "w" : write mode
# create a new file
# If there is a file with the same name, it deletes that file and creates it again.

file = open("D:\\my_projects\\pycharms\\python_workspace\\lecture_1\\file_operations\\txt_files\\myfile2.txt", "w", encoding="utf-8")

file.write("hello world!\n")
file.write("My name is Arif.\n")
file.close()

