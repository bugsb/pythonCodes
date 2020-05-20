from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")
bsObj = BeautifulSoup(html,"html5lib")
for link in bsObj.find("div", {"id":"bodyContent"}).findAll("a",
href=re.compile("^(/wiki/)((?!:).)*$")):
    #print(link.attrs)
    if 'href' in link.attrs:
        print("http://en.wikipedia.org"+link.attrs['href'])