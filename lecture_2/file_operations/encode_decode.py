#
#

my_str = "abcçşü"

encode_my_str = my_str.encode("utf-8")

print(encode_my_str)  # b'abc\xc3\xa7\xc5\x9f\xc3\xbc'

print(encode_my_str.decode("utf-8"))  # abcçşü

print(encode_my_str.decode("cp1250"))  # abcĂ§ĹźĂĽ
