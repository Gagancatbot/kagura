from pyrogram import filters
from YorForger import pbot

@pbot.on_message(filters.command(['void']))
async def void(_, message):
    caption = f"**Welcome to [【V๏ɪ፝֟𝔡】Network](https://t.me/voidxnetwork)** \n\n◈ Void is an anime based Community with a motive to spread love and peace around telegram. Go through the channel and join the Community if it draws your attention. ◈"

    await message.reply_photo(photo=PHOTO, caption=caption)


__help__ = """
 ──「Void Network」──                         
 
❂ /void: Get information about our community! using it in groups may create promotion so we don't support using it in groups."""
   
__mod_name__ = "【ᴠᴏɪᴅ】"