from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import random
from bot.config import Config
from ..screenshotbot import ScreenShotBot

PICS = [
 "https://telegra.ph/file/08834517d04e99c969615.jpg"
]

@ScreenShotBot.on_message(filters.private & filters.command("start"))
async def start(c, m, cb=False):
    owner_id = Config.AUTH_USERS[0]
    username = 'MR_HKZ_TG'
    mention = '[𝙼𝚛. 𝙷𝙺𝚉 𝚃𝙶](https://t.me/MR_HKZ_TG)'
    try:
        owner = await c.get_users(owner_id)
        username = owner.username if owner.username else 'Ns_AnoNymous'
        mention = owner.mention(style="md")
    except Exception as e:
        print(e)

    BUTTONS = [[
        InlineKeyboardButton("Dᴇᴠᴇʟᴏᴘᴇʀ 👨‍💻", url=f"https://t.me/{username}"),
        InlineKeyboardButton("Uᴘᴅᴀᴛᴇs Cʜᴀɴɴᴇʟ 🔰", url="https://telegram.dog/HKZTG")
        ],[
        InlineKeyboardButton("Sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ 😎", url="https://github.com/Ns-AnoNymouS/animated-lamp")
        ],[
        InlineKeyboardButton("Hᴇʟᴘ 🛠", callback_data="help"),
        InlineKeyboardButton("Sᴇᴛᴛɪɴɢs ⚙", callback_data="set+settings")
        ],[
        InlineKeyboardButton("Cʟᴏsᴇ 📛", callback_data="close")
    ]]

    if cb:
        try:
            await m.message.edit_photo(
                photo=random.choice(PICS),
                caption=f"""Hᴇʟʟᴏ 👋,

I'ᴍ Sᴄʀᴇᴇɴsʜᴏᴛ Gᴇɴᴇʀᴀᴛᴏʀ Bᴏᴛ. I ᴄᴀɴ ᴘʀᴏᴠɪᴅᴇ sᴄʀᴇᴇɴsʜᴏᴛs ʏᴏᴜʀ ᴠɪᴅᴇᴏ ғɪʟᴇs. Fᴏʀ ᴍᴏʀᴇ ᴅᴇᴛᴀɪʟs ᴄʜᴇᴄᴋ ʜᴇʟᴘ

Mᴀɪɴᴛᴀɪɴᴇᴅ Bʏ: {mention}""",
                reply_markup=InlineKeyboardMarkup(BUTTONS)
            )
        except:
            pass
    else:
        await m.reply_photo(
            photo=random.choice(PICS),
            caption=f"""Hᴇʟʟᴏ 👋,

I'ᴍ Sᴄʀᴇᴇɴsʜᴏᴛ Gᴇɴᴇʀᴀᴛᴏʀ Bᴏᴛ. I ᴄᴀɴ ᴘʀᴏᴠɪᴅᴇ sᴄʀᴇᴇɴsʜᴏᴛs ʏᴏᴜʀ ᴠɪᴅᴇᴏ ғɪʟᴇs. Fᴏʀ ᴍᴏʀᴇ ᴅᴇᴛᴀɪʟs ᴄʜᴇᴄᴋ ʜᴇʟᴘ

Mᴀɪɴᴛᴀɪɴᴇᴅ Bʏ: {mention}""",
            quote=True,
            reply_markup=InlineKeyboardMarkup(BUTTONS)
        )


# i generally liked to use regex filters for callback 
# but since odysseusmax used lambda i am also using the same
@ScreenShotBot.on_callback_query(
    filters.create(lambda _, __, query: query.data.startswith("home"))
)
async def home_cb(c, m):
    await m.answer()
    await start(c, m, True)


@ScreenShotBot.on_callback_query(
    filters.create(lambda _, __, query: query.data.startswith("close"))
)
async def close_cb(c, m):
    try:
        await m.message.delete()
        await m.message.reply_to_message.delete()
    except:
        pass
