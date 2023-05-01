from pyrogram import filters

from config import HANDLER, OWNER_ID
from PandapiesUserBot import Pandapies


@Pandapies.on_message(filters.command("join", prefixes=HANDLER) & filters.user(OWNER_ID))
def join_chat(_, m):
    if len(m.command) < 2:
        m.reply_text("ɢɪᴠᴇ ᴀ ᴊᴏɪɴ ɢʀᴏᴜᴘ ᴜsᴇʀɴᴀᴍᴇ ᴏʀ ɪɴᴠɪᴛᴇ  ʟɪɴᴋ")
        return
    link = m.text.split(" ")[1]
    Pandapies.join_chat(link)
    chat = Pandapies.get_chat(link)
    name = chat.title
    m.reply_text(f"Successfully joined {name}")


@Pandapies.on_message(filters.command("leave", prefixes=HANDLER) & filters.user(OWNER_ID))
def leave_chat(_, m):
    if len(m.command) < 2:
        m.reply_text("ɢɪᴠᴇ ᴀ ʟᴇғᴛ ɢʀᴏᴜᴘ ᴜsᴇʀɴᴀᴍᴇ ᴏʀ ɪɴᴠɪᴛᴇ  ʟɪɴᴋ")
        return
    link = m.text.split(" ")[1]
    Pandapies.leave_chat(link)
    chat = Pandapies.get_chat(link)
    name = chat.title
    m.reply_text(f"Successfully left {name}")
