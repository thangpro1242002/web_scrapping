
from bs4 import BeautifulSoup

from urllib.request import urlopen
textPage = urlopen('http://www.pythonscraping.com/pages/warandpeace/chapter1.txt')
print(textPage.read())

from urllib.request import urlopen
textPage = urlopen(
             'http://www.pythonscraping.com/pages/warandpeace/chapter1-ru.txt')
print(textPage.read())

from urllib.request import urlopen

textPage = urlopen(
             'http://www.pythonscraping.com/pages/warandpeace/chapter1-ru.txt')
print(str(textPage.read(), 'utf-8'))


html = urlopen("http://en.wikipedia.org/wiki/Python_(programming_language)")
bs = BeautifulSoup(html, "html.parser")
content = bs.find("div", {"id":"mw-content-text"}).get_text()
content = bytes(content, "UTF-8")
content = content.decode("UTF-8")
print(content)

