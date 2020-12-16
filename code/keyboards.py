from aiogram.types import ReplyKeyboardMarkup,  \
                          KeyboardButton

bthInfo = KeyboardButton('/Показания')
bthMon = KeyboardButton('/Мониторинг')
bthAlarm = KeyboardButton('/Охрана')

greed_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(bthInfo).add(bthMon).add(bthAlarm)
