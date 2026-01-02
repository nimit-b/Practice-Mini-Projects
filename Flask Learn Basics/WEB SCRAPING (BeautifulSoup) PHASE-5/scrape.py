import requests
from bs4 import BeautifulSoup
url = "https://example.com"
response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, 'html.parser')
title = soup.find('h1')
links = soup.find_all('a')

for link in links:
    print(link.text,'=>', link.get('href'))

print(title.text)
