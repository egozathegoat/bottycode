import telebot
from telebot import types
bot = telebot.TeleBot('6307577892:AAEXdAPJdzQP67eT_liPUnyZKEzv3uCwTbk')

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Привет, это команда "побеги" ляляля надо вставить приветственный текст!')

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
##добавить ссылку на ЯК и картинку карту


bot.polling(none_stop=True)

