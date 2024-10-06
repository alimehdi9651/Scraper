import requests
from bs4 import BeautifulSoup
with open('sample.html', 'r') as f:
    html_doc = f.read()
soup = BeautifulSoup(html_doc, 'html.parser')
# print(soup.prettify())
# print(soup.title)
# print(soup.title.string)
# print(soup.p)
# print(soup.p['paratag'])
# print(soup.find_all('div')) 
# print(soup.div.get_text)
# print(soup.select('div.italic'))
# print(soup.div.get('class'))
# print(soup.find(id = "italic"))
# print(soup.find(class_ = "italic"))
# print(soup.find_all(class_ = "italic")[2])
# for child in soup.find(class_ = 'container').children:
#     print(child)

# for parent in soup.find(class_ = 'box').parents:
#     print(parent)
# cont = soup.find(class_ = "container")

# cont.name = "span"
# # print(cont)
# cont['class'] = "contain"
# print(cont)


# insert new tags

ultag = soup.new_tag('ul')
litag = soup.new_tag('li')
litag.string = 'home'
ultag.append(litag)
soup.html.body.insert(0, ultag)
with open('modified.html', 'w') as f:
    f.write(str(soup))