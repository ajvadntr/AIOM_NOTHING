from plugins.client import Client

@bot.on_message(filters.command('start') & filters.private)
def command1(bot, message):
    bot.send_message(message.chat.id, "Hi, This Is A Test Bot")

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
