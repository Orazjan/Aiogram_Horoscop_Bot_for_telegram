from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb1 = KeyboardButton("Овен")
kb2 = KeyboardButton("Телец")
kb3 = KeyboardButton("Близнецы")
kb4 = KeyboardButton("Рак")
kb5 = KeyboardButton("Лев")
kb6 = KeyboardButton("Дева")
kb7 = KeyboardButton("Весы")
kb8 = KeyboardButton("Скорпион")
kb9 = KeyboardButton("Стрелец")
kb10 = KeyboardButton("Козерог")
kb11 = KeyboardButton("Водолей")
kb12 = KeyboardButton("Рыбы")

Keybord = ReplyKeyboardMarkup(resize_keyboard=True)
Keybord.add(kb1, kb2, kb3).add(kb4, kb5, kb6).add(
    kb7, kb8, kb9).add(kb10, kb11, kb12)
