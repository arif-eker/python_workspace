#
#
# topic numbers = [1, 2, 3]
# CTRL + F and enter --topic number-- for jump topic to topic
# for example "--5--"

# topics list:

# abspath, dirname, exists, expanduser, isdir, isfile,
# join, split, splitext, splitdrive


import os.path as path

#########################################################################################################################################################
# Topic: --1--

# abspath
path.abspath(".")  # 'D:\\my_projects\\pycharms\\python_workspace'
path.abspath("..")  # D:\\my_projects\\pycharms'

# dirname
path.dirname('D:\\my_projects\\pycharms\\python_workspace')  # 'D:\\my_projects\\pycharms'

# exists : Return true or false
path.exists(r"D:\my_projects\pycharms\python_workspace\lecture_2\modules\path_module\path_module.py")  # True

path.exists(r"D:\my_projects\pycharms\python_workspace\lecture_2\modules\path_module")  # True

# expanduser
path.expanduser("~")  # 'C:\\Users\\arife'

#########################################################################################################################################################
# Topic: --2--

# isdir : return true if it is folder
path.isdir(r"D:\my_projects\pycharms\python_workspace\lecture_2\modules\path_module\path_module.py")  # False
path.isdir(r"D:\my_projects\pycharms\python_workspace\lecture_2\modules\path_module")  # True

# isfile : return true if it is file
path.isfile(r"D:\my_projects\pycharms\python_workspace\lecture_2\modules\path_module\path_module.py")  # True
path.isfile(r"D:\my_projects\pycharms\python_workspace\lecture_2\modules\path_module")  # False

# join : create a path
print(path.join("D:\\", "my_projects", "pycharms", "python_workspace"))  # D:\my_projects\pycharms\python_workspace

#########################################################################################################################################################
# Topic: --3--

# split : return tuple
path.split(r"D:\my_projects\pycharms\python_workspace\lecture_2\modules\path_module\path_module.py")
# ('D:\\my_projects\\pycharms\\python_workspace\\lecture_2\\modules\\path_module', 'path_module.py')

path.split(r"D:\my_projects\pycharms\python_workspace\lecture_2\modules\path_module")
# ('D:\\my_projects\\pycharms\\python_workspace\\lecture_2\\modules', 'path_module')

#

# splitext : return file extention
path.splitext(r"D:\my_projects\pycharms\python_workspace\lecture_2\modules\path_module\path_module.py")
# ('D:\\my_projects\\pycharms\\python_workspace\\lecture_2\\modules\\path_module\\path_module', '.py')

mypath = r"D:\my_projects\pycharms\python_workspace\lecture_2\modules\path_module\path_module.py"
print(path.splitext(path.split(mypath)[1])[1])  # .py

# splitdrive
path.splitdrive(mypath)
# ('D:', '\\my_projects\\pycharms\\python_workspace\\lecture_2\\modules\\path_module\\path_module.py')
