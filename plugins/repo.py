import asyncio

from BADMUSIC import app
from pyrogram import filters
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

@app.on_message(filters.command(["repo"]))
async def start(client: Client, message: Message):
    await message.reply_video(
        video=f"https://telegra.ph/file/bda2c51bd00c8f4710b04.mp4",
        caption=f"❤️ ʜᴇʏ {message.from_user.mention}",
        reply_markup=InlineKeyboardMarkup(
            [
               [
            InlineKeyboardButton(
                text="☆ ᴏᴡɴᴇʀ 💗 ", url=f"https://t.me/Fidha_Mine"
            ),
            InlineKeyboardButton(
                text="☆ ɢʀᴏᴜᴘ 💗", url=f"https://t.me/THE_ARCHITECT_II"
            ),
        ],
          [
            InlineKeyboardButton(
                text="☆ ᴄʜᴀɴɴᴇʟ 💗 ", url=f"https://t.me/THE_ARCHITECT_II"
            ),
            InlineKeyboardButton(
                text="☆ ʀᴇᴘᴏ 💗", url=f"https://github.com"
            ),
        ],
                [
                    InlineKeyboardButton(
                        "✯ ᴄʟᴏsᴇ ✯", callback_data="close"
                    )
                ],
            ]
        )
    )
  
