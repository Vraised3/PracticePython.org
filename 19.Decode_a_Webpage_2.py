from bs4 import BeautifulSoup
import requests

res = requests.get('http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture')
soup = BeautifulSoup(res.text)
for lines in soup.find_all('p'):
    print(str(lines.getText()))
