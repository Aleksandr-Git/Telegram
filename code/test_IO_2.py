import config
import logging
import asyncio
from datetime import datetime
from aiogram import Bot, Dispatcher, executor, types
import keyboards as kb
import serial
import os

logging.basicConfig(level=logging.INFO)

API_TOKEN = config.API_TOKEN
MY_ID = config.MY_ID

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

dict_Alarm = {'Alarm_0': ['\n ТРЕВОГА!!! Датчик №0 (левый)'],
              'Alarm_1': ['\n ТРЕВОГА!!! Датчик №1 (левый)'],
              'Alarm_2': ['\n ТРЕВОГА!!! Датчик №2 (правый)'],
              'Alarm_3': ['\n ТРЕВОГА!!! Датчик №3 (правый)'],
              'Norma_0': ['\n Возврат в НОРМУ!!! Датчик №0 (левый)'],
              'Norma_1': ['\n Возврат в НОРМУ!!! Датчик №1 (левый)'],
              'Norma_2': ['\n Возврат в НОРМУ!!! Датчик №2 (правый)'],
              'Norma_3': ['\n Возврат в НОРМУ!!! Датчик №3 (правый)'],
              'Alarm_D0': ['\n Сработала ситема защиты от протечки!'],
              'Alarm_D1': ['\n Отключение электропитания в вводном щите!'],
              'Alarm_D2': ['\n Сработал датчик движения!'],
              'Alarm_D3': ['\n Переход на резервное электропитание!'],
              'Norma_D0': ['\n Возврат в НОРМУ системы защиты от протечки!'],
              'Norma_D1': ['\n Восстановление электропитания в водном щите!'],
              'Norma_D3': ['\n Восстановление основного электропитания!'],
              'Mode_M': ['\n Режим мониторинга!'],
              'Mode_A': ['\n Постановка на охрану!'],
              'ERROR_Mode_A': ['\n Не удалось поставить на охрану! Датчик движения в режиме тревоги!']
              }

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
#    print(DATA.decode().rstrip())
#    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.", reply_markup=kb.greed_kb)
    await message.reply(DATA.decode().rstrip(), reply_markup=kb.greed_kb)

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

async def Alarm():  # проверяет данные с COM порта и отправляет сообщения на почту
    global DATA
    while True:
#        await asyncio.sleep(wait_for)
#        global DATA
        await asyncio.sleep(0)
        DATA = ser.readline()  # читаем строку с COM порта
        try:
#            await send()
#            print(DATA.decode().rstrip())
            for i, j in dict_Alarm.items():
                if DATA.decode().rstrip() == i:

# аргументы: кому отправить, текст сообщения ...
                    await bot.send_message(MY_ID, j[0], disable_notification=True)
                    print(j[0])

        except UnicodeDecodeError:
            continue
#        print(DATA.decode('utf-8'))
#        print(DATA)
#    for i, j in dict_Alarm.items():  # перебираем словарь с сообщениями
#        if DATA.decode().rstrip() == i:  # если даные с COM порта есть в словаре сообщений
#            print(j[0])  # для тестов


#def send():
#    for i, j in dict_Alarm.items():
#        if DATA.decode().rstrip() == i:

# аргументы: кому отправить, текст сообщения ...
#            bot.send_message(MY_ID, j[0], disable_notification=True)
#            print(j[0])

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
#    loop.create_task(test(10))
    loop.create_task(Con_ser())
    loop.create_task(Alarm())
    executor.start_polling(dp, skip_updates=True)
