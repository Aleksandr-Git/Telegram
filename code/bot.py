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

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply('Привет!', reply_markup=kb.greed_kb)

# отправляем в чат показания датчиков влажности
@dp.message_handler(commands=['Показания'])
async def send_welcome(message: types.Message):
    await message.reply(DATA.decode().rstrip()) 

# отправляем команду на arduino на включения режима мониторинга
@dp.message_handler(commands=['Мониторинг'])
async def send_mon(message: types.Message):
    ser.write(b'CMode_M!')  

# отправляем команду на arduino для постановки на охрану
@dp.message_handler(commands=['Охрана'])
async def send_alarm(message: types.Message):
    ser.write(b'CMode_A!')  

# подключаемся к COM порту
async def Con_ser():
    global CONNECT, ser

    if os.name == 'posix':  # если linux
        ser = serial.Serial('/dev/ttyUSB0')  # подключаемся к COM порту

    if os.name == 'nt':  # если windows
        ser = serial.Serial('COM4', 9600, timeout=1)  # подключаемся к COM порту

    print(ser.name)  # печатаем номер COM порта

async def Alarm():  # проверяет данные с COM порта и отправляет сообщения в чат
    global DATA
    while True:
        await asyncio.sleep(0)
        DATA = ser.readline()  # читаем строку с COM порта
        try:
            for i, j in dict_Alarm.items():
                if DATA.decode().rstrip() == i:

# аргументы: кому отправить, текст сообщения ...
                    await bot.send_message(MY_ID, j[0], disable_notification=True)
                    print(j[0])

        except UnicodeDecodeError:
            continue

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(Con_ser())
    loop.create_task(Alarm())
    executor.start_polling(dp, skip_updates=True)
