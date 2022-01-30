from Handlers import Horoscopy

def Start_command():
    return "Приветствую вас в нашем Боте\
        \nПредлагаю вам другой наш проект\nФильмы: @@AlijoomBot"

def help_answer():
    return "Переходите в нашу группу с фильмами\n\
    Там вы найдёте подборки фильмов\n\
        Держи ссылку: https://t.me/Towary_Ineta"

def luboy_answer(message):
    if message == "Овен":
        return Horoscopy.Oven()

    elif message == "Телец":
        return Horoscopy.Telec()

    elif message == "Близнецы":
        return Horoscopy.Bliznecy()

    elif message == "Рак":
        return Horoscopy.Rak()

    elif message == "Лев":
        return Horoscopy.Lev()

    elif message == "Дева":
        return Horoscopy.Deva()

    elif message == "Весы":
        return Horoscopy.Vesy()

    elif message == "Скорпион":
        return Horoscopy.Scropion()

    elif message == "Стрелец":
        return Horoscopy.Strelec()

    elif message == "Козерог":
        return Horoscopy.Kozerog()

    elif message == "Водолей":
        return Horoscopy.Vodoley()

    elif message == "Рыбы":
        return Horoscopy.Ryby()

    else:
        return "Приветствую"
