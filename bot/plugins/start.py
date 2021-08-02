from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from ..screenshotbot import ScreenShotBot


@ScreenShotBot.on_message(filters.private & filters.command("start"))
async def start(c, m):

    await m.reply_text(
        text=f"👋 Hi there {m.from_user.mention}.\n\nI'm Screenshot Generator Bot. I can provide screenshots from "
        "your video files without downloading the entire file (almost instantly). For more details check /help.",
        quote=True,
        reply_markup=InlineKeyboardMarkup(
            [[
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
        ),
    )
