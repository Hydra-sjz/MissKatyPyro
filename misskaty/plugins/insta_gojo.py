import requests
from pyrogram import Client, filters
from pyrogram.types import *
from misskaty import app
@app.on_message(filters.command(["insdl", "ig_gojo"]))
async def igdowngojoload(client, message):
    if len(message.command) < 2:
        return await message.reply_text("**Please Provide a Instagram Url 🤦‍♂️**")
    url = message.text.split(None, 1)[1]
    msg = await message.reply_text("📤")
    response = requests.get(f"https://horridapi.onrender.com/instadl?url={url}")
    data = response.json()

    if not data["STATUS"] == "OK":
        await message.reply_text("**Not An Instagram Url 🤷‍♂️**")
        await msg.delete()
        return

    result = data["result"]
    media = []
    if data["STATUS"] == "OK":
        for s in result:                
            if s["media"] == "image":
                media.append(InputMediaPhoto(media=s["url"]))
            else:
                media.append(InputMediaVideo(media=s["url"]))
            
        await message.reply_media_group(media=media) 
        await message.reply_photo_group(photo=media) 
        await msg.delete()
