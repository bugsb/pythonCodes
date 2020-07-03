from bs4 import BeautifulSoup
import requests

req = requests.get("https://codewithharry.com/videos/")

soup = BeautifulSoup(req.text, 'html.parser')
c = 1
for i in soup.find_all('h2'):
    print(f"{c}.] {i.text}")
    c += 1
