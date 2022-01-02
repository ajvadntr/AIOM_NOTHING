from plugins.client import Client

@bot.on_message(filters.command('start') & filters.private)
def command1(bot, message):
    bot.send_message(message.chat.id, "Hi, This Is A Test Bot")

@bot.on_message(filters.command('help'))
def command1(bot, message):
    message.replay_text("Their Is Nothing To Say")

@bot.on_message(filters.text)
def echobot(client, message):
    message.replay_text(message.text)

bot.run()
