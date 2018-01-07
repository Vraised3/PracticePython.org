from bs4 import BeautifulSoup
import requests

website = 'http://www.practicepython.org/exercise/2014/06/06/17-decode-a-web-page.html'
web_data = requests.get(website)
data = BeautifulSoup(web_data.data)
print(data)
