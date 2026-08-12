#
# Copyright (C) 2026-present by Sora Music.
#
# This file is part of the < https://github.com/pratikNexvault/kartikmusic > project.
#

from pyrogram import filters, types

from KartikMusic import Kartik, app, db, lang
from KartikMusic.helpers import can_manage_vc


@app.on_message(filters.command(["skip", "next"]) & filters.group & ~app.bl_users)
@lang.language()
@can_manage_vc
async def _skip(_, m: types.Message):
    if not await db.get_call(m.chat.id):
        return await m.reply_text(m.lang["not_playing"])

    await Kartik.play_next(m.chat.id)
    await m.reply_text(m.lang["play_skipped"].format(m.from_user.mention))
