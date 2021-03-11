import config
import logging
import keyboards
import MakeMessage
from SQL import SQLighter
import asyncio
from ParseSub import ParseNews
from aiogram import *


logging.basicConfig(level=logging.INFO)

# инициализация бота
bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)
n = ParseNews()

#Инициализация базы данных
db = SQLighter('database.db')


@dp.message_handler(commands=['start'])
async def start_menu(message: types.Message):
    await message.answer(MakeMessage.MM_start(), parse_mode='HTML')


@dp.message_handler(commands=['info'])
async def info_menu(message: types.Message):
    await message.answer("Выберете интересующую информацию", reply_markup=keyboards.greed_info)


@dp.message_handler(text='События сегодня')
async def get_today(message: types.Message):
    await message.answer(MakeMessage.MM_Today(), parse_mode='HTML')


@dp.message_handler(text='Контакты')
async def get_contacts(message: types.Message):
    await message.answer(MakeMessage.MM_contacts())


@dp.message_handler(text='Адреса библиотек')
async def get_adreccs(message: types.Message):
    await message.answer("Выбирите нужный район:", reply_markup=keyboards.greed_adreccs)


@dp.message_handler(text=['Савёлки', 'Матушкино', 'Крюково', 'Силино'])
async def get_adrecc(message: types.Message):
    await message.answer(MakeMessage.MM_adrecc(message.text))


@dp.message_handler(text='Алена ты лучшая)!011!!)(9))0')
async def poshalka(message: types.Message):
    await message.answer('Я знаю')
    await message.answer_sticker('CAACAgIAAxkBAALYDWAsHl8mydZroM8QcSmiIB0VEvqEAAI9AAMULFEWM5bdrJaNaAQeBA')


@dp.message_handler(text=['subscribe'])
async def subscribe(message: types.Message):
    if not db.subscriber_exist(message.from_user.id):
        db.add_subscriber(message.from_user.id)
        await message.answer("welcome")
    else:
        db.update_subscription(message.from_user.id, True)
        await message.answer("nice")


@dp.message_handler(text=['unsubscribe'])
async def unsubscribe(message: types.Message):
    if not db.subscriber_exist(message.from_user.id):
        db.add_subscriber(message.from_user.id, False)
        await message.answer("Вы не были подписаны")
    else:
        db.update_subscription(message.from_user.id, False)
        await message.answer("Вы успешно отписались")


async def scheduled(wait_for):
    while True:
        await asyncio.sleep(wait_for)
        news_link = n.NewsLink()
        news = n.NewNewsList(news_link)
        subscriptions = db.get_subscriptions()
        n.lastkay = news_link
        if news:
            news.reverse()
            for new in news:
                for s in subscriptions:
                    await bot.send_message(s[1], text=MakeMessage.MM_news(new), disable_notification=True, parse_mode='html')

async def on_startup(x):
    asyncio.create_task(scheduled(3600))



if __name__ == '__main__':

    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)

