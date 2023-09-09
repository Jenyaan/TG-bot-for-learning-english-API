from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, \
    InlineKeyboardButton
import random 
import requests
import json
from bs4 import BeautifulSoup
from time import sleep
import fake_useragent

url = 'https://englishvoyage.com/api/webapi/'

headers = {
    'User-Agent': fake_useragent.FakeUserAgent().random,
    'X-Requested-With': 'XMLHttpRequest'
}

list_card = []
list_keys = {}
my_quiz = 0

def url_categore():
    path = 'category'
    res = requests.get(url+path, headers=headers).json()
    info = []
    for i in res:
        #!!!!!!!!!!!!!!!!!!!
        info.append(i['Name'])
    info = url_vocabulary(info,"verif")
    return info

def url_vocabulary(categore, types):
    path = 'flashcardset/vocabulary'
    res = requests.get(url+path, headers=headers).json()
    if types == "cout":
        info = {}
        lst = []
        for i in res:
            if i['CategoryName'] == categore:
                info[i['Name']] = i['Id']
                lst.append(i['Name'])
        return info, lst
    elif types == "verif":
        info = []
        for i in res:
            if i['CategoryName'] in categore and i['CategoryName'] not in info:
                info.append(i['CategoryName'])
        print(info)
        return info                    


def url_cards(id):
    path = f'trainingvocabulary/tasks/{id}/0/1/0'
    res = requests.get(url+path, headers=headers).json()
    info = {}
    for i in res:
        info[i['Question']] = i['Answer']
    return info

