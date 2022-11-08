from Parsering import Parser as Par


def Start_command():
    return "Приветствую вас в нашем Боте\
        \nПредлагаю вам другой наш проект\nФильмы: @@AlijoomBot"


def help_answer():
    return "Переходите в нашу группу с фильмами\n\
    Там вы найдёте подборки фильмов\n\
        Держи ссылку: https://t.me/Towary_Ineta"


def luboy_answer(message, days):
    if message == "Овен":
        return Par.Oven(days)

    elif message == "Телец":
        return Par.Telec(days)

    elif message == "Близнецы":
        return Par.Bliznecy(days)

    elif message == "Рак":
        return Par.Rak(days)

    elif message == "Лев":
        return Par.Lev(days)

    elif message == "Дева":
        return Par.Deva(days)

    elif message == "Весы":
        return Par.Vesy(days)

    elif message == "Скорпион":
        return Par.Scorp(days)

    elif message == "Стрелец":
        return Par.Strelec(days)

    elif message == "Козерог":
        return Par.Kozerog(days)

    elif message == "Водолей":
        return Par.Vodoley(days)

    elif message == "Рыбы":
        return Par.Ryby(days)

    else:
        return "Хуйня короче"
