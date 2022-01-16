#
#
#

from bs4 import BeautifulSoup

with open("D:\\my_projects\\pycharms\\python_workspace\\lecture_1\\web_scraping\\index.html") as file:
    html_doc = file.read()

doc = BeautifulSoup(html_doc, "html.parser")

id_2 = doc.find(id="div2")
print(id_2)
# <div id="div2">
# <h3>Menu 4</h3>
# <h3>Menu 5</h3>
# <h3>Menu 6</h3>
# </div>


myclass = doc.find(class_="myclass")
print(myclass)
# <div class="myclass" id="div1">
# <h3 class="myclass">Menu 1</h3>
# <h3>Menu 2</h3>
# <h3>Menu 3</h3>
# </div>

div_list = doc.find_all("div")  # shows attributes
print(div_list[0].attrs)  # {'id': 'div1', 'class': ['myclass']}
print(div_list[1].attrs)  # {'id': 'div2'}

print(div_list[0].get("id"))  # div1
print(div_list[0].get("class"))  # ['myclass']
print(div_list[1].get("id"))  # div2


sec = doc.find(attrs={'id': 'div1', 'class': ['myclass']})
print(sec)
# <div class="myclass" id="div1">
# <h3 class="myclass">Menu 1</h3>
# <h3>Menu 2</h3>
# <h3>Menu 3</h3>
# </div>


all_text = doc.get_text()  #
print(all_text)
# My Future
# Hello World!
#  A Computer Science portal for geeks
#     A Computer Science portal for geeks
#     A Computer Science portal for geeks
# Menu 1
# Menu 2
# Menu 3
# Menu 4
# Menu 5
# Menu 6

all_text = doc.get_text(strip=True)  #
print(all_text)
# My FutureHello World!A Computer Science portal for geeksA Computer Science portal for geeksA Computer Science portal for geeksMenu 1Menu 2Menu 3Menu 4Menu 5Menu 6

all_text = doc.get_text(strip=True, separator=',')  #
print(all_text)
# My Future,Hello World!,A Computer Science portal for geeks,A Computer Science portal for geeks,A Computer Science portal for geeks,Menu 1,Menu 2,Menu 3,Menu 4,Menu 5,Menu 6

all_text = doc.get_text(strip=True, separator='\n')  #
print(all_text)
# My Future
# Hello World!
# A Computer Science portal for geeks
# A Computer Science portal for geeks
# A Computer Science portal for geeks
# Menu 1
# Menu 2
# Menu 3
# Menu 4
# Menu 5
# Menu 6
