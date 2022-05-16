from pyrogram import Client, filters



@Client.on_message(filters.regex("h") | filters.regex("H"))
async def regex(bot, message): 
    await message.reply_text(
        text="/leech"
    )
