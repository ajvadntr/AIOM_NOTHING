from plugins.client import Client
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

START_MESSAGE = "Hi, This Is A Test Bot"
START_MESSAGE_BUTTONS = [
     [
                 InlineKeyboardButton('CHANNEL', url='https://t.me/AIOM_BOTS'),
                 InlineKeyboardButton('GROUP', url='https://t.me/AIOM_BOTS_GROUP')
     ],
     [
                 InlineKeyboardButton('OWNER', url='https://t.me/ajvadntr')],
                 InlineKeyboardButton('MY DEY', url='https://t.me/ajvadntr')]
     ]
]

@bot.on_message(filters.command('start') & filters.private)
def start(bot, message):
   text = START_MESSAGE
   reply_markup = InlineKeyboardMarkup(START_MESSAGE_BUTTONS)
   message.replay(
        text=text,
        reply_markup=reply_markup,
        disable_web_page_preview=True
)

@bot.on_message(filters.command('help'))
def command2(bot, message):
    message.replay_text("Their Is Nothing To Say")

@bot.on_message(filters.text)
def echobot(client, message):
    message.replay_text(message.text)

GROUP = "AIOM_BOTS_GROUP"
WELCOME_MESSAGE = "Hey, Welcome To Our Group"


@bot.on_message(filters.chat(GROUP) & filters.new_chat_members)
def welcomebot(client, message):
    message.replay_text(WELCOME_MESSAGE)

@bot.on_message(filters.command('photo'))
def command3(bot, message):
    bot.send_photo(message.chat.id, "https://telegra.ph/file/0665b36e85d979ae3e862.jpg")

bot.run()
