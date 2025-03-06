from aiogram import Bot, Dispatcher, executor, types
from tokn import *

bot = Bot(TELEGRAM_TOKEN)
dp = Dispatcher()
START_MESSAGE = "СоСал!"

@dp.message_handler(comannds=["start"])
async def start_message(message: type.Message) -> type.Message:
    await message.reply(START_MESSAGE)
        
@dp.message_handler()
async def send_message(message: type.Message) -> type.Message:
    await message.reply()

start_message()