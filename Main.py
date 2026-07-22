import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot {bot.user} ta readyyy!')

async def load():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')

async def main():
    async with bot: 
        await load()
        print(os.getcwd())
        print(os.listdir())
        await bot.start(os.getenv('TOKEN'))

import asyncio
asyncio.run(main())
