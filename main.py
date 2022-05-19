import logging

from pyrogram import Client, idle

from vars import var

logging.getLogger("pyrogram").setLevel(logging.INFO)

#Client
Client = Client(
    "Memehub Bot",
    api_id=var.API_ID,
    api_hash=var.API_HASH,
    bot_token=var.BOT_TOKEN,
    plugins=dict(root="plugins"),
)


Client.start()
uname = (Client.get_me()).username
print(f"@{uname} Deployed Successfully !")

idle()
