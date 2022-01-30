import requests
from bs4 import BeautifulSoup

otwet = ''
data = ''
lists = []

header = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"
}

def Oven():
    url = "https://horo.mail.ru/prediction/aries/today/"
    return GetData("♈️Овен:\n\n", url)

def Telec():
    url = "https://horo.mail.ru/prediction/taurus/today/"
    return GetData("♉️Телец:\n\n", url)

def Bliznecy():
    url = "https://horo.mail.ru/prediction/gemini/today/"
    return GetData("♊️Близнецы:\n\n", url)

def Rak():
    url = "https://horo.mail.ru/prediction/cancer/today/"
    return GetData("♋️Рак:\n\n",url)

def Lev():
    url = "https://horo.mail.ru/prediction/leo/today/"
    return GetData("♌️Лев:\n\n",url)

def Deva():
    url = "https://horo.mail.ru/prediction/virgo/today/"
    return GetData("♍️Дева:\n\n",url)

def Vesy():
    url = "https://horo.mail.ru/prediction/libra/today/"
    return GetData("♎️Весы:\n\n", url)

def Scorp():
    url = "https://horo.mail.ru/prediction/scorpio/today/"
    return GetData("♏️Скорпион:\n\n",url)

def Strelec():
    url = "https://horo.mail.ru/prediction/sagittarius/today/"
    return GetData("♐️Стрелец:\n\n", url)

def Kozerog():
    url = "https://horo.mail.ru/prediction/capricorn/today/"
    return GetData("♑️Козерог:\n\n", url)

def Vodoley():
    url = "https://horo.mail.ru/prediction/aquarius/today/"
    return GetData("♒️Водолей:\n\n",url)

def Ryby():
    url = "https://horo.mail.ru/prediction/pisces/today/"
    return GetData("♓️Рыбы:\n\n", url)

def GetData(horoscop, url):
    req = requests.get(url, headers=header)

    soup = BeautifulSoup(req.text, "html.parser")

    for itemdata in soup.find_all(class_="link__text"):
        lists.append(itemdata.text)
        data = lists[0]

    for item in soup.find_all(class_="article__item article__item_alignment_left article__item_html"):
        print(item.text)
        otwet = item.text
    return data + " " + horoscop + otwet
