from pyrogram import Client, filters
from Plugins.Config import Config

bot = Client(
  "My First Project"
  bot_token=Config.BOT_TOKEN,
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
)
