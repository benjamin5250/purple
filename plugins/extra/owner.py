from pyrogram import Client, filters

from Bikash import app
from Bikash.utils.bgtmusic.bk import command

from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@app.on_message(
    filters.command("owner")
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def owner(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/f73af9a4ffe130a83d8d2.jpg",
        caption=f"""🥀 𝐂𝐥𝐢𝐜𝐤 𝐇𝐞𝐫𝐞 𝐅𝐨𝐫 𝐂𝐨𝐧𝐭𝐚𝐜𝐭 𝐎𝐰𝐧𝐞𝐫.""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🥀 𝚂𝙰𝙽𝙶𝙻𝙸𝚈𝙰𝙽𝙰 🥀", url=f"https://t.me/SP_SANGLIYANA")
            ],          
           
        ),
    )
