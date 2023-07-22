import telebot
from telebot import types
import webbrowser

bot = telebot.TeleBot('6090863335:AAG0WLd9Nepwqp5xqPm_j2XRwXD2ofa1Dvc')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    #btn1 = types.KeyboardButton("Расписание")
    #btn2 = types.KeyboardButton("Навигация")
    btn1 = types.KeyboardButton("О фестивале")
    btn2 = types.KeyboardButton("Купить билет")
    #btn5 = types.KeyboardButton("Как добраться")
    btn3 = types.KeyboardButton("Связаться с нами")
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id, 'Привет, это команда "побеги"! Пожалуйста, выберите интересующий вас раздел:'.format(message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
    #if(message.text == "Расписание"):
        #bot.send_message(message.chat.id, 'здесь должно быть либо задизайненое ввиде картинки расписание, либо оно же, но текстом. у меня его нет')
        #file = open('./raspisanie-2.gif', 'rb')
        #bot.send_photo(message.chat.id, file)

    if(message.text == "Купить билет"):
        bot.send_message(message.chat.id, 'Приобрести билет можно по ссылке: https://events.nethouse.ru/all/77174/')
        bot.send_message(message.chat.id, 'Спасибо, что поддерживаете нас <3')

    elif(message.text == "О фестивале"):
        file = open('./Banner — 1.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
        bot.send_message(message.chat.id, 'Наш лесной фестиваль по традиции пройдёт в конце лета, однако в этом году мы впервые сделаем фестиваль двухдневным. Он будет проходить 26-27 августа в ближайшем Подмосковье (место мы объявим позже). В этот раз участниками фестиваля станут разные коммуны, кооперативы и самоорганизации. ')

        bot.send_message(message.chat.id,'Основные темы нашего фестиваля — это стремление к объединению и открытому взаимодействию, а главная особенность — это возможность познакомиться с локальными инициативами через совместные дискуссии, лекции, мастер-классы и различные иммерсивные практики.')

        bot.send_message(message.chat.id,' Мы приглашаем всех в лес — ведь программа нашего фестиваля в этот раз рассчитана на два дня. Совместные прогулки, дискуссии и практики днём будут плавно перетекать в ночные беседы у костра и любование звёздами. ')

        bot.send_message(message.chat.id,'Приобрести билет на фестиваль вы можете через кнопку "Купить билет" в этом боте. Билет — это вход на фестиваль и вклад в его осуществление. Фестиваль длится два дня, с 26-го по 27-е августа. ')

        bot.send_message(message.chat.id,'Вы можете купить билет за разную стоимость и тем самым поддержать нас. Все средства оплачивают организацию музыкальной сцены, монтаж, печать каталогов и многое другое. Мы постарались сделать наш фестиваль доступным для всех, поэтому, если у вас нет возможности приобрести билет, вы можете подать заявку на волонтёрство по ссылке: https://clck.ru/355Esu')


    #elif (message.text == "Навигация"):
       #bot.send_message(message.chat.id, 'дофига крутая задизайненая карта и ссылка на яндекскарту мероприятия')
       #file = open('./geo-map-small.gif', 'rb')
       #bot.send_photo(message.chat.id, file)

    elif(message.text == "Связаться с нами"):
        bot.send_message(message.chat.id, 'Если на любом из этапов у вас возникнут сложности или что-то пойдет не так, напишите нам: @egozathegoat, @lexa_levshin. Все уладим!')

    #elif(message.text == "Как добраться"):
        #bot.send_message(message.chat.id, 'как добраться')
markup = types.ReplyKeyboardMarkup(resize_keyboard=True)


#@bot.message_handler(commands=['timetable'])
#def main(message):
    #bot.send_message(message.chat.id, 'здесь должно быть либо задизайненое ввиде картинки расписание, либо оно же, но текстом. у меня его нет')
    #file = open('./raspisanie-2.gif', 'rb')
    #bot.send_photo(message.chat.id, file)


#@bot.message_handler(commands=['navigation'])
#def main(message):
    #bot.send_message(message.chat.id, 'дофига крутая задизайненая карта и ссылка на яндекскарту мероприятия')
    #file = open('./geo-map-small.gif', 'rb')
    #bot.send_photo(message.chat.id, file)

@bot.message_handler(commands=['about'])
def main(message):
    bot.send_message(message.chat.id, 'очень классное описание фестиваля')

@bot.message_handler(commands=['contacts'])
def main(message):
 bot.send_message(message.chat.id, 'контакты оргов')


#@bot.message_handler(commands=['howtoget'])
#def main(message):
     #bot.send_message(message.chat.id, 'как добраться')

@bot.message_handler(commands=['tikets'])
def main(message):
     bot.send_message(message.chat.id, 'купить билет')

bot.polling(none_stop=True)

