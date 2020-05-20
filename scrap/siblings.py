from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("http://www.pythonscraping.com/pages/page3.html")

bsObj = BeautifulSoup(html,'html5lib')

for price in bsObj.findAll("img",{"src":"../img/gifts/img1.jpg"}):
    print(price.parent.previous_sibling.get_text())
for item in bsObj.findAll("tr",{"class":'gift'}):

    print(item.td.get_text())


images = bsObj.findAll("img", {"src":re.compile("\.\.\/img\/gifts/img.*\.jpg")})

for image in images:
    print(image['src'])

# k= bsObj.findAll(lambda tr: len(tr.attrs) == 2)
# print(k)