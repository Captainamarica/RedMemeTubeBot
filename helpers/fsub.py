from functools import wraps
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant

CAPTION_BTN = InlineKeyboardMarkup([[
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
    async def forcesub(_, message):
        try:
            await message._client.get_chat_member(-1001325914694, message.from_user.id)
        except UserNotParticipant:
            file_id = "CAADBQADOAcAAn_zKVSDCLfrLpxnhAI"
            return await client.send_sticker(message.chat.id, file_id) 
            await message.reply_text(
            text="""
            """,
            reply_markup=CAPTION_BTN,
            disable_web_page_preview=True) 
        return await func(_, message)    
    return sz_message
