import logging

from pyrogram import Client, idle

from vars import var

logging.getLogger("pyrogram").setLevel(logging.INFO)

MhubBot = Client(
    "Memehub_Bot",
    api_id=var.API_ID,
    api_hash=var.API_HASH,
    bot_token=var.BOT_TOKEN,
    plugins=dict(root="plugins"),
)

MhubBot.start()
uname = (MhubBot.get_me()).username
print(f"@{uname} Deployed Successfully !")

idle()
