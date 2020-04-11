import subprocess

import discord
from discord.ext.commands import Bot
from discord.ext import commands
from mcstatus import MinecraftServer

import asyncio


Client = discord.Client()
client = commands.Bot(command_prefix = "!")

client.remove_command("help")


def player_list(input):
    index = input.find("[")

    if index == -1:
        return []

    lst_string = input[index+1:-4]
    lst = lst_string.split(", ")
    lst = [s.split(" ")[0][2:] for s in lst]

    return lst


def server_lookup(ip):
    server = MinecraftServer.lookup(ip)
    status = server.status()
    player_count = status.players.online

    output = str(subprocess.check_output("mcstatus " + str(ip) + " status",
                 shell=True))
    players_online = player_list(output)

    if player_count == 0:
        reply = "0 players."
    elif player_count == 1:
        reply = str(player_count) + " player:" + "```" + "\n" + "\n".join(players_online) + "\n" + "```"
    else:
        reply = str(player_count) + " players:" + "```" + "\n" + "\n".join(players_online) + "\n" + "```"

    return reply


@client.event
async def on_ready():
    print("Bot is ready!")


@client.command()
async def tu(ctx):
    response = server_lookup("Vextossup.join-mc.net")

    await ctx.send(response)


@client.command()
async def tt(ctx):
    response = server_lookup("51.161.120.109:25616")

    await ctx.send(response)


@client.command()
async def sa(ctx):
    response = server_lookup("sackattack.join-game.net")

    await ctx.send(response)


@client.command()
async def help(ctx):
    reply = "```\n" + "!tu \t Toss Up" + "\n" + "!tt \t Tower Takeover" + "\n" + "!sa \t Sack Attack" + "\n```"

    await ctx.send(reply)


with open("token.txt", "r") as f:
    lines = f.readlines()
    token = lines[0].strip()

client.run(token)
