import telebot

TOKEN = "5568377403:AAFnc1JrEQp8fgbGTIPJHveDdkuWntVHhnM"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler()
def echo_test(message: telebot.types.Message):
    bot.send_message(message.chat.id, 'hello')


@bot.message_handler(commands=['start', 'help'])
def start(message: telebot.types.Message):
    text = 'Добрый день, Я - Считалочка, умею конвертировать валюту. \n - Хочешь увидеть спиков доступных валют ' \
           'напиши /currency '
    bot.reply_to(message, text)


@bot.message_handler(commands=['currency'])
def currency(message: telebot.types.Message):
    text = 'доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key,))
    bot.reply_to(message, text)
