from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
#KeyBoard /info-----------------------------------------------------------------------
button_calendar = KeyboardButton("События сегодня")
button_news = KeyboardButton("Контакты")
button_adreccs = KeyboardButton("Адреса библиотек")

greed_info = ReplyKeyboardMarkup(resize_keyboard=True,)
greed_info.add(button_calendar).add(button_news).add(button_adreccs)

#KeyBoard "Адресс Библиотек"-----------------------------------------------------------
button_savelki = KeyboardButton("Савёлки")
button_matyshkino = KeyboardButton("Матушкино")
button_krykovo = KeyboardButton("Крюково")
button_silino = KeyboardButton("Силино")

greed_adreccs = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
greed_adreccs.add(button_savelki).add(button_matyshkino).add(button_krykovo).add(button_silino)