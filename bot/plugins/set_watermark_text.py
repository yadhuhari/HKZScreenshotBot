from pyrogram import filters

from bot.screenshotbot import ScreenShotBot
from bot.database import Database


db = Database()


@ScreenShotBot.on_message(filters.private & filters.command("set_watermark"))
async def _(c, m):

    if len(m.command) == 1:
        await m.reply_text(
            text="""Yᴏᴜ ᴄᴀɴ ᴀᴅᴅ ᴄᴜsᴛᴏᴍ ᴡᴀᴛᴇʀᴍᴀʀᴋ ᴛᴇxᴛ ᴛᴏ ᴛʜᴇ sᴄʀᴇᴇɴsʜᴏᴛs.

Usᴀɢᴇ: /set_watermark ᴛᴇxᴛ.
Tᴇxᴛ sʜᴏᴜʟᴅ ɴᴏᴛ Exᴄᴇᴇᴅ 𝟹𝟶 ᴄʜᴀʀᴀᴄᴛᴇʀs.""",
            quote=True
        )
        return

    watermark_text = " ".join(m.command[1:])
    if len(watermark_text) > 30:
        await m.reply_text(
            text=f"Tʜᴇ ᴡᴀᴛᴇʀᴍᴀʀᴋ ᴛᴇxᴛ ʏᴏᴜ ᴘʀᴏᴠɪᴅᴇᴅ (__{watermark_text}__) ɪs `{len(watermark_text)}` "
            "ᴄʜᴀʀᴀᴄᴛᴇʀs ʟᴏɴɢ! Yᴏᴜ ᴄᴀɴɴᴏᴛ sᴇᴛ ᴡᴀᴛᴇʀᴍᴀʀᴋ ᴛᴇxᴛ ɢʀᴇᴀᴛᴇʀ ᴛʜᴀɴ 𝟹𝟶 ᴄʜᴀʀᴀᴄᴛᴇʀs.",
            quote=True
        )
        return

    await db.update_watermark_text(m.chat.id, watermark_text)
    await m.reply_text(
        text=f"Yᴏᴜ ʜᴀᴠᴇ sᴜᴄᴄᴇssғᴜʟʟʏ sᴇᴛ __{watermark_text}__ ᴀs ᴡᴀᴛᴇʀᴍᴀʀᴋ ᴛᴇxᴛ. Fʀᴏᴍ ɴᴏᴡ ᴏɴ ᴛʜɪs ᴡɪʟʟ "
        "ʙᴇ ᴀᴘᴘʟɪᴇᴅ ᴛᴏ ʏᴏᴜʀ sᴄʀᴇᴇɴsʜᴏᴛs! Tᴏ ʀᴇᴍᴏᴠᴇ ᴡᴀᴛᴇʀᴍᴀʀᴋ ᴛᴇxᴛ sᴇᴇ /sᴇᴛᴛɪɴɢs.",
        quote=True
    )
