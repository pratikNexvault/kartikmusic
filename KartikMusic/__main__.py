#
# Copyright (C) 2026-present by Sora Music.
#
# This file is part of the < https://github.com/pratikNexvault/kartikmusic > project.
#

import asyncio
import importlib

from KartikMusic import Kartik, app, config, db, logger, stop, thumb, userbot, yt
from KartikMusic.plugins import all_modules


async def startup():
    await db.connect()
    await thumb.start()
    await app.boot()
    await userbot.boot()
    await Kartik.boot()

    for module in all_modules:
        importlib.import_module(f"KartikMusic.plugins.{module}")
    logger.info(f"Loaded {len(all_modules)} modules.")

    if config.COOKIES_URL:
        await yt.save_cookies(config.COOKIES_URL)

    sudoers = await db.get_sudoers()
    app.sudoers.update(sudoers)
    app.bl_users.update(await db.get_blacklisted())
    logger.info(f"Loaded {len(app.sudoers)} sudo users.")


async def shutdown():
    await stop()


if __name__ == "__main__":
    app.run(startup(), shutdown())
