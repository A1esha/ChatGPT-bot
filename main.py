import telebot
from telebot import types
import openai

TOKEN = "your token" # Token of the telegram bot

bot = telebot.TeleBot(TOKEN)

openai.api_key = "Your token"# Token ChatGPT

lang = 0 ### When we have 0 information in out bot will be on english, if 1 - on russian


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("English")
    btn2 = types.KeyboardButton("Русский")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, text="Hi, {0.first_name}! Select your language, which you want to use in bot.\n"
    "Привет {0.first_name}! Выбери язык использования бота".format(message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
    if message.text == "Русский":
        bot.send_message(message.chat.id, text="Привет! Вы можете использовать этого бота для решения задач по " +
            "математики, информатике и программированию. Для этого пришлите в чат задание, которое вам нужно решить")
    elif message.text == 'English':
        bot.send_message(message.chat.id,
                         text="Hi! You can use this bot to solve math, informatics and programming problems." +
                                " Just send text of your probrem to the chat")
    else:
        problem = message.text
        model = "text-davinci-003"

        answer = openai.Completion.create(engine=model, prompt=problem, max_tokens=1024,temperature=0.5, top_p=1,
                                          frequency_penalty=0, presence_penalty=0)
        s = answer.choices[0].text
        bot.send_message(message.chat.id, text=s)


bot.polling(none_stop=True)
