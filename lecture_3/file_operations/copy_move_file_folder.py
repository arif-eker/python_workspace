#
#
#

import shutil

path = r"D:\my_projects\pycharms\python_workspace\lecture_3\file_operations"

# copy file
source_file = path + r"\origin_file.txt"
copy_file = path + r"\copy_file.txt"

shutil.copy(source_file, copy_file)  # worked!

# copy folder
source_folder = path + r"\origin_folder"
copy_folder = path + r"\copy_folder"
shutil.copytree(source_folder, copy_folder)  # worked!

# move folder or file
shutil.move(source_file, source_folder)  # origin_file.txt move to origin_folder
shutil.move(source_folder, copy_folder)  # then origin_folder move to copy_folder
