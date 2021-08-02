from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from ..screenshotbot import ScreenShotBot


@ScreenShotBot.on_message(filters.private & filters.command("start"))
async def start(c, m, cb=False):
    BUTTONS = [[
        InlineKeyboardButton("My Father 🧔", url="https://t.me/Ns_AnoNymous"),
        InlineKeyboardButton("Updates Channel 🔰", url="https://t.me/Ns_bot_updates")
        ],[
        InlineKeyboardButton("Source code 😎", url="https://github.com/odysseusmax/animated-lamp")
        ],[
        InlineKeyboardButton("Help ⁉️", callback_data="help"),
        InlineKeyboardButton("Settings ⚙", callback_data="set+settings")
        ],[
        InlineKeyboardButton("Close 📛", callback_data="close")
    ]]

    TEXT = "👋 Hi {m.from_user.mention},\n\nI'm Screenshot Generator Bot. I can provide screenshots, sample video from "
    TEXT += "your video files and also can trim. For more details check help.",

    if cb:
        await m.message.edit(
            text=TEXT
            reply_markup=InlineKeyboardMarkup(BUTTONS)
        )
    else:
        await m.reply_text(
            text=TEXT
            quote=True,
            reply_markup=InlineKeyboardMarkup(BUTTONS)
        )

@ScreenShotBot.on_callback_query(
    filters.create(lambda _, __, query: query.data.startswith("set")))
async def settings_cb(c, m):
