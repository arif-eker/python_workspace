#
#
# topic numbers = [1, 2, 3, 4, 5, 6]
# CTRL + F and enter --topic number-- for jump topic to topic
# for example "--5--"

# topics list:

# cpu_count, name, linesep, sep, altsep, extsep, pathsep, getlogin, environ
# getcwd, getcwdb, chdir, listdir, curdir, pardir, startfile
# mkdir, makedirs, rename, remove, rmdir, removedirs, stat

import os

#########################################################################################################################################################
# Topic: --1--

# cpu_count : Return the number of CPUs in the system.
os.cpu_count()  # 12

# name : Return the name of operating system
print(os.name)  # nt --> windows

# linesep : Returns the end-of-line marker of the operating system
f"{os.linesep}"  # '\r\n'   --> for windows

# sep : Returns the directory separator of the operating system
f"{os.sep}"  # \\'  --> for windows

# altsep : Returns the alternative directory separator of the operating system
f"{os.altsep}"  # '/' --> for windows

# extsep : Returns the file extension token of the operating system
print(os.extsep)  # "."

# pathsep : Returns the marker at the end of file paths in environment variables
print(os.pathsep)  # ";"

# getlogin : Returns the username running python from the command line.
print(os.getlogin())  # arife

#########################################################################################################################################################
# Topic: --2--

# environ : Returns information in environment variables as a dictionary.
# You can get key-value from system variables or add key-value permanently.

environs = os.environ
for key in environs:
    print(key)

# ALLUSERSPROFILE
# APPDATA
# COMMONPROGRAMFILES
# COMMONPROGRAMFILES(X86)
# COMMONPROGRAMW6432 ......

print(environs["NUMBER_OF_PROCESSORS"])  # 12
print(environs["PROCESSOR_IDENTIFIER"])  # Intel64 Family 6 Model 158 Stepping 10, GenuineIntel

#########################################################################################################################################################
# Topic: --3--

# getcwd : get current working directory
print(os.getcwd())  # D:\my_projects\pycharms\python_workspace

# getcwdb : get current working directory bytes
print(os.getcwdb())  # b'D:\\my_projects\\pycharms\\python_workspace'

# chdir : change directory
print(os.getcwd())  # D:\my_projects\pycharms\python_workspace
os.chdir(r"D:\my_projects\pycharms")
print(os.getcwd())  # D:\my_projects\pycharms
os.chdir(r"D:\my_projects\pycharms\python_workspace")

# listdir : Return a list containing the names of the files in the directory.
curr_dir = os.getcwd()
os.listdir(curr_dir)  # ['.git', '.gitignore', '.idea', 'lecture_1', 'lecture_2', 'lecture_info']

os.listdir(curr_dir + r"\lecture_2")
# ['basics', 'exceptions', 'file_operations', 'functions', 'iterators_generators', 'modules', 'oop']

# currdir : current directory marker
os.listdir(os.curdir)  # ['.git', '.gitignore', '.idea', 'lecture_1', 'lecture_2', 'lecture_info']

# pardir
os.listdir(os.pardir)  # ..... other folders....

#########################################################################################################################################################
# Topic: --4--

# startfile : Only works on windows. Runs a file on the computer. --> exe, xlsx, txt etc.
os.startfile("www.google.com")  # opens the google

# mkdir : make one directory
os.mkdir(
    r"D:\my_projects\pycharms\python_workspace\lecture_2\modules\os_module\sample_directory")  # create sample_directory

# makedirs : make some directories
os.makedirs(
    r"D:\my_projects\pycharms\python_workspace\lecture_2\modules\os_module\sample2\sample3")  # create sample2>sample3 directories

os.rename(r"D:\my_projects\pycharms\python_workspace\lecture_2\modules\os_module\sample_directory",
          r"D:\my_projects\pycharms\python_workspace\lecture_2\modules\os_module\sample1")  # worked!

#########################################################################################################################################################
# Topic: --5--

# remove : remove file
os.remove(r"D:\my_projects\pycharms\python_workspace\lecture_2\modules\os_module" + r"deleting_file.txt")

# rmdir : remove directory
os.rmdir(r"D:\my_projects\pycharms\python_workspace\lecture_2\modules\os_module\sample1")  # sample1 removed: worked!

# removedirs : remove directories
os.removedirs(
    r"D:\my_projects\pycharms\python_workspace\lecture_2\modules\os_module\sample2\sample3")  # removes smaple and sample3

#########################################################################################################################################################
# Topic: --6--

# stat

os.stat(os.getcwd())
# os.stat_result(st_mode=16895, st_ino=2814749767130095, st_dev=1117851787, st_nlink=1, st_uid=0,
# st_gid=0, st_size=4096, st_atime=1642636295, st_mtime=1642635784, st_ctime=1642370537)
