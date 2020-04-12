import asyncio

import discord
from discord.ext.commands import Bot
from discord.ext import commands
from mcstatus import MinecraftServer

from MinecraftServer import MinecraftServer



Client = discord.Client()
client = commands.Bot(command_prefix = "!")

client.remove_command("help")

serverTU = MinecraftServer("Vextossup.join-mc.net")
serverTT = MinecraftServer("51.161.120.109:25616")
serverSA = MinecraftServer("sackattack.join-game.net")


def format_response(response):
    count = response[0]
    players = response[1]

    if count == 0:
        reply = "0 players."
    elif count == 1:
        reply = str(count) + " player:" + "```" + "\n" + "\n".join(players) + "\n" + "```"
    else:
        reply = str(count) + " players:" + "```" + "\n" + "\n".join(players) + "\n" + "```"

    return reply


@client.event
async def on_ready():
    print("Bot is ready!")


@client.command()
async def tu(ctx):
    lookup = serverTU.server_lookup()
    response = format_response(lookup)

    await ctx.send(response)


@client.command()
async def tt(ctx):
    lookup = serverTT.server_lookup()
    response = format_response(lookup)

    await ctx.send(response)


@client.command()
async def sa(ctx):
    lookup = serverSA.server_lookup()
    response = format_response(lookup)

    await ctx.send(response)


@client.command()
async def help(ctx):
    reply = "```\n" + "!tu \t Toss Up" + "\n" + "!tt \t Tower Takeover" + "\n" + "!sa \t Sack Attack" + "\n```"

    await ctx.send(reply)


with open("token.txt", "r") as f:
    lines = f.readlines()
    token = lines[0].strip()

client.run(token)
