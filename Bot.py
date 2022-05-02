import telebot
from Parser_WILDBERRIES import Wildberries
from Parser_LAMODA import Lamoda
from Klaviatura import Klaviatura
from Secret import token

bot = telebot.TeleBot(token)
K = Klaviatura()
parser = Wildberries()
parser1 = Lamoda()


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Greetings, parser! \n'
                                      'Do you want to know which sites I can parse for you right now?\n\n'
                                      'Приветствую, парсер! \n'
                                      'Хочешь узнать, какие сайты я могу пропарсить прямо сейчас?',
                                      reply_markup=K.markupinline('start'))


@bot.message_handler(content_types=['text'])
def ostalnoe(message):
    bot.send_message(message.chat.id, 'Упс, я все еще не сильно понимаю ваш язык, давай по кнопочкам! \n\n'
                                      "Oops, I still don't understand your language very well, "
                                      "let's hit the buttons!")


@bot.callback_query_handler(func=lambda call: True)
def answer_buttons(call):
    if call.data == 'Wildberies':
        bot.send_message(call.message.chat.id, 'Вот: \nHere we are',
                                               reply_markup=K.markupinline('wildberies'))

    elif call.data == 'Shtani':
        bot.send_message(call.message.chat.id, 'Processing "trousers" request \n\n ... \n\n'
                                               ' This may take some time, '
                                               'but you get a data plate at the end! \n '
                                               'As long as you can safely enjoy your legal holiday \n\n'
                                               'Обрабатываю запрос "Штаны" \n\n ... \n\n'
                                               ' Это может занять некоторое время, '
                                               'но ты получишь табличку с данными в конце! \n '
                                               'Пока можешь смело наслаждаться законным отдыхом')
        parser.run()
        bot.send_document(call.message.chat.id, open('shtani.csv', 'rb'))

    elif call.data == 'Lamoda':
        bot.send_message(call.message.chat.id, 'Вот: \nHere we are',
                                               reply_markup=K.markupinline('lamoda'))

    elif call.data == 'Blouse':
        bot.send_message(call.message.chat.id, 'Processing "Blouse" request \n\n ... \n\n'
                                               ' This may take some time, '
                                               'but you get a data plate at the end! \n '
                                               'As long as you can safely enjoy your legal holiday \n\n'
                                               'Обрабатываю запрос "<Блузки>" \n\n ... \n\n'
                                               ' Это может занять некоторое время, '
                                               'но ты получишь табличку с данными в конце! \n '
                                               'Пока можешь смело наслаждаться законным отдыхом')
        parser1.run()
        bot.send_document(call.message.chat.id, open('Blouse.csv', 'rb'))

    elif call.data == 'Yes':
        bot.send_message(call.message.chat.id, 'Отлично, вот варианты, которые я могу предложить \n'
                                               'Great, here are the options I can suggest',
                                               reply_markup=K.markupinline('yes'))

    elif call.data == 'No':
        bot.send_message(call.message.chat.id, 'Thank you for your interest! \n\n '
                                               'However, if you have a minute, please write,'
                                               'what creators can improve in my work. \n\n '
                                               'There is also an opportunity to support the creators'
                                               'because they are still developing me.'''
                                               "If you need me again, I'm always here, just write /start. \n "
                                               'Waiting for you,Come back! \n\n\n'
                                               'Спасибо, что проявил интерес! \n\n'
                                               'Однако если есть минутка, напиши, пожалуйста,'
                                               ' что создатели могут улучшить в моей работе. \n\n'
                                               'Также есть возможность поддержать создателей,'
                                               ' ведь они все еще развивают меня. \n\n'
                                               'Если я снова понадоблюсь, то всегда тут, стоит только написать '
                                               '/start. \n Жду тебя, возвращайся!',
                                               reply_markup=K.markupinline('no'))

    elif call.data == 'start':
        bot.send_message(call.message.chat.id, 'Greetings, parser! \n'
                                               'Do you want to know which sites I can parse for you right now?\n\n'
                                               'Приветствую, парсер! \n'
                                               'Хочешь узнать, какие сайты я могу пропарсить прямо сейчас?',
                                               reply_markup=K.markupinline('start'))

    elif call.data == 'Donate':
        bot.send_message(call.message.chat.id, 'Здесь будет линк на перевод')


if __name__ == '__main__':
    bot.infinity_polling()