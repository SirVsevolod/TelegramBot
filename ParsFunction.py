import requests
from bs4 import BeautifulSoup
import datetime

HEADERS = {'user-agent': 'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0', 'accept': '*/*'}


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


#парс календаря на сегодня-------------------------------------------------------------------------------------------
def parse_today():
    today = str(datetime.datetime.today().date()).split('-')

    news_today = []
    href_today = []

    news = []

    day = today[2]
    month = today[1]
    year = today[0]

    URL = "http://zelbiblio.ru/meropriyatiya/?year=" + year + "&month=" + month + "&day=" + day
    html = get_html(URL)
    pages = get_page_count_today(html.text)
    for i in pages:
        html = get_html(url=URL, params={'PAGEN_1': i})
        news_today.extend(get_content_today(html.text))
        href_today.extend(get_href_today(html.text))

    for i in range(len(news_today)):
        news.append([news_today[i], href_today[i]])

    return news


def get_content_today(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('p', class_='news-item')
    #adreccs = soup.find_all('td', class_='news-item')

    news = []

    for item in items:
        news_name = item.find('b',).get_text(strip=True)

        news.append(news_name)

    return news


def get_href_today(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('p', class_='news-item')

    href = []
    for item in items:
        href_today = item.find('a').get('href')

        href.append(href_today)
    return href


def get_page_count_today(html):
    soup = BeautifulSoup(html, 'html.parser')
    pagination = soup.find_all('div', class_='navigation-pages')

    pages = [1]

    if pagination:
        page = pagination[0].find_all('a')
        for i in page:
            pages.append(int(i.get_text()))
        return pages
    else:
        return pages


parse_today()

