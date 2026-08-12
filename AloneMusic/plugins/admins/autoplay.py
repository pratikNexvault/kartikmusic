#
# Copyright (C) 2021-2022 by TheAloneteam@Github, < https://github.com/TheAloneTeam >.
#
# This file is part of < https://github.com/TheAloneTeam/AloneMusic > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TheAloneTeam/AloneMusic/blob/master/LICENSE >
# All rights reserved.

from pyrogram import filters
from pyrogram.types import Message

from AloneMusic import app
from AloneMusic.utils.database import get_autoplay, set_autoplay
from AloneMusic.utils.decorators import AdminRightsCheck
from AloneMusic.utils.inline import close_markup
from config import BANNED_USERS


@app.on_message(filters.command("autoplay") & filters.group & ~BANNED_USERS)
@AdminRightsCheck
async def autoplay_cmd(client, message: Message, _, chat_id):
    usage = "**Usage:**\n/autoplay [enable|disable]"
    if len(message.command) < 2:
        return await message.reply_text(usage, reply_markup=close_markup(_))
    state = message.text.split(None, 1)[1].strip().lower()
    if state in ["enable", "on"]:
        await set_autoplay(chat_id, True)
        return await message.reply_text(
            f"✅ Autoplay **enabled** by {message.from_user.mention}\n\nWhen the queue finishes, a related song will play automatically.",
            reply_markup=close_markup(_),
        )
    elif state in ["disable", "off"]:
        await set_autoplay(chat_id, False)
        return await message.reply_text(
            f"❌ Autoplay **disabled** by {message.from_user.mention}",
            reply_markup=close_markup(_),
        )
    return await message.reply_text(usage, reply_markup=close_markup(_))
