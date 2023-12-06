from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton
import time
import logging
import asyncio

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


urlkb = InlineKeyboardMarkup(row_width=1)
urlButton = InlineKeyboardButton(text='VK', 
url ='https://vk.com/valiantdemon2608')
urlButton2 = InlineKeyboardButton(text='GitHub',
url = 'https://github.com/ValiantDemon2608')
urlkb.add(urlButton, urlButton2)

@dp.message_handler(commands='links')
async def url_command(message: types.message):
    await message.answer('Useful links:', reply_markup=urlkb)

@dp.message_handler(commands=['creator'])
async def send_creator(message: types.message):
    await message.answer('Мой создатель: Ташлыков Дмитрий Романович')

#Место для создания алерта в котором будут приходить оповещения из группы вк созвездие
#Стикеры с созвездием

#Штука что бы синхронизироваться с тг
if __name__ =='__main__':
    executor.start_polling(dp)
