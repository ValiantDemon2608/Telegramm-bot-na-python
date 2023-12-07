from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, callback_query
import time
import logging
import asyncio
from aiogram.dispatcher.filters import Text
import random as r

API_TOKEN = '6773333833:AAFsaNhdm_8RvFxcmXoPx0tJ7jH0zGlo1rQ'
text_alert = 'Напоминание'

bot = Bot(token = API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text='Приветики!😊'),
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer('😁Приветствую тебя в моём боте!😁', reply_markup=keyboard)

@dp.message_handler(text='Приветики!😊')
async def send_welcome(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text='Случайный факт о Созвездии'),
            types.KeyboardButton(text='Созвездие маркет'),
            types.KeyboardButton(text='Ссылки на Созвездие'),
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer('Выберите категорию:', reply_markup=keyboard)

urlkb = InlineKeyboardMarkup(row_width=1)
urlButton = InlineKeyboardButton(text='Созвездие Маркет', 
url ='https://vk.com/valiantdemon2608')
urlkb.add(urlButton)

@dp.message_handler(text="Созвездие маркет")
async def url_market(message: types.message):
    await message.answer('Актуальная ссылка:',reply_markup = urlkb)

urlkb_SocialMedia = InlineKeyboardMarkup(row_width=1)
urlButtonSocial = InlineKeyboardButton(text = 'Сайт Созвездия')

dp.message_handler(text = 'Ссылки на Созвездие')
async def url_market(message: types.message):
    await message.answer('Актуальная ссылка:',reply_markup = urlkb)

@dp.message_handler(text="Случайный факт о Созвездии")
async def facts(message: types.message):
    number = r.randint(0,10)
    if number == 1:
        await message.reply('На территории дружины , есть большой стул , который построила семья ,однажды проживающая в "Созвездии". Все кто хочет может загадать желание связанное с семьей, возле него.')
    if number == 2:
        await message.reply('Изначально в " Созвездии" были только весенние и летние смены')
    if number == 3:
        await message.reply('На главном корпусе есть Знаки зодиака под которыми по традиции фотографируются, и загадывают желания!')
    if number == 4:
        await message.reply('У "Созвездия" есть свой маскот Звездун')
    if number == 5:
        await message.reply('kekek')
    if number == 6:
        await message.reply('kekek')
    if number == 7:
        await message.reply('kekek')
    if number == 8:
        await message.reply('kekek')
    if number == 9:
        await message.reply('kekek')
    if number == 10:
        await message.reply('kekek')

@dp.message_handler(commands=["alert"])
async def start_alert(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    user_full_name = message.from_user.full_name
    logging.info(f'{user_id} {user_full_name} {time.asctime}')
    await message.reply(f'Привет, {user_full_name}')
    for i in range(7):
        await asyncio.sleep(60*60*24)
        await bot.send_message (user_id,text_alert.format(user_name))

@dp.message_handler(commands=['creator'])
async def send_creator(message: types.message):
    await message.answer('Мой создатель: Ташлыков Дмитрий Романович и Пичко Георгий Павлович')
#Сделать ссылки на все соцсети созвездия 
#Место для создания алерта в котором будут приходить оповещения из группы вк созвездие
#Стикеры с созвездием
#Сделать интерактив с местами для загадывания желаний: Предложить сделать фотки на которых дети загадывают желания и скидывать их на электронную почту созвездия
#Штука что бы синхронизироваться с тг
if __name__ =='__main__':
    executor.start_polling(dp)
