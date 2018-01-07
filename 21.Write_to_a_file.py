from bs4 import BeautifulSoup
import requests

site = requests.get('http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture')
page = BeautifulSoup(site.text, 'html.parser')

file_name = input('Save file as: ')
with open(file_name + '.txt', 'w') as open_file:
    for lines in page.find_all('p'):
        open_file.write(lines.getText())
