from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import random
from bot.screenshotbot import ScreenShotBot
from bot.config import Config


PICS = [
 "https://telegra.ph/file/08834517d04e99c969615.jpg"
]

BUTTONS = [[
    InlineKeyboardButton('Hᴏᴍᴇ 🏡', callback_data='home'),
    InlineKeyboardButton('Cʟᴏsᴇ 📛', callback_data='close')
]]

HELP_TEXT = """
Hɪ {mention}. Wᴇʟᴄᴏᴍᴇ ᴛᴏ Sᴄʀᴇᴇɴsʜᴏᴛ Gᴇɴᴇʀᴀᴛᴏʀ Bᴏᴛ. Yᴏᴜ ᴄᴀɴ ᴜsᴇ ᴍᴇ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ:

    𝟷. Sᴄʀᴇᴇɴsʜᴏᴛs.
    𝟸. Sᴀᴍᴘʟᴇ Vɪᴅᴇᴏ.
    𝟹. Tʀɪᴍ Vɪᴅᴇᴏ.

👉 I sᴜᴘᴘᴏʀᴛ ᴀɴʏ ᴋɪɴᴅ ᴏғ ᴛᴇʟᴇɢʀᴀᴍ ᴠɪᴅᴇᴏ ғɪʟᴇ (sᴛʀᴇᴀᴍɪɴɢ ᴠɪᴅᴇᴏ ᴏʀ ᴅᴏᴄᴜᴍᴇɴᴛ ᴠɪᴅᴇᴏ ғɪʟᴇs) ᴘʀᴏᴠɪᴅᴇᴅ ɪᴛ ʜᴀs ᴘʀᴏᴘᴇʀ ᴍɪᴍᴇ-ᴛʏᴘᴇ ᴀɴᴅ ɪs ɴᴏᴛ ᴄᴏʀʀᴜᴘᴛᴇᴅ.
👉 I ᴀʟsᴏ sᴜᴘᴘᴏʀᴛ Sᴛʀᴇᴀᴍɪɴɢ URLs. Tʜᴇ URL sʜᴏᴜʟᴅ ʙᴇ ᴀ sᴛʀᴇᴀᴍɪɴɢ URL, ɴᴏɴ IP sᴘᴇᴄɪғɪᴄ, ᴀɴᴅ sʜᴏᴜʟᴅ ʀᴇᴛᴜʀɴ ᴘʀᴏᴘᴇʀ ʀᴇsᴘᴏɴsᴇ ᴄᴏᴅᴇs.
Jᴜsᴛ sᴇɴᴅ ᴍᴇ ᴛʜᴇ ᴛᴇʟᴇɢʀᴀᴍ ғɪʟᴇ ᴏʀ ᴛʜᴇ sᴛʀᴇᴀᴍɪɴɢ URL.

Sᴇᴇ /settings ᴛᴏ ᴄᴏɴғɪɢᴜʀᴇ ʙᴏᴛ's ʙᴇʜᴀᴠɪᴏʀ.
Usᴇ /set_watermark ᴛᴏ sᴇᴛ ᴄᴜsᴛᴏᴍ ᴡᴀᴛᴇʀᴍᴀʀᴋs ᴛᴏ ʏᴏᴜʀ sᴄʀᴇᴇɴsʜᴏᴛs.

Gᴇɴᴇʀᴀʟ FAQ.

👉 Iғ ᴛʜᴇ ʙᴏᴛ ᴅᴏsᴇɴ'ᴛ ʀᴇsᴘᴏɴᴅ ᴛᴏ ᴛᴇʟᴇɢʀᴀᴍ ғɪʟᴇs ʏᴏᴜ ғᴏʀᴡᴀʀᴅ, ғɪʀsᴛ ᴄʜᴇᴄᴋ /start ᴀɴᴅ ᴄᴏɴғɪʀᴍ ʙᴏᴛ ɪs ᴀʟɪᴠᴇ. Tʜᴇɴ ᴍᴀᴋᴇ sᴜʀᴇ ᴛʜᴇ ғɪʟᴇ ɪs ᴀ ᴠɪᴅᴇᴏ ғɪʟᴇ ᴡʜɪᴄʜ sᴀᴛɪsғɪᴇs ᴀʙᴏᴠᴇ ᴍᴇɴᴛɪᴏɴᴇᴅ ᴄᴏɴᴅɪᴛɪᴏɴs.
👉 Iғ ʙᴏᴛ ʀᴇᴘʟɪᴇs 😟 Sᴏʀʀʏ! I ᴄᴀɴɴᴏᴛ ᴏᴘᴇɴ ᴛʜᴇ ғɪʟᴇ., ᴛʜᴇ ғɪʟᴇ ᴍɪɢʜᴛ ʙᴇ ᴄᴜʀʀᴜᴘᴛᴇᴅ ᴏʀ ɪs ᴍᴀʟғᴏʀᴍᴀᴛᴛᴇᴅ.

Iғ ɪssᴜᴇs ᴘᴇʀsɪsᴛs ᴄᴏɴᴛᴀᴄᴛ ᴍʏ ғᴀᴛʜᴇʀ.

{admin_notification}
"""
ADMIN_NOTIFICATION_TEXT = (
    "Sɪɴᴄᴇ ʏᴏᴜ ᴀʀᴇ ᴏɴᴇ ᴏғ ᴛʜᴇ ᴀᴅᴍɪɴs, ʏᴏᴜ ᴄᴀɴ ᴄʜᴇᴄᴋ /admin ᴛᴏ ᴠɪᴇᴡ ᴛʜᴇ ᴀᴅᴍɪɴ ᴄᴏᴍᴍᴀɴᴅs."
)


@ScreenShotBot.on_message(filters.private & filters.command("help"))
async def help_(c, m):

    await m.reply_photo(
        photo=random.choice(PICS),
        caption=HELP_TEXT.format(
            mention=m.from_user.mention,
            admin_notification=ADMIN_NOTIFICATION_TEXT
            if m.from_user.id in Config.AUTH_USERS
            else "",
        ),
        reply_markup=InlineKeyboardMarkup(BUTTONS),
        quote=True,
    )


@ScreenShotBot.on_callback_query(
    filters.create(lambda _, __, query: query.data.startswith("help"))
)
async def help_cb(c, m):
    await m.answer()
    await m.message.edit(
        text=HELP_TEXT.format(
            mention=m.from_user.mention,
            admin_notification=ADMIN_NOTIFICATION_TEXT
            if m.from_user.id in Config.AUTH_USERS
            else "",
        ),
        reply_markup=InlineKeyboardMarkup(BUTTONS)
    )
