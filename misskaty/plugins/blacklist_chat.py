from pyrogram import filters
from pyrogram.types import Message

from misskaty import app
from misskaty.vars import SUDO as SUDOERS

from misskaty.ultis_ex.decorators.errors import capture_err
from misskaty.ultis_ex.database.dbfunctions import (
    blacklist_chat,
    blacklisted_chats,
    whitelist_chat,
)


@app.on_message(filters.command("blacklist_chat") & filters.user(SUDOERS))
@capture_err
async def blacklist_chat_func(_, message: Message):
    if len(message.command) != 2:
        return await message.reply_text(
            "**Usage:**\n/blacklist_chat [CHAT_ID]"
        )
    chat_id = int(message.text.strip().split()[1])
    if chat_id in await blacklisted_chats():
        return await message.reply_text("Chat is already blacklisted.")
    blacklisted = await blacklist_chat(chat_id)
    if blacklisted:
        return await message.reply_text(
            "Chat has been successfully blacklisted"
        )
    await message.reply_text("Something wrong happened, check logs.")


@app.on_message(filters.command("whitelist_chat") & filters.user(SUDOERS))
@capture_err
async def whitelist_chat_func(_, message: Message):
    if len(message.command) != 2:
        return await message.reply_text(
            "**Usage:**\n/whitelist_chat [CHAT_ID]"
        )
    chat_id = int(message.text.strip().split()[1])
    if chat_id not in await blacklisted_chats():
        return await message.reply_text("Chat is already whitelisted.")
    whitelisted = await whitelist_chat(chat_id)
    if whitelisted:
        return await message.reply_text(
            "Chat has been successfully whitelisted"
        )
    await message.reply_text("Something wrong happened, check logs.")


@app.on_message(filters.command("blacklisted_chats") & filters.user(SUDOERS))
@capture_err
async def blacklisted_chats_func(_, message: Message):
    text = ""
    for count, chat_id in enumerate(await blacklisted_chats(), 1):
        try:
            title = (await app.get_chat(chat_id)).title
        except Exception:
            title = "Private"
        text += f"**{count}. {title}** [`{chat_id}`]\n"
    if text == "":
        return await message.reply_text("No blacklisted chats found.")
    await message.reply_text(text)
