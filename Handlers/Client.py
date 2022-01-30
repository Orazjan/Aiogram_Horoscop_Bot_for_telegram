from aiogram import types
from Token import bot
from aiogram import Dispatcher
from KeyBoards.Keyboard_Client import Keybord
import Handlers.Otwety as Otwety

async def start_sms(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, Otwety.Start_command(), reply_markup=Keybord)
        
    except:
        await message.reply("Общение через ЛС.\nБот @AlijoomBot",)

async def help_sms(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, Otwety.help_answer())
        
    except:
        await message.reply("Общение через ЛС.\nБот @AlijoomBot",)

async def Otwet(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, Otwety.luboy_answer(message.text))

    except:
        await message.reply("Общение через ЛС.\nБот @AlijoomBot")

def register_Handler_Client(dp : Dispatcher):
    dp.register_message_handler(start_sms, commands=['start'])
    dp.register_message_handler(help_sms, commands=['help'])
    dp.register_message_handler(Otwet)
