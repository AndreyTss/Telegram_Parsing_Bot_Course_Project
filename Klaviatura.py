from telebot import types


class Klaviatura:

    def __init__(self):
        self.keys = types.InlineKeyboardButton(text='Блузки / Blouse', callback_data='Blouse')
        self.keyf = types.InlineKeyboardButton(text='Футболки / T-shorts', callback_data='Futbolki')
        self.keys1 = types.InlineKeyboardButton(text='Штаны / Trousers', callback_data='Shtani')
        self.keyf1 = types.InlineKeyboardButton(text='Футболки / T-shirts', callback_data='Fut')
        self.key1 = types.InlineKeyboardButton(text='Wildberies', callback_data='Wildberies')
        self.key2 = types.InlineKeyboardButton(text='Lamoda', callback_data='Lamoda')
        self.key3 = types.InlineKeyboardButton(text='Обратная связь \n Review',
                                               url='https://forms.gle/j8vMH7VHQfTgVy8i7')
        self.key4 = types.InlineKeyboardButton(text='На развитие проекта \n For the development of the project',
                                               callback_data='Donate')
        self.key5 = types.InlineKeyboardButton(text='Yes / Да', callback_data='Yes')
        self.key6 = types.InlineKeyboardButton(text='No / Нет', callback_data='No')
        self.key_back = types.InlineKeyboardButton(text='Return back / Вернуться назад', callback_data='Yes')
        self.key_back1 = types.InlineKeyboardButton(text='Return back / Вернуться назад', callback_data='start')

    def markupinline(self, flag):
        markup_inline = types.InlineKeyboardMarkup(row_width=2)
        if flag == 'start':
            markup_inline.add(self.key5, self.key6)
            return markup_inline
        elif flag == 'wildberies':
            markup_inline.add(self.keys1, self.keyf1, self.key_back)
            return markup_inline
        elif flag == 'lamoda':
            markup_inline.add(self.keys, self.keyf, self.key_back)
            return markup_inline
        elif flag == 'yes':
            markup_inline.add(self.key1, self.key2, self.key_back1)
            return markup_inline
        elif flag == 'no':
            markup_inline.add(self.key3, self.key4, self.key_back1)
            return markup_inline



