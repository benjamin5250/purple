## Bikash Halder & Aditya Halder

from Bikash import app
from pyrogram import filters


@app.on_message(filters.command("id"))
def ids(_, message):
    reply = message.reply_to_message
    if reply:
        message.reply_text(
            f"🥀 𝐃𝐞𝐚𝐫 𝐔𝐬𝐞𝐫 𝐓𝐡𝐢𝐬 𝐈𝐬 𝐔𝐬𝐞𝐫 𝐈𝐧𝐟𝐨 𝐒𝐞𝐞 𝐁𝐞𝐥𝐨𝐰 𝐈𝐧𝐟𝐨 🥀 \n\n🌿 𝐔𝐬𝐞𝐫 𝐈𝐝 🌿: `{reply.from_user.id}`\n\n🥀 𝐅𝐢𝐫𝐬𝐭 𝐍𝐚𝐦𝐞 🍁 : {reply.from_user.first_name} \n\n🥀 𝐔𝐬𝐞𝐫𝐍𝐚𝐦𝐞 🍁 : `@{reply.from_user.username}`\n🥀 𝐂𝐡𝐚𝐭 𝐈𝐝 🥀 : `{message.chat.id}` \n\n𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐁𝐲 [𝚂𝙰𝙽𝙶𝙻𝙸𝚈𝙰𝙽𝙰](https://t.me/SafestPlaceDiscussion)"
        )
    else:
        message.reply(
            f"🥀 𝐃𝐞𝐚𝐫 𝐔𝐬𝐞𝐫 𝐓𝐡𝐢𝐬 𝐈𝐬 𝐘𝐨𝐮𝐫 𝐈𝐧𝐟𝐨 𝐒𝐞𝐞 𝐁𝐞𝐥𝐨𝐰 𝐈𝐧𝐟𝐨 🥀 \n\n**🥀 𝐘𝐨𝐮𝐫 𝐈𝐝 🥀**: `{message.from_user.id}`\n**🥀 𝐂𝐡𝐚𝐭 𝐈𝐝 🥀**: `{message.chat.id}`"
        )
