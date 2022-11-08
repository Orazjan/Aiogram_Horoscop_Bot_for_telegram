import requests
from bs4 import BeautifulSoup

header = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"
}


def GetData(horoscop, url):
    otwet = ''
    data = ''
    lists = []

    req = requests.get(url, headers=header)

    soup = BeautifulSoup(req.text, "html.parser")

    for itemdata in soup.find_all(class_="link__text"):
        lists.append(itemdata.text)
        data = lists[0]

    for item in soup.find_all(class_="article__item article__item_alignment_left article__item_html"):
        print(item.text)
        otwet = item.text
    return data + " " + horoscop + otwet


def Oven(days):
    url = f"https://horo.mail.ru/prediction/aries/{days}/"
    return GetData("♈️Овен:\n\n", url)


def Telec(days):
    url = f"https://horo.mail.ru/prediction/taurus/{days}/"
    return GetData("♉️Телец:\n\n", url)


def Bliznecy(days):
    url = f"https://horo.mail.ru/prediction/gemini/{days}/"
    return GetData("♊️Близнецы:\n\n", url)


def Rak(days):
    url = f"https://horo.mail.ru/prediction/cancer/{days}/"
    return GetData("♋️Рак:\n\n", url)


def Lev(days):
    url = f"https://horo.mail.ru/prediction/leo/{days}/"
    return GetData("♌️Лев:\n\n", url)


def Deva(days):
    url = f"https://horo.mail.ru/prediction/virgo/{days}/"
    return GetData("♍️Дева:\n\n", url)


def Vesy(days):
    url = f"https://horo.mail.ru/prediction/libra/{days}/"
    return GetData("♎️Весы:\n\n", url)


def Scorp(days):
    url = f"https://horo.mail.ru/prediction/scorpio/{days}/"
    return GetData("♏️Скорпион:\n\n", url)


def Strelec(days):
    url = f"https://horo.mail.ru/prediction/sagittarius/{days}/"
    return GetData("♐️Стрелец:\n\n", url)


def Kozerog(days):
    url = f"https://horo.mail.ru/prediction/capricorn/{days}/"
    return GetData("♑️Козерог:\n\n", url)


def Vodoley(days):
    url = f"https://horo.mail.ru/prediction/aquarius/{days}/"
    return GetData("♒️Водолей:\n\n", url)


def Ryby(days):
    url = f"https://horo.mail.ru/prediction/pisces/{days}/"
    return GetData("♓️Рыбы:\n\n", url)
