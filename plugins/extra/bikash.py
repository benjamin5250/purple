from pyrogram import Client, filters

from Bikash import app
from Bikash.utils.bgtmusic.bk import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@app.on_message(
    filters.command("bikash")
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def bikash(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/f73af9a4ffe130a83d8d2.jpg",
        caption=f"""🥀 𝚂𝙰𝙽𝙶𝙻𝙸𝚈𝙰𝙽𝙰 𝐈𝐬 𝐎𝐰𝐧𝐞𝐫 𝐎𝐟 𝐌𝐮𝐬𝐢𝐜 𝐁𝐨𝐭 🌺, 𝐂𝐥𝐢𝐜𝐤 𝐁𝐞𝐥𝐨𝐰 𝐁𝐮𝐭𝐭𝐨𝐧 𝐅𝐨𝐫 𝐂𝐨𝐧𝐭𝐚𝐜𝐭 ♕ """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🥀 𝚂𝙰𝙽𝙶𝙻𝙸𝚈𝙰𝙽𝙰 🥀", url=f"https://t.me/SP_SANGLIYANA")
            ],          
            [
                    InlineKeyboardButton(
                        "🥀 GIOVANNI 🥀", url=f"https://t.me/GI0VANN1_420")
                ],
                [
                    InlineKeyboardButton(
                        "🥀 Pyar Sabhi Dhoka He 🥀", url=f"https://t.me/SP_SANGLIYANA"
                    ),
                    InlineKeyboardButton(
                        "🥀 𝐔𝐩𝐝𝐚𝐭𝐞𝐬 🥀", url=f"https://t.me/SafestPlaceDiscussion")
                ]
            ]
        ),
    )
