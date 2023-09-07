from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import os
from conf import url_categore, url_cards, list_keys, list_card
from button import inline_button_card, inline_button_categore, stop_quiz
import random
from time import sleep


bot = Bot(token='YOUR_ID_BOT')
dp = Dispatcher(bot)

count = 1
correct_count = 0
my_quiz = 0


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    info = inline_button_categore()
    print(info)

    await message.answer(f"Ку гайс\nБот состоит из наборов карточек для изучение англ.\n(Все наборы берутся с сайта https://englishvoyage.com/)\n\n" +
                        "<b>Кагерии карточек</b> \n\n",reply_markup=info, parse_mode="HTML")


@dp.message_handler()
async def eho_message(message: types.Message):
    if message['text'] == "Остановить тест":
        global count
        global correct_count
        global my_quiz

        await my_quiz.delete()
        await bot.send_message(message.from_user.id, f"Готово, количество правильных ответов: {correct_count}/{count-1}", reply_markup=types.ReplyKeyboardRemove())
        count = 1
        correct_count = 0


@dp.callback_query_handler()
async def process_command(message: types.Message):
    # if message['data'] == "stop_quiz":
    #     await my_quiz.delete()
    #     await bot.send_message(message.from_user.id, "Тест закончен")
    try:
        global list_card
        global list_keys
        global my_quiz
        list_card = url_cards(int(message["data"]))
        list_keys = list_card
        list_card = list(list_card.keys())
        
        data = [list_card[0], list_card[random.randint(0,len(list_card)-1)], list_card[random.randint(0,len(list_card)-1)], list_card[random.randint(0,len(list_card)-1)]]
        random.shuffle(data)

        await bot.send_message(message.from_user.id, "Тест начался", reply_markup=stop_quiz)
        my_quiz = await bot.send_poll(message.from_user.id, list_keys[list_card[0]], data, type='quiz', correct_option_id=data.index(list_card[0]), is_anonymous=False)
    except:      
        group_card = inline_button_card(message['data'])
        await bot.send_message(message.from_user.id, f"Наборы с категорией: <b>{message['data']}</b>", reply_markup=group_card,parse_mode="HTML")

@dp.poll_answer_handler()
async def my_poll(message: types.Message):
    global my_quiz
    global count
    global correct_count
    sleep(0.5)
    await my_quiz.delete()
    if my_quiz.poll.correct_option_id == message.option_ids[0]:
        correct_count += 1


    if count <= (len(list_keys)-1):
        data = [list_card[count], list_card[random.randint(0,len(list_card)-1)], list_card[random.randint(0,len(list_card)-1)], list_card[random.randint(0,len(list_card)-1)]]
        random.shuffle(data)
        my_quiz = await bot.send_poll(message.user.id, list_keys[list_card[count]], data, type='quiz', correct_option_id=data.index(list_card[count]), is_anonymous=False)
        count += 1
    else:
        await bot.send_message(message.user.id, f"Готово, количество правильных ответов: {correct_count}/{count}")
        count = 1
        correct_count = 0



if __name__ == '__main__':
    executor.start_polling(dp)