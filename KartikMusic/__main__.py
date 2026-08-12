#
# Copyright (C) 2026-present by Sora Music.
#
# This file is part of the < https://github.com/pratikNexvault/kartikmusic > project.
#

import asyncio
import importlib
import traceback

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

    print(f"[DEBUG] Dispatcher running: {getattr(app.dispatcher, 'running', 'N/A')}", flush=True)
    print(f"[DEBUG] Dispatcher polling: {getattr(app.dispatcher, '_polling', 'N/A')}", flush=True)
    logger.info(f"Dispatcher running: {getattr(app.dispatcher, 'running', 'N/A')}")
    logger.info(f"Dispatcher polling: {getattr(app.dispatcher, '_polling', 'N/A')}")

    # Add exception handler for background tasks
    def handle_exception(loop, context):
        logger.error(f"Background task exception: {context}")
        if "exception" in context:
            logger.error(f"Exception: {context['exception']}")
            traceback.print_exception(
                type(context["exception"]),
                context["exception"],
                context["exception"].__traceback__,
            )

    loop = asyncio.get_running_loop()
    loop.set_exception_handler(handle_exception)
    print("[DEBUG] Exception handler set", flush=True)


async def shutdown():
    await stop()


if __name__ == "__main__":
    app.run(startup(), shutdown())
