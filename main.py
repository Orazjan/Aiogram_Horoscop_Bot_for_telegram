from aiogram import Bot
from aiogram.utils import executor
from Token import dp
from datetime import datetime
from Handlers import Client
import logging

logging.basicConfig(level=logging.INFO)
current_datetime = datetime.now().time()

Client.register_Handler_Client(dp)

#Konec bota
executor.start_polling(dp, skip_updates=True)
