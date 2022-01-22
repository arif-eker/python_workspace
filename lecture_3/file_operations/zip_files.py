#
#
#

import zipfile

path = r"D:\my_projects\pycharms\python_workspace\lecture_3\file_operations"
zip_file = path + r"\hello.zip"
hello = zipfile.ZipFile(zip_file, "r")

print(hello)
# <zipfile.ZipFile filename='D:\\my_projects\\pycharms\\python_workspace\\lecture_3\\file_operations\\hello.zip' mode='r'>

type(hello)  # <class 'zipfile.ZipFile'>

hello.NameToInfo  # {'hello.txt': <ZipInfo filename='hello.txt' compress_type=deflate external_attr=0x20 file_size=40 compress_size=39>}
hello.NameToInfo.keys()  # dict_keys(['hello.txt'])

for file in hello.filelist:
    print(file)  # <ZipInfo filename='hello.txt' compress_type=deflate external_attr=0x20 file_size=40 compress_size=39>

hello.extractall(path=path)

hello.open(hello.filelist[0], "r").readlines()

hello.close()
