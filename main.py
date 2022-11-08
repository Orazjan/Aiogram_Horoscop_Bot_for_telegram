from datetime import datetime
import logging
from aiogram.utils import executor
from Handlers.Client import dp
from Handlers import Client

logging.basicConfig(level=logging.INFO)
current_datetime = datetime.now().time()

Client.register_Handler_Client(dp)

#Konec bota
executor.start_polling(dp, skip_updates=True)
