import telebot
from telebot import types
import webbrowser

bot = telebot.TeleBot('6307577892:AAEXdAPJdzQP67eT_liPUnyZKEzv3uCwTbk')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Расписание")
    btn2 = types.KeyboardButton("Навигация")
    btn3 = types.KeyboardButton("О фестивале")
    btn4 = types.KeyboardButton("Связаться с организаторами")
    btn5 = types.KeyboardButton("Как добраться")
    btn6 = types.KeyboardButton("Купить билет")
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
    bot.send_message(message.chat.id, 'Привет, это команда "побеги" ляляля надо вставить приветственный текст!'.format(message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "Расписание"):
        bot.send_message(message.chat.id, 'здесь должно быть либо задизайненое ввиде картинки расписание, либо оно же, но текстом. у меня его нет')
        file = open('./raspisanie-2.gif', 'rb')
        bot.send_photo(message.chat.id, file)

    elif(message.text == "О фестивале"):
        bot.send_message(message.chat.id, 'очень классное описание фестиваля')

    elif (message.text == "Навигация"):
       bot.send_message(message.chat.id, 'дофига крутая задизайненая карта и ссылка на яндекскарту мероприятия')
       file = open('./geo-map-small.gif', 'rb')
       bot.send_photo(message.chat.id, file)

    elif(message.text == "Связаться с организаторами"):
        bot.send_message(message.chat.id, 'контакты оргов')

    elif(message.text == "Как добраться"):
        bot.send_message(message.chat.id, 'как добраться')

    elif(message.text == "Купить билет"):
        bot.send_message(message.chat.id, 'покупка билета')


    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)


@bot.message_handler(commands=['timetable'])
def main(message):
    bot.send_message(message.chat.id, 'здесь должно быть либо задизайненое ввиде картинки расписание, либо оно же, но текстом. у меня его нет')
    file = open('./raspisanie-2.gif', 'rb')
    bot.send_photo(message.chat.id, file)


@bot.message_handler(commands=['navigation'])
def main(message):
    bot.send_message(message.chat.id, 'дофига крутая задизайненая карта и ссылка на яндекскарту мероприятия')
    file = open('./geo-map-small.gif', 'rb')
    bot.send_photo(message.chat.id, file)

@bot.message_handler(commands=['about'])
def main(message):
    bot.send_message(message.chat.id, 'очень классное описание фестиваля')

@bot.message_handler(commands=['contacts'])
def main(message):
 bot.send_message(message.chat.id, 'контакты оргов')


@bot.message_handler(commands=['howtoget'])
def main(message):
     bot.send_message(message.chat.id, 'как добраться')


bot.polling(none_stop=True)

