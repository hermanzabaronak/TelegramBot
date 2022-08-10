import telebot
from telebot import types

bot = telebot.TeleBot('5511258057:AAEnhAyi83PPcU5a_qWVEn2a8YncbvoCoSk')


@bot.message_handler(commands=['welcome'])
def start(message):
        mess = f'Hi <b>{message.from_user.first_name}</b>! This is my CV chatbot. Please, press /start to know more about me.'
        bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler(commands=['start', 'Start'])
def website(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    linkedin = types.KeyboardButton('/LinkedIn')
    instagram = types.KeyboardButton('/Instagram')
    cv = types.KeyboardButton('/CV')
    photo = types.KeyboardButton('/Photo')
    contact = types.KeyboardButton('/Contact_me')

    markup.add(linkedin, instagram, cv, photo, contact)
    bot.send_message(message.chat.id, 'Please, choose what you would like to know about me.', reply_markup=markup)


@bot.message_handler(commands=['CV'])
def cv(message):
    cvdoc = open('Zabaronak_CV .docx', 'rb')
    bot.send_document(message.chat.id, cvdoc)

@bot.message_handler(commands=['Photo'])
def phts(message):
    photos = open('photo_2022-08-10_15-19-32.jpg', 'rb')
    bot.send_photo(message.chat.id, photos)

@bot.message_handler(commands=['LinkedIn'])
def lnkd(message):
    bot.send_message(message.chat.id,'https://www.linkedin.com/in/herman-zabaronak-7a2501171/', parse_mode='html')

@bot.message_handler(commands=['Instagram'])
def insta(message):
    bot.send_message(message.chat.id,'https://www.instagram.com/zabarona_/', parse_mode='html')

@bot.message_handler(commands=['Contact_me'])
def contact(message):
    bot.send_message(message.chat.id,'Please, write on misterzab@gmail.com or @zabarona in Telegram', parse_mode='html')


bot.polling(none_stop=True)



