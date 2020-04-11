import subprocess

import discord
from discord.ext.commands import Bot
from discord.ext import commands
from mcstatus import MinecraftServer

import asyncio


Client = discord.Client()
client = commands.Bot(command_prefix = "!")


@client.event
async def on_ready():
    print("Bot is ready!")


with open("token.txt", "r") as f:
    lines = f.readlines()
    token = lines[0].strip()

client.run(token)
