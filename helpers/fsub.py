from functools import wraps
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant

force_subchannel = "Memehubtgsl"

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

def ForceSub(func):
    @wraps(func)
    async def force(_, message):
        try:
            await message._client.get_chat_member(-1001210985373, message.from_user.id)
        except UserNotParticipant:
            return await message.reply_text(
            text=f"""
**❌ Dear {message.from_user.mention}, Access Denied ❌**
Memehub eke nathuva Mokatada yako Botva Start Kare kkk😒😒
♻️Join and Try Again.♻️
            """,
            reply_markup=CAPTION_BTN,
            disable_web_page_preview=True) 
        return await func(_, message)    
    return force
