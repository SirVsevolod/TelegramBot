import ParsFunction
import text
from ParseSub import *
import re

def MM_news(news_link):
    n = ParseNews()
    regex = re.compile(r'[\n\r\t]')
    text = "<a href='" + n.host + str(news_link) + "'>" + str(regex.sub('', n.NewsTitle(news_link))) + "</a>" + '\n\n' + str(regex.sub('', n.GetDescriptionNews(news_link)))
    return text


def MM_Today():
    """Построение сообщения союытия сегодня"""
    news = ParsFunction.parse_today()
    HOST = "http://zelbiblio.ru"
    if len(news) > 0:
        message = "События на сегодня:\n\n"
        for i in range(len(news)):
            a = str(i + 1)
            message = message + a + ')' + "<a href='" + HOST + news[i][1] + "'>" + news[i][0] + "</a>" + '\n\n'
    else:
        message = "На сегодня события отсутствуют"

    return message


def MM_start():
    message = text.start_text
    return message


def MM_contacts():
    message = text.contacts_text
    return message


def MM_adrecc(message):
    if message == 'Савёлки':
        answer = text.adrecc_savelki_text
    elif message == 'Матушкино':
        answer = text.adrecc_matyshkino_text
    elif message == "Крюково":
        answer = text.adrecc_krykovo_text
    elif message == "Силино":
        answer = text.adrecc_silino_text

    return answer

def MM_help():
    message = text.help
    return message