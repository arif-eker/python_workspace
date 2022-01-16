#
#

from bs4 import BeautifulSoup

with open("D:\\my_projects\\pycharms\\python_workspace\\lecture_1\\web_scraping\\index.html") as file:
    html_doc = file.read()

doc = BeautifulSoup(html_doc, "html.parser")

print(doc.prettify())  # for good print

doc.title  # <title>My Future</title>

doc.title.string  # 'My Future'
