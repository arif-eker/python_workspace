#
#
#

from bs4 import BeautifulSoup

with open("D:\\my_projects\\pycharms\\python_workspace\\lecture_1\\web_scraping\\index.html") as file:
    html_doc = file.read()

doc = BeautifulSoup(html_doc, "html.parser")

doc.find("div")  # find first div element

div_list = doc.find_all("div")  # find all elements, return in list

type(div_list[0])  # <class 'bs4.element.Tag'>
div_list[0]
# <div>
# <h3>Menu 1</h3>
# <h3>Menu 2</h3>
# <h3>Menu 3</h3>
# </div>

div_list[0].h3  # <h3>Menu 1</h3>
h3_list = div_list[0].find_all("h3")
h3_list  # [<h3>Menu 1</h3>, <h3>Menu 2</h3>, <h3>Menu 3</h3>]

h3_list[0].string  # Menu 1
h3_list[1].string  # Menu 2