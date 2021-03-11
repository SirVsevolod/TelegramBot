import requests
from bs4 import BeautifulSoup as BS
"""Получить список новых новостей
ссылки на них 
картинку"""
class ParseNews:
    host = 'http://zelbiblio.ru/'
    url = 'http://zelbiblio.ru/news/'

    lastkay = []
    lastkay_file = ""


    def NewsLink(self):
        # Получение ссылок новостей
        r = requests.get(self.url)
        html = BS(r.content, 'html.parser')
        check = 0

        news_link = []

        items = html.select('.article-content  p a')

        for i in items:

            if check % 2 != 0:
                news_link.append(i.get('href'))

            check = check + 1

        return news_link


    def NewsTitle(self, uri):
        url = self.host + uri
        r = requests.get(url)
        html = BS(r.content, 'html.parser')

        title = html.find('h2').text

        return title


    def GetDescriptionNews(self, uri):
        #Получает описание новости
        url = self.host + uri
        r = requests.get(url)
        html = BS(r.content, 'html.parser')

        Description = html.find('p').text

        return Description


    def NewNewsList(self, news_link):
        news = []
        if self.lastkay:
            for i in range(len(news_link)):
                if news_link[0] != self.lastkay[0]:
                    news.append(news_link[i])
                else:
                    return news
        else:
            news = news_link
            return news


    def NewPoster(self,new):
        r = requests.get(self.url)
        html = BS(r.content, 'html.parser')
        check = 0

        poster_link = []
        news_poster = {}

        links = self.NewsLink()
        items = html.select('.article-content  p a img')
        for i in items:
            poster_link.append(i.get('src'))
        for i in links:
            news_poster[i] = poster_link[check]
            check = check + 1

        return str(self.host + news_poster[new])



        

        


