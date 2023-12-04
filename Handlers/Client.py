from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardRemove
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from Handlers import Otwety
from KeyBoards.Keyboard_Client import Keybord
from KeyBoards.Keyboard_days import Keybday
from Token import bot

storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

ReplyKeyboardRemove.remove_keyboard = True


class work_comands(StatesGroup):
    commamnd = State()
    set_secconds = State()


async def help_sms(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, Otwety.help_answer())

    except:
        await message.reply("Общение через ЛС.\nБот @AlijoomBot")


async def menu_work(message: types.Message):
    await work_comands.commamnd.set()
    await bot.send_message(message.from_user.id, "Приветствую вас. Выберите свой знак зодиака", reply_markup=Keybord)


@dp.message_handler(state=work_comands.commamnd)
async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        await state.reset_state()
        data['comandname'] = message.text

    await bot.send_message(message.from_user.id, "Выберите на какой день вам нужен гороскоп: ", reply_markup=Keybday)
    await work_comands.next()

    await work_comands.set_secconds.set()


@dp.message_handler(state=work_comands.set_secconds)
async def set_seconds(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if (message.text == "Вчера"):
            data['set_seccond'] = "yesterday"

        elif message.text == "Сегодня":
            data['set_seccond'] = "today"

        elif message.text == "Завтра":
            data['set_seccond'] = "tomorrow"

        elif message.text == "Неделя":
            data['set_seccond'] = "week"

        elif message.text == "Месяц":
            data['set_seccond'] = "month"

        elif message.text == "2023":
            data['set_seccond'] = "year"

        elif message.text == "2024":
            data['set_seccond'] = "2024"

        await bot.send_message(message.from_user.id, Otwety.luboy_answer(data['comandname'], data['set_seccond']), reply_markup=types.ReplyKeyboardRemove())
    await state.finish()


def register_Handler_Client(dp: Dispatcher):
    dp.register_message_handler(menu_work, commands=['start'])
    dp.register_message_handler(help_sms, commands=['help'])
