import requests
from bs4 import BeautifulSoup

url = 'https://ridibooks.com/category/new-releases/2200?order=selling'
response = requests.get(url)
response.encoding = 'utf-8'
html = response.text

soup = BeautifulSoup(html, 'html.parser')

bookservice = soup.select('.title_text')
for no, book in enumerate(bookservice, 1):
  print(no, book.text.strip())
