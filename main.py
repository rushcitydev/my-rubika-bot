import asyncio
import os
from robka import Client

TOKEN = os.environ.get("RUBIKA_BOT_TOKEN")

async def main():
    if not TOKEN:
        print("❌ توکن پیدا نشد!")
        return

    print("✅ توکن پیدا شد. در حال اتصال...")
    bot = Client(TOKEN)

    @bot.on_message()
    async def echo(msg):
        if msg.text == "سلام":
            await msg.reply("سلام داداش! ربات وصله ⚡")

    print("🚀 ربات روشن شد...")
    await bot.run()

if __name__ == "__main__":
    asyncio.run(main())
