#!/usr/bin/env python3

import disnake
import os

from disnake.ext import commands

TOKEN = os.getenv("VERHU_TOKEN")

intents = disnake.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix=commands.when_mentioned_or("verhu ", "v "), intents=intents, sync_commands_debug=True)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    print("------")

bot.load_extension("cogs.roll")
bot.load_extension("cogs.psalm")
bot.load_extension("cogs.character")

bot.run(TOKEN)
