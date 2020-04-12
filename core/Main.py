import asyncio
import logging
import os
import sys

import pykeybasebot.types.chat1 as chat1
from pykeybasebot import Bot

from MinecraftServer import MinecraftServer

serverDefault = MinecraftServer("")


def format_response(response):
    count = response[0]
    players = response[1]

    if count == 0:
        reply = "0 players."
    elif count == 1:
        reply = "{} player:```\n{}\n```".format(str(count), "\n".join(players))
    else:
        reply = "{} players:```\n{}\n```".format(str(count), "\n".join(players))

    return reply

if "win32" in sys.platform:
    asyncio.set_event_loop_policy(
        asyncio.WindowsProactorEventLoopPolicy()
    )


async def handler(bot, event):
    if event.msg.content.type_name != chat1.MessageTypeStrings.TEXT.value:
        return
    if event.msg.content.text.body == "!players":
        lookup = serverDefault.server_lookup()
        response = format_response(lookup)
        channel = event.msg.channel
        await bot.chat.send(channel, response)



listen_options = {"filter-channels": [
 {
     "name": "nomik",
     "topic_name": "general",
     "members_type": "team",
 },
]}

bot = Bot(username="javathunderman", paperkey="", handler=handler)

asyncio.run(bot.start(listen_options))
