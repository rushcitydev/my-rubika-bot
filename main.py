import asyncio
import os
from fast_rub import Client, filters

TOKEN = os.environ.get("CIFFEE0TPEQWWLKUBSYRUQYNMHMUQRJAMUGHHOTPHKDQJATYJXPZCTKDVQEKPJQX")

async def main():
    bot = Client(TOKEN)

    @bot.on_message(filters.text("سلام"))
    async def say_hello(msg):
        await msg.reply("سلام داداش، ربات وصله! ⚡")

    await bot.run()

if __name__ == "__main__":
    asyncio.run(main())
