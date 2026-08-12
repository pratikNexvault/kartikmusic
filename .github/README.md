<div align="center">

<h1>🎵 Sora Music 🎵</h1>

<b>A Powerful Telegram Music Bot for Group Voice Chats</b><br>
Stream high-quality audio and video with ease.

<p align="center">
    <a href="https://github.com/pratikNexvault/kartikmusic/stargazers"><img src="https://img.shields.io/github/stars/pratikNexvault/kartikmusic?color=blueviolet&logo=github&style=for-the-badge" alt="Stars"/></a>
    <a href="https://github.com/pratikNexvault/kartikmusic/network/members"><img src="https://img.shields.io/github/forks/pratikNexvault/kartikmusic?color=blueviolet&logo=github&style=for-the-badge" alt="Forks"/></a>
    <a href="https://github.com/pratikNexvault/kartikmusic/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue?style=for-the-badge" alt="License"/></a>
    <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Written%20in-Python-blue?style=for-the-badge&logo=python" alt="Python"/></a>
</p>

<img src="https://github.com/pratikNexvault/kartikmusic/blob/main/.github/anonx.jpg" width="100%" alt="Sora Music Banner">

</div>

<hr>

## 🚀 Features

- 🔊 **High Quality Audio:** Crystal clear sound for your voice chats.
- 🎬 **Video Playback:** Support for high-definition video streaming.
- 📜 **Queue Management:** Powerful and easy-to-use queue system.
- 🔄 **Autoplay:** Keeps the music going automatically.
- 🌍 **Multi-Language:** Supports 13+ languages.
- 🛠️ **Customizable:** Easy to configure for your own needs.

<hr>

## 🛠️ Deployment

### 💻 VPS / Local Deployment

Follow these steps to host the bot on your own server:

1. **Clone the Repo:**
   ```bash
   git clone https://github.com/pratikNexvault/kartikmusic && cd kartikmusic
   ```

2. **Install UV:**
   ```bash
   curl -Ls https://astral.sh/uv/install.sh | sh
   export PATH="$HOME/.local/bin:$PATH"
   ```

3. **Install Dependencies:**
   ```bash
   uv sync --frozen
   ```

4. **Configure Environment:**
   ```bash
   cp sample.env .env
   # Edit .env with your variables
   ```

5. **Start the Bot:**
   ```bash
   bash start
   ```

<hr>

## ⚙️ Configuration

Required environment variables:

| Variable | Description |
| :--- | :--- |
| `API_ID` | Your Telegram API ID from [my.telegram.org](https://my.telegram.org) |
| `API_HASH` | Your Telegram API Hash from [my.telegram.org](https://my.telegram.org) |
| `BOT_TOKEN` | Your Bot Token from [@BotFather](https://t.me/BotFather) |
| `MONGO_URL` | Your MongoDB connection string |
| `LOGGER_ID` | Your Log Group ID |
| `OWNER_ID` | Your Telegram User ID |
| `SESSION` | A Pyrogram String Session |

<hr>

## 📜 License

This project is licensed under the [MIT License](https://github.com/pratikNexvault/kartikmusic/blob/main/LICENSE).

---

<div align="center">
    <b>Made with ❤️ by Sora Music</b>
</div>
