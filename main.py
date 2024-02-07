import discord
import os

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

#
# @client.event
# async def on_ready():
#     print(f"Logged in as {client.user}")
#
#
# @client.event
# async def on_message(message):
#     index = ":"
#     commands = ["say", "wipe"]
#     if message.author == client.user:
#         return
#     if message.content.startswith(f"{index}help"):
#         print(commands)
#
#
# client.run(os.getenv('TOKEN'))
print(os.getenv("TOKEN"))
