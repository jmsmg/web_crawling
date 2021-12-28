import requests
from bs4 import BeautifulSoup

# 대상 url
URL = 'https://kr.indeed.com/취업?q=python&limit=50'


def extract_indeed_pages():
    # url 요청
    response = requests.get(URL)

    # 요청 받은 url에서 html문서만 추출
    html = response.text

    # html 파싱
    html = BeautifulSoup(html, 'html.parser')

    # 페이지 넘기
    pagination = html.find("ul", {"class" : "pagination-list"})

    links = pagination.find_all("a")

    pages = []
    for link in links[:-1]:
        pages.append(int(link.string))

    max_page = pages[-1]
    return max_page