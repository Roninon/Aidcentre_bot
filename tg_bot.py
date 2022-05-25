from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from datetime import datetime
import time


import os

# await message.reply(message.text)  -  ответ на сообщение
# await bot.send_message(message.from_user.id, message.text)  -  сообщение в ЛС
# await message.answer(message.text)  -  собщение в группу

text_hum_aid = "Пункт № 1. ЦНАП\n\n📍Адреса: вул. Героїв Майдану, 7 (вхід з двору) \n📍Графік роботи: ПН-ПТ: 09:00-17:00; СБ: 10:00-15:00; НД: вихідний \n📍Видають: продуктові набори та засоби гігієни від Чернівецької міської ради\n\nПункт № 2. Дитячий хаб.\n\n📍Адреса: вул. Івана Франка, 29\n(Будинок культури творчої молоді «Автограф») \n📍Графік роботи: ПН-ПТ: 10:00-17:00; СБ: 10:00-15:00; НД: вихідний\n📍Видають: дитяче харчування, підгузки, дитячий одяг, iграшки, дитячi книги тощо (за наявностi)\n\nПункт № 3. Дитячий хаб.\n\n📍Адреса: м. Чернівці, вул. Головна, 223\n(Магазин «Цархліб»)\n📍Графік роботи: ПН-ПТ: 10:00-17:00; СБ: 10:00-15:00; НД: вихідний \n📍Видають: дитяче харчування, підгузки, дитячий одяг, iграшки, дитячi книги тощо (за наявності)\n\nПункт №4\n\n📍Адреса: м. Чернівці, вул. Підкова, 7а (Садгора) \n📍Графік роботи: ПН-ПТ: 10:00-17:00; СБ: 10:00-15:00; НД: вихідний \n📍Видають: одяг дитячий та дорослий, дитяче харчування, підгузки тощо (за наявності)\n\nПункт №5 Благодійний фонд «Карітас Чернівці»\n\n📍Адреса: м. Чернівці, вул. Героїв Майдану, 44 (Управління у справах сім'ї та молоді департаменту соціальної політики ) \n📍Графік роботи: ПН-ПТ: 10:00-18:00; СБ-НД: вихідні \n📍Видають: гiгiєнiчнi набори для осіб вiком 65+, особам з інвалідністю та маломобільним (лежачим) людям.\n\n\nПункт обласної військової адміністрації \n📍Адреса: м. Чернівці, вул. Небесної Сотні, 6 \n📍Графік роботи: 10:00 - 18:00\n📍Видають: одяг"
text_psy_aid = "Психологічна допомога\n\n📞037 2 57 15 15 \n📞095 932 15 15 \n📞066 798 76 53"

btnOne = KeyboardButton('Житель приміщення')
btnTwo = KeyboardButton('Волонтер')
btnThree = KeyboardButton('Хочу пожертвувати')

btn4 = KeyboardButton('вул. Ентузіастів, 5Б')
btn5 = KeyboardButton('вул. Чорноморська, 4А')
btn6 = KeyboardButton('вул. 28 Червня, 17')

btnHelp1 = KeyboardButton('Духовна або психологічна підтримка')
btnHelp2 = KeyboardButton('Гуманітарна допомога')
btnHelp3 = KeyboardButton('Діти')
btnHelp4 = KeyboardButton('Юристи')
btnHelp5 = KeyboardButton('Робота')
btnHelp6 = KeyboardButton('Волонтерство')
btnHelp7 = KeyboardButton('Облік')

btnHome = KeyboardButton('◀  На головну')
btnAcces = InlineKeyboardButton('Згоден з прочитаним', callback_data='button1')

MainMenu = ReplyKeyboardMarkup(
    resize_keyboard=True).add(btnOne, btnTwo, btnThree)
SecondMenu = ReplyKeyboardMarkup(
    resize_keyboard=True).add(btn4, btn5, btn6, btnHome)
AccesMenu = InlineKeyboardMarkup(row_width=1).add(btnAcces)
HelpMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnHelp1, btnHelp2, btnHelp3, btnHelp4, btnHelp5, btnHelp6, btnHelp7, btnHome)

# def Board (*args):

# 	temp_arr = list[str(args)]
# 	arr_len = len(temp_arr)
# 	for (i = 0; i < arr_len; i++ ):
# 		btnName = KeyboardButton(name)


bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def echo_send(message: types.Message):
    await message.answer('Привіт! Мене звати Тарас. Я– бот для пошуку корисної інформації у місті Чернівці🧡')
    # time.sleep(4)
    await message.answer('Щоб я краще розумів, про що нам можна спілкуватись, розкажіть трохи, хто ви?', reply_markup=MainMenu)


@dp.message_handler()
async def sendMessage(message: types.Message):
    match message.text:
        case "Житель приміщення":
            await message.answer('Перш ніж почати, я б хотів проговорити правила приміщення, де ви перебуваєте! Оберіть місце проживання:', reply_markup=SecondMenu)

        case "вул. Ентузіастів, 5Б":
            await message.answer_photo(photo=open('./media/img-rule.jpg', 'rb'))
            await message.answer_photo(photo=open('./media/img-rule-2.jpg', 'rb'), reply_markup=AccesMenu)

        case "Гуманітарна допомога":
        	await message.answer(text_hum_aid, reply_markup=HelpMenu)

        case "Духовна або психологічна підтримка":
            await message.answer(text_psy_aid)

        case "◀  На головну":
        	await message.answer('Повертаю на головну. Хто ви?', reply_markup=MainMenu)

        case _:
            await message.answer('Не зрозумів тебе. Спробуй обрати дію знизу екрана!')


@dp.callback_query_handler(lambda message: message.data == 'button1')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id,
     'О’кей, тепер ми можемо продовжити🥰\nПідкажіть, про що Ви хотіли б дізнатись?', reply_markup=HelpMenu)


executor.start_polling(dp, skip_updates=True)
