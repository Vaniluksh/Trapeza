import telebot
from telebot import types


token = '390314515:AAHDSIFc5S8UzvUkWSe524hNjWRSMl80fJc'
bot = telebot.TeleBot(token)

def keyboard_vvod_adresa(msg, command):
    markup = types.ReplyKeyboardMarkup(row_width=2, one_time_keyboard=True, resize_keyboard=True)
    itembtn1 = types.KeyboardButton('Избраный 1')
    itembtn2 = types.KeyboardButton('Избраный  2')
    itembtn3 = types.KeyboardButton('Избраный адрес 3')
    itembtn4 = types.KeyboardButton('Избраный адрес 4')
    markup.add(itembtn1, itembtn2, itembtn3, itembtn4)
    bot.send_message(msg["chat"]['id'], 'Выберите свой адрес или пришлите мне свое геоположение', reply_markup=markup)

def keyboard_diets(msg, command):
    markup = types.ReplyKeyboardMarkup(row_width=2, one_time_keyboard=True, resize_keyboard=True)
    itembtn1 = types.KeyboardButton('Веганство')
    itembtn2 = types.KeyboardButton('ЗОЖ')
    itembtn3 = types.KeyboardButton('Каллорийная')
    markup.add(itembtn1, itembtn2, itembtn3)
    bot.send_message(msg["chat"]['id'], 'Выберете диету', reply_markup=markup)

def keyboard_persons(msg, command):
    markup = types.ReplyKeyboardMarkup(row_width=2, one_time_keyboard=True, resize_keyboard=True)
    itembtn1 = types.KeyboardButton('1')
    itembtn2 = types.KeyboardButton('2')
    itembtn3 = types.KeyboardButton('3')
    itembtn4 = types.KeyboardButton('4')
    markup.add(itembtn1, itembtn2, itembtn3, itembtn4)
    bot.send_message(msg["chat"]['id'], 'Укажите количество персон', reply_markup=markup)

def keyboard_complex(msg, command):
    markup = types.ReplyKeyboardMarkup(row_width=3, one_time_keyboard=True, resize_keyboard=True)
    itembtn1 = types.KeyboardButton('Завтрак')
    itembtn2 = types.KeyboardButton('Перекус')
    itembtn3 = types.KeyboardButton('Обед')
    itembtn4 = types.KeyboardButton('Ужин')
    itembtn5 = types.KeyboardButton('Десерт')
    itembtn6 = types.KeyboardButton('Не важно')
    markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5, itembtn6)
    bot.send_message(msg["chat"]['id'], 'Выберете комплекс', reply_markup=markup)

def keyboard_market(msg, command):
    markup = types.ReplyKeyboardMarkup(row_width=2, one_time_keyboard=True, resize_keyboard=True)
    itembtn1 = types.KeyboardButton('Дикси')
    itembtn2 = types.KeyboardButton('Окей')
    itembtn3 = types.KeyboardButton('Пятерочка')
    itembtn4 = types.KeyboardButton('Карусель')
    markup.add(itembtn1, itembtn2, itembtn3, itembtn4)
    bot.send_message(msg["chat"]['id'], 'Выберете магазин', reply_markup=markup)

def keyboard_bluda(msg, command):
    markup = types.ReplyKeyboardMarkup(row_width=2, one_time_keyboard=True, resize_keyboard=True)
    itembtn1 = types.KeyboardButton('Диеты')
    itembtn2 = types.KeyboardButton('Мне повезет')
    itembtn3 = types.KeyboardButton('Популярное')
    itembtn4 = types.KeyboardButton('Все блюда')
    markup.add(itembtn1, itembtn2, itembtn3, itembtn4)
    bot.send_message(msg["chat"]['id'], 'Что отведаем?)', reply_markup=markup)

def keyboard_bluda_with_complex(msg, command):
    markup = types.ReplyKeyboardMarkup(row_width=2, one_time_keyboard=True, resize_keyboard=True)
    itembtn1 = types.KeyboardButton('Диеты')
    itembtn2 = types.KeyboardButton('Комплексы')
    itembtn3 = types.KeyboardButton('Мне повезет')
    itembtn4 = types.KeyboardButton('Популярное')
    itembtn5 = types.KeyboardButton('Все блюда')
    markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5)
    bot.send_message(msg["chat"]['id'], 'Что отведаем?(2)', reply_markup=markup)

def keyboard_complex2(msg, command):
    markup = types.ReplyKeyboardMarkup(row_width=3, one_time_keyboard=True, resize_keyboard=True)
    itembtn1 = types.KeyboardButton('Завтрак')
    itembtn2 = types.KeyboardButton('Перекус')
    itembtn3 = types.KeyboardButton('Обед')
    itembtn4 = types.KeyboardButton('Ужин')
    itembtn5 = types.KeyboardButton('Десерт')
    markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5)
    bot.send_message(msg["chat"]['id'], 'Выберете комплекс', reply_markup=markup)
