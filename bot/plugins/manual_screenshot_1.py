from pyrogram import filters
from pyrogram.types import ForceReply

from bot.screenshotbot import ScreenShotBot


@ScreenShotBot.on_callback_query(
    filters.create(lambda _, __, query: query.data.startswith("mscht"))
)
async def _(c, m):
    await m.answer()
    dur = m.message.text.markdown.split("\n")[-1]
    await m.message.delete(True)
    await c.send_message(
        m.from_user.id,
        f"""#ᴍᴀɴᴜᴀʟ_sᴄʀᴇᴇɴsʜᴏᴛ
        
{dur}

Nᴏᴡ sᴇɴᴅ ʏᴏᴜʀ ʟɪsᴛ ᴏғ sᴇᴄᴏɴᴅs sᴇᴘᴀʀᴀᴛᴇᴅ ʙʏ ,(ᴄᴏᴍᴍᴀ).
Eɢ: 𝟶,𝟷𝟶,𝟺𝟶,𝟼𝟶,𝟷𝟸𝟶.

Tʜɪs ᴡɪʟʟ ɢᴇɴᴇʀᴀᴛᴇ sᴄʀᴇᴇɴsʜᴏᴛs ᴀᴛ 𝟶, 𝟷𝟶, 𝟺𝟶, 𝟼𝟶, ᴀɴᴅ 𝟷𝟸𝟶 sᴇᴄᴏɴᴅs.

𝟷. Tʜᴇ ʟɪsᴛ ᴄᴀɴ ʜᴀᴠᴇ ᴀ ᴍᴀxɪᴍᴜᴍ ᴏғ 𝟷𝟶 ᴠᴀʟɪᴅ ᴘᴏsɪᴛɪᴏɴs.
𝟸. Tʜᴇ ᴘᴏsɪᴛɪᴏɴ ʜᴀs ᴛᴏ ʙᴇ ɢʀᴇᴀᴛᴇʀ ᴛʜᴀɴ ᴏʀ ᴇǫᴜᴀʟ ᴛᴏ 𝟶, ᴏʀ ʟᴇss ᴛʜᴀɴ ᴛʜᴇ ᴠɪᴅᴇᴏ ʟᴇɴɢᴛʜ ɪɴ ᴏʀᴅᴇʀ ᴛᴏ ʙᴇ ᴠᴀʟɪᴅ.""",
        reply_to_message_id=m.message.reply_to_message.message_id,
        reply_markup=ForceReply(),
    )
