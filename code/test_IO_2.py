import config
import logging
import asyncio
from datetime import datetime
from aiogram import Bot, Dispatcher, executor, types
import keyboards as bk
import serial
import os

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

async def Con_ser():
    global CONNECT, ser

    if os.name == 'posix':  # если linux
        ser = serial.Serial('/dev/ttyUSB0')  # подключаемся к COM порту

    if os.name == 'nt':  # если windows
        ser = serial.Serial('COM4', 9600, timeout=1)  # подключаемся к COM порту

    print(ser.name)  # печатаем номер COM порта

async def Alarm(wait_for):  # проверяет данные с COM порта и отправляет сообщения на почту
    while True:
        await asyncio.sleep(wait_for)
        global DATA

        DATA = ser.readline()  # читаем строку с COM порта
        print(DATA)
#    for i, j in dict_Alarm.items():  # перебираем словарь с сообщениями
#        if DATA.decode().rstrip() == i:  # если даные с COM порта есть в словаре сообщений
#            print(j[0])  # для тестов


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(test(10))
    loop.create_task(Con_ser())
    loop.create_task(Alarm(5))
    executor.start_polling(dp, skip_updates=True)
