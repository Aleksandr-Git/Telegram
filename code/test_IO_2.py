import config
import logging
import asyncio
from datetime import datetime
from aiogram import Bot, Dispatcher, executor, types
import keyboards as bk

logging.basicConfig(level=logging.INFO)

API_TOKEN = config.API_TOKEN
MY_ID = config.MY_ID

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):

    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.", reply_markup=bk.greed_kb)

async def test(wait_for):
    while True:
        await asyncio.sleep(wait_for)

        now = datetime.utcnow()
        await bot.send_message(MY_ID, f"{now}", disable_notification=True)
        #await bot.send_message(f"{now}")

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(test(10))
    executor.start_polling(dp, skip_updates=True)