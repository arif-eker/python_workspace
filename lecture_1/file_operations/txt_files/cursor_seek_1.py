#
#

# use open() method for open or create a file

file = open("D:\\my_projects\\pycharms\\python_workspace\\lecture_1\\file_operations\\txt_files\\myfile.txt")

#
file.read()  # 'line1\nline2\nline3\nline4'
file.read()  # ''
# When you read the file for the first time, the cursor goes all the way to the end and stays there.
# That's why it doesn't read anything when you read it again.

# Therefore, you can move the cursor back to the desired location with the X and read it again.
file.seek(0)  # cursor move to 0. index (character index)
file.read()  # 'line1\nline2\nline3\nline4'

file.seek(3)
file.read()  # 'e1\nline2\nline3\nline4'

# readline() ---> read one line
file.seek(0)
file.readline()  # 'line1\n'
file.readline()  # 'line2\n'

# readlines() ---> read all lines, return lines in list
file.seek(0)
file.readlines()  # ['line1\n', 'line2\n', 'line3\n', 'line4']
file.seek(0)
file.readlines()[2]  # 'line3\n'

file.closed  # False
file.close()  # close file
file.closed  # True
