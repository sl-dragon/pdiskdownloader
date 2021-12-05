import os
import logging
from pyrogram import filters, Client, idle
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from mega import Mega
from sample_config import Config

# mega client
mega = Mega()
m = mega.login()

# location
LOCATION = "./"

# logging
bot = Client(
   "MegaNz",
   api_id=Config.APP_ID,
   api_hash=Config.API_HASH,
   bot_token=Config.TG_BOT_TOKEN,
)
# mega download
@bot.on_message(filters.regex(pattern="https://mega.nz/") & filters.private)
async def meganz(_, message):
    input = message.text
    user = message.from_user.mention
    msg = await message.reply_text("📥 𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱𝗶𝗻𝗴 𝗬𝗼𝘂𝗿 𝗠𝗲𝗴𝗮 𝗹𝗶𝗻𝗸. 𝗣𝗹𝗲𝗮𝘀𝗲 𝘄𝗮𝗶𝘁...")
    try:
        file = m.download_url(input, LOCATION)
    except Exception as e:
        print(str(e))
        return await msg.edit("𝗢𝗼𝗽𝘀! 𝗬𝗼𝘂𝗿 𝗹𝗶𝗻𝗸 𝗶𝘀 𝗜𝗻𝘃𝗮𝗹𝗶𝗱.")
    await msg.edit("📤 𝗨𝗽𝗹𝗼𝗮𝗱𝗶𝗻𝗴...")
    cap = f"𝗨𝗽𝗹𝗼𝗮𝗱𝗲𝗱 𝗕𝘆 @AIODownloader_Bot"
    await bot.send_document(message.chat.id, file, caption=cap)
    await msg.delete()
    os.remove(file)

