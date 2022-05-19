


from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


from .start import REPLY_MARKUP, START


@Client.on_callback_query()  
async def tgm(bot, update):  
    if update.data == "add": 
        await update.answer(
             text="♻️Adding Soon.....",
        )
    elif update.data == "bak":
         await update.message.edit_text(
             text=HELP_STRING,
             reply_markup=CLOSE_BUTTON,
             disable_web_page_preview=True
         )
         await update.answer(
             text="👻 ʙᴀᴍᴄᴋ 👻",
         )
    elif update.data == "bak":
         await update.message.delete()
         await bot.delete_message(update.chat.id, update.message.id)
    elif update.data == "hlp":
         await update.message.edit_text(
             text=HELP_STRING,
             reply_markup=CLOSE_BUTTON,
             disable_web_page_preview=True
         )
         await update.answer(
             text="👻 ʜᴇᴍʟᴘ 👻",
         )
    elif update.data == "cloc":
         await update.message.delete()