import sqlite3

import telebot
from telebot import types

from consts import *
from settings import token
from parce import parce

bot = telebot.TeleBot(token)

region = []
city = []


@bot.message_handler(commands=[COMMAND_START])
def start_message(message):

    db = sqlite3.connect(DATA_BASE)
    db.row_factory = lambda cursor, row: row[0]
    cur = db.cursor()

    cur.execute(COMMAND_DELETE)

    db.commit()

    db.close()

    bot.send_message(message.chat.id, START_TEXT)

    parce()

    bot.send_message(message.chat.id, STOP_PARCE_TEXT)


@bot.message_handler(content_types=TYPE_CONTENT)
def message_reply(message):

    db = sqlite3.connect(DATA_BASE)
    db.row_factory = lambda cursor, row: row[0]
    cur = db.cursor()

    cities = cur.execute(COMMAND_CITY).fetchall()
    city_hrefs = cur.execute(COMMAND_CITY_HREF).fetchall()
    regions = cur.execute(COMMAND_REGION).fetchall()
    populations = cur.execute(COMMAND_POPULATION).fetchall()

    if message.text in cities and message.text in regions:

        city.append(message.text)
        region.append(message.text)

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = [BUTTON_CITY, BUTTON_REGION]
        markup.add(*buttons)
        bot.send_message(message.chat.id, TWINS_TEXT, reply_markup=markup)

    elif message.text in cities:

        index_city = cities.index(message.text)
        city_href = city_hrefs[index_city]
        population = populations[index_city]

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button = types.KeyboardButton(text=BUTTON_RESTART)
        markup.add(button)
        bot.send_message(message.chat.id, f'{TEXT_HREF} {city_href}\n\n '
                                          f'{TEXT_POPULATION} {population}\n\n'
                                          f'{NEXT_TEXT}', reply_markup=markup)

    elif message.text in regions:

        cities_region = []

        index_cities = [i for i, ltr in enumerate(regions) if ltr == message.text]

        for index in index_cities:
            city_el = cities[index]
            cities_region.append(city_el)

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button = types.KeyboardButton(text=BUTTON_RESTART)
        markup.add(button)
        bot.send_message(message.chat.id, f'{TEXT_REGION} '
                                          f'{str(cities_region).replace("[", "").replace("]", "")}\n\n'
                                          f'{NEXT_TEXT}', reply_markup=markup)

    elif message.text == BUTTON_CITY:

        index = cities.index(city[0])
        city_href = city_hrefs[index]
        population = populations[index]

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button = types.KeyboardButton(text=BUTTON_RESTART)
        markup.add(button)
        bot.send_message(message.chat.id, f'{TEXT_HREF} {city_href}\n\n '
                                          f'{TEXT_POPULATION} {population}\n\n'
                                          f'{NEXT_TEXT}', reply_markup=markup)
        city.clear()

    elif message.text == BUTTON_REGION:

        cities_region = []

        index_cities = [i for i, ltr in enumerate(regions) if ltr == region[0]]

        for index in index_cities:
            city_el = cities[index]
            cities_region.append(city_el)

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button = types.KeyboardButton(text=BUTTON_RESTART)
        markup.add(button)
        bot.send_message(message.chat.id, f'{TEXT_REGION} '
                                          f'{str(cities_region).replace("[","").replace("]","")}\n\n'
                                          f'{NEXT_TEXT}', reply_markup=markup)
        region.clear()

    elif message.text == BUTTON_RESTART:

        bot.send_message(message.chat.id, TEXT_RESTART_1)

        db = sqlite3.connect(DATA_BASE)
        db.row_factory = lambda cursor, row: row[0]
        cur = db.cursor()

        cur.execute(COMMAND_DELETE)

        db.commit()

        db.close()

        parce()

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button = types.KeyboardButton(text=BUTTON_RESTART)
        markup.add(button)
        bot.send_message(message.chat.id, TEXT_RESTART_2, reply_markup=markup)
        city.clear()
        region.clear()


bot.polling(none_stop=True, interval=0)
