import requests
from bs4 import BeautifulSoup

url = 'https://kr.indeed.com/취업?q=python&limit=50'

response = requests.get(url)
html = response.text

html = BeautifulSoup(html, 'html.parser')

pagination = html.find("ul", {"class" : "pagination-list"})

pages = pagination.find_all("span")

spans = []

for page in pages:
    spans.append(page)
print(type(pages))
print(type(spans))
# print(spans[:4])