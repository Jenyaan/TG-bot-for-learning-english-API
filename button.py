from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from conf import url_vocabulary
def inline_button(categores):
    info, lst = url_vocabulary(categores)
    markup = InlineKeyboardMarkup(row_width=1)
    for i in lst:
        markup.insert(InlineKeyboardButton(text=str(i), callback_data=info[f'{i}']))
    return markup

