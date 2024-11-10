from emojis import decode
from pyrogram.types import Message

from misskaty import app as pgram
from misskaty.ultis_ex.wmilia_m.users_mongo import GetChatName


async def GetChat(chat_id: int):
    """This function return chat_title of the given chat_id from the database of the bot.

    Args:
        chat_id (int): chat_id: message.chat.id

    Returns:
        [type]: chat's title
    """
    if (await GetChatName(chat_id)) is not None:
        chat_title = await GetChatName(chat_id)
        return chat_title
    else:
        await pgram.send_message(
            chat_id=chat_id,
            text=(
                f"I couldn't find the chat in my database. Please execute /forcecachechat here to make me be able to store your chat's data!"
            ),
        )
        return


async def get_text_reason(message: Message) -> str:
    """This function returns text, and the reason of the user's arguments

    Args:
        message (Message): Message

    Returns:
        [str]: text, reason
    """
    text = decode(message.text)
    index_finder = [x for x in range(len(text)) if text[x] == '"']
    if len(index_finder) >= 2:
        text1 = text[index_finder[0] + 1 : index_finder[1]]
        reason = text[index_finder[1] + 2 :]
        if not reason:
            reason = None
    else:
        text1 = message.text.split()[1]
        reason = " ".join(message.text.split()[2:])
        if not reason:
            reason = None

    return (text1, reason)
