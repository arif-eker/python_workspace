#
#
#

path = r"D:\my_projects\pycharms\python_workspace\lecture_2\file_operations\binary_files"

# Write
my_str = "abçşü"
encode_str = my_str.encode("utf-8")

file = open(path + r"\my_bin.bin", "bw+")
file.write(encode_str)
file.close()

# Read
file = open(path + r"\my_bin.bin", "br")
data = file.read()
print(data)  # b'ab\xc3\xa7\xc5\x9f\xc3\xbc'
file.close()

print(data.decode("utf-8"))  # abçşü
