import pyowm
import telebot

owm = pyowm.OWM('your-API-key', language='ru') #API-key Open Weather Map; (language if you need).
bot = telebot.TeleBot("TOKEN") # Get token with BotFather


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, введи название города на русском или английском')

@bot.message_handler(content_types=['text'])
def send_echo(message):
    observation = owm.weather_at_place( message.text )
    w = observation.get_weather()
    temp = w.get_temperature('celsius')['temp']

    answer = message.text + ": " + w.get_detailed_status() + "\n"
    answer += 'Температура: ' + str(temp) + '℃' + "\n\n"

    if temp < 10:
        answer +='Одевайся теплее'

    elif temp <15:
        answer += 'Прохладно, возьми шапку на всякий'   

    elif temp <20:
        answer += 'Ну, вроде тепло'
    
    elif temp >20:
        answer += 'ОГО! Да у вас лето!'


    bot.send_message(message.chat.id, answer)


bot.polling( none_stop = True)