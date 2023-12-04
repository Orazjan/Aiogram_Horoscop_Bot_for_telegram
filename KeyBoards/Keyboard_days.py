from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb1 = KeyboardButton("Вчера")
kb2 = KeyboardButton("Сегодня")
kb3 = KeyboardButton("Завтра")
kb4 = KeyboardButton("Неделя")
kb5 = KeyboardButton("Месяц")
kb6 = KeyboardButton("2023")
kb7 = KeyboardButton("2024")


Keybday = ReplyKeyboardMarkup(resize_keyboard=True)
Keybday.add(kb1, kb2, kb3).add(kb4, kb5, kb6, kb7)
