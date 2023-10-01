from pyrogram.types import (InlineQueryResultArticle,
                            InputTextMessageContent)

answer = []

answer.extend(
    [
        InlineQueryResultArticle(
            title="⏸️ 𝐏𝐚𝐮𝐬𝐞 ⏸️",
            description=f"𝐏𝐚𝐮𝐬𝐞 𝐓𝐡𝐞 𝐂𝐮𝐫𝐫𝐞𝐧𝐭 𝐌𝐮𝐬𝐢𝐜.",
            thumb_url="https://telegra.ph/file/abadfa45600f81471a20d.jpg",
            input_message_content=InputTextMessageContent("/pause"),
        ),
        InlineQueryResultArticle(
            title="⏹️ 𝐑𝐞𝐬𝐮𝐦𝐞 ⏹️",
            description=f"𝐑𝐞𝐬𝐮𝐦𝐞 𝐓𝐡𝐞 𝐏𝐚𝐮𝐬𝐞𝐝 𝐌𝐮𝐬𝐢𝐜.",
            thumb_url="https://telegra.ph/file/5535164d77433ff7a1e49.mp4",
            input_message_content=InputTextMessageContent("/resume"),
        ),
        InlineQueryResultArticle(
            title="⏩ 𝐒𝐤𝐢𝐩 ⏩",
            description=f"𝐒𝐤𝐢𝐩 𝐓𝐡𝐞 𝐂𝐮𝐫𝐫𝐞𝐧𝐭 𝐌𝐮𝐬𝐢𝐜 & 𝐏𝐥𝐚𝐲 𝐍𝐞𝐱𝐭 𝐌𝐮𝐬𝐢𝐜",
            thumb_url="https://telegra.ph/file/4d7ccb00983c91e76faa5.mp4",
            input_message_content=InputTextMessageContent("/skip", "/next"),
        ),
        InlineQueryResultArticle(
            title="📴 𝐄𝐧𝐝 📴",
            description="𝐄𝐧𝐝 𝐓𝐡𝐞 𝐂𝐮𝐫𝐫𝐞𝐧𝐭 𝐏𝐥𝐚𝐲𝐢𝐧𝐠 𝐌𝐮𝐬𝐢𝐜.",
            thumb_url="https://telegra.ph/file/17af76e737aae8cd5de1f.jpg",
            input_message_content=InputTextMessageContent("/end"),
        ),
        InlineQueryResultArticle(
            title="🔉 𝐒𝐡𝐮𝐟𝐟𝐥𝐞 🔉",
            description="𝐒𝐡𝐮𝐟𝐟𝐥𝐞 𝐓𝐡𝐞 𝐂𝐮𝐫𝐫𝐞𝐧𝐭 𝐌𝐮𝐢𝐜.",
            thumb_url="https://te.legra.ph/file/3810eb9a72fd36c0aed50.jpg",
            input_message_content=InputTextMessageContent("/shuffle"),
        ),
        InlineQueryResultArticle(
            title="🔈 𝐋𝐨𝐨𝐩 🔈",
            description="𝐋𝐨𝐨𝐩 𝐓𝐡𝐞 𝐏𝐥𝐚𝐲𝐢𝐧𝐠 𝐌𝐮𝐬𝐢𝐜 .",
            thumb_url="https://te.legra.ph/file/d35e187e613d1b6cbfb07.jpg",
            input_message_content=InputTextMessageContent("/loop 3"),
        ),
    ]
)
