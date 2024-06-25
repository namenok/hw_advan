import telebot

import requests
import json

API_TOKEN = '7257738215:AAHQZQOjJWqnkeN8p_ihnsO03laLffp6lP0'

bot = telebot.TeleBot(API_TOKEN)

API_TOKEN_WEATHER = 'af2d18189b21ad385e9969492f9f026d'


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id, 'хочеш дізнатись погоду Києва ? введи /weather kyiv \n Так само для міст odesa , lviv ! '
    )


@bot.message_handler(commands=['weather'])
def get_weather(message):
    city = message.text.split()[1]

    res = get_api_weather(city)
    print(res)
    bot.send_message(
        message.chat.id, res)


def get_api_weather(cit):
    if cit == 'kyiv':
        url_kyiv = 'https://api.openweathermap.org/data/2.5/weather?lat=50.45&lon=30.52&appid=af2d18189b21ad385e9969492f9f026d'
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url_kyiv, headers=headers)
        weather_kyiv = response.json()

        hum = weather_kyiv["main"]
        temp = weather_kyiv["main"]
        cel_temp = int(temp["temp"]) - 273, 15
        pres = weather_kyiv["main"]
        return f'Вологість : {hum["humidity"]}\nТемпература середня : {cel_temp}\nТиск : {pres["pressure"]}'

    elif cit == 'odesa':
        url_od = 'https://api.openweathermap.org/data/2.5/weather?lat=46.48&lon=30.71&appid=af2d18189b21ad385e9969492f9f026d'
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url_od, headers=headers)
        url_od = response.json()

        hum = url_od["main"]
        temp = url_od["main"]
        cel_temp = int(temp["temp"]) - 273, 15
        pres = url_od["main"]
        return f'Вологість : {hum["humidity"]}\nТемпература середня : {cel_temp}\nТиск : {pres["pressure"]}'

    elif cit == 'lviv':
        url_lvi = 'https://api.openweathermap.org/data/2.5/weather?lat=49.84&lon=24.03&appid=af2d18189b21ad385e9969492f9f026d'
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url_lvi, headers=headers)
        url_lvi = response.json()

        hum = url_lvi["main"]
        temp = url_lvi["main"]
        cel_temp = int(temp["temp"]) - 273, 15
        pres = url_lvi["main"]
        return f'Вологість : {hum["humidity"]}\nТемпература середня : {cel_temp}\nТиск : {pres["pressure"]}'


bot.polling()

