from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

btnBackMenu = KeyboardButton('Меню🍻')
justMenu_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(btnBackMenu)
btnSpr = KeyboardButton('Плани📝')
btnBdg = KeyboardButton('Витрати')
menu_kb = ReplyKeyboardMarkup(resize_keyboard=True).row(btnSpr, btnBdg).add(btnBackMenu)

btnZap = KeyboardButton("Запланувати")
bntShw = KeyboardButton("Переглянути плани")
plans_kb = ReplyKeyboardMarkup(resize_keyboard=True).row(btnZap, bntShw).add(btnBackMenu)