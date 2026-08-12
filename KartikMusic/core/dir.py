#
# Copyright (C) 2026-present by Sora Music.
#
# This file is part of the < https://github.com/pratikNexvault/kartikmusic > project.
#

import shutil
from pathlib import Path

from KartikMusic import logger


def ensure_dirs():
    """
    Ensure that the necessary directories exist.
    """
    if not shutil.which("deno") or not shutil.which("ffmpeg"):
        raise RuntimeError(
            "Deno and FFmpeg must be installed and accessible in the system PATH."
        )

    for dir in ["cache", "downloads"]:
        Path(dir).mkdir(parents=True, exist_ok=True)
    logger.info("Cache directories updated.")
