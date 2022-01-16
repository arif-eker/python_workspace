#
#

class Comment:
    def __init__(self, name_="Default name", text_="Default text", age_=0):
        self.name = name_
        self.text = text_
        self.age = age_


comment_1 = Comment()

comment_2 = Comment("Arif", "Hello world!", 24)

comment_3 = Comment("Mehmet", "No comment")

comments = [comment_1, comment_2, comment_3]

for com in comments:
    print(f"\nName : {com.name}\n"
          f"Text : {com.text} Type : {type(com.text)}\n"
          f"Age : {com.age} Type : {type(com.age)}")


# Name : Default name
# Text : Default text Type : <class 'str'>
# Age : 0 Type : <class 'int'>

# Name : Arif
# Text : Hello world! Type : <class 'str'>
# Age : 24 Type : <class 'int'>

# Name : Mehmet
# Text : No comment Type : <class 'str'>
# Age : 0 Type : <class 'int'>