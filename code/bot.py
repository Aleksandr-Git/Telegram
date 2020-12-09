import config
import logging
import asyncio
from datetime import datetime
from aiogram import Bot, Dispatcher, executor, types
import keyboards as bk

print(config.API_TOKEN)

API_TOKEN = config.API_TOKEN

#loop = asyncio.get_event_loop()

#инициализация бота и дичпетчера 
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):

    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")

@dp.message_handler(commands=['otvet'])
async def otvet(message: types.Message):
    await message.reply('Ok', reply_markup=bk.greed_kb)
    print('Ok')

@dp.message_handler(commands=['test'])
async def test():
    t = "ASDFGHJKLQWERTYUIOPZXCVBNM"


@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)

    await message.reply(message.text)

#запуск опроса
if __name__ == '__main__':
#    dp.loop.create_task(test())
    executor.start_polling(dp, skip_updates=True)