import telebot
import json
import keyboards
from telebot import types

token = '390314515:AAHDSIFc5S8UzvUkWSe524hNjWRSMl80fJc'
bot = telebot.TeleBot(token)


def lambda_handler(event, context):
    print("Received event: " + json.dumps(event, indent=2)) #вывод лога в cloudWatch AWS
    handle(event['message'])



def handle(msg):
    command = msg['text']
    if '/start' in command: #Ответ на первое обращение к боту
        keyboards.keyboard_vvod_adresa(msg, command) #клавиатура с выбором адреса
    elif command=='Магазин' or 'магазин':
        keyboards.keyboard_market(msg, command) #клавиатура с выбором адреса

    return msg, command


