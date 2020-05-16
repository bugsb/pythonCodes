from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from urllib.error import HTTPError
def fetchTitle(url):
    try:
        url = urlopen(url)
    except HTTPError:
        return None

    try:
        bsObj = bs(url.read(),features="html5lib")
    except AttributeError:
        return None
    return bsObj.title

title = fetchTitle(url="http://www.pythonscraping.com/exercises/exercise1.html")

print(title.get_text())