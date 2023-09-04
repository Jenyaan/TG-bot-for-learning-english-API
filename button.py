from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from conf import url_vocabulary, url_categore


def inline_button_card(categores):
    info, lst = url_vocabulary(categores, "cout")
    markup = InlineKeyboardMarkup(row_width=1)
    for i in lst:
        markup.insert(InlineKeyboardButton(text=str(i), callback_data=str(info[f'{i}'])))
    return markup

def inline_button_categore():
    lst = url_categore()
    markup = InlineKeyboardMarkup(row_width=1)
    for i in lst:
        markup.insert(InlineKeyboardButton(text=str(i), callback_data=str(i)))
    return markup
