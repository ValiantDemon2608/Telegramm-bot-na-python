from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

API_TOKEN = '6773333833:AAFsaNhdm_8RvFxcmXoPx0tJ7jH0zGlo1rQ'

bot = Bot(token = API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['button'])
async def send_welcome(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text='Что?'),
            types.KeyboardButton(text='Чта??')
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer('Приветики', reply_markup=keyboard)

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

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

#Штука что бы синхронизироваться с тг
if __name__ =='__main__':
    executor:executor.start_polling(dp,skip_updates=True)
