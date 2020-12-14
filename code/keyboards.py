from aiogram.types import ReplyKeyboardMarkup,  \
                          KeyboardButton

bthHello = KeyboardButton('/Привет')
greed_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(bthHello)
