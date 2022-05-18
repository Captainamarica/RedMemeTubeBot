from functools import wraps
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant

FORCESUB_BUTTONS = InlineKeyboardMarkup([[
                 InlineKeyboardButton('Join Here - MemeHub Telegram 🇱🇰', url=f"https://t.me/{force_subchannel}")
                 ],
                 [
                 InlineKeyboardButton('🐞 ʀᴘᴏʀᴛ ʙᴜɢs 🐞', url=f"https://t.me/Imgishan")
                 ],
                 [
                 InlineKeyboardButton(text="♻️ Reload ♻️",callback_data="ref")
                 ]]
                  )

async def forcesub(bot, message):  
   if force_subchannel:
        try:
            user = await bot.get_chat_member(force_subchannel, message.from_user.id)
            if user.status == "kicked out":
                await message.reply_text("Yourt Banned")
                return 
        except UserNotParticipant:
            file_id = "CAADBQADOAcAAn_zKVSDCLfrLpxnhAI"
            await bot.send_sticker(message.chat.id, file_id)
            text = f"""
            **❌ Dear {message.from_user.mention}, Access Denied ❌**

Memehub eke nathuva Mokatada yako Botva Start Kare kkk😒😒
♻️Join and Try Again.♻️
            """,
            reply_markup = FORCESUB_BUTTONS
            await message.reply_text(
            text=text,
            reply_markup=reply_markup
            )
      return await func(bot, message)
return forcesub
