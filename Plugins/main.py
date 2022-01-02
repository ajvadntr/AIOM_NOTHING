from plugins.client import Client

@bot.on_message(filters.command('start') & filters.private)
def command1(bot, message):
