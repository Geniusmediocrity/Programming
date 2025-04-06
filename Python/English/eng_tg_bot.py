import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart, Command
from aiogram.methods import DeleteWebhook

from settings.tenses import tnss
from settings.config import TELEGRAM_TOKEN



bot = Bot(TELEGRAM_TOKEN)
dp = Dispatcher()    
# DB = DataBase(database="db/DataBase.db") #? коннект с БД


import random
from settings.tenses import tnss


def check_ans(answer: str, task: str) -> bool:
    if answer == task:
        return True


#? Базовые команды:
@dp.message(CommandStart())
async def command_start(message: types.Message):
    """⁡⁢⁣⁣Начало использования"""
    global chat_id
    await message.reply(text="""Hint write ALL the words separated by a <b>space</b>
"If you can use two words in the same form, <i>use: '/'</i>
Write me answers on the questions
If you want to stop print <i>/stop</i>""", parse_mode = 'HTML')
    chat_id = message.chat.id
    message
    
    
@dp.message(Command("stop"))
async def command_start(message: types.Message):
    perc = round((correct / all_questions) * 100, 1)
    await message.reply(text=f"""There were only a few questions: <i>{all_questions}</i>
Correct answers: <i>{correct}</i>
Incorrect answers: <i>{incorrect}</i>
Percentage of correct answers: <i>{perc}</i>""", parse_mode="HTML")
    

dp.message(lambda message: message.text)
async def words_hadler(message: types.Message):
    global correct, incorrect, all_questions
    
    while tnss:
        rus_f = random.choice(list(tnss.keys()))
        task = " ".join(tnss[rus_f])
        await bot.send_message(chat_id=chat_id, text=f"Your word:\n{rus_f}")
        
        answer = input("Enter three irregular verb forms: to ")
        if check_ans(answer, task):
            await message.reply("Success")
            del tnss[rus_f]
            correct += 1
        else:
            await message.reply((f"Wrong answer:\nYour answer:  {answer}\nRight answer: {task}"), parse_mode="HTML")
            incorrect += 1
        all_questions += 1


async def main():
    """Главный скрипт"""
    await bot(DeleteWebhook(drop_pending_updates=True))
    await dp.start_polling(bot)

if __name__ == "__main__":
    correct, incorrect, all_questions = 0, 0, 0
    chat_id = 0
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())