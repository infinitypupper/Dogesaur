import os
import random

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

# Auto-responses to text in chat.
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == '>help':
        response = "There is no help list available yet. For help, contact the bot owner: puptaco#3335!"
        await message.channel.send(response)
    elif message.content == '>doge':
        response = "Bork!"
        await message.channel.send(response)
    elif message.content == '>about':
        response = "This is a bot created by puptaco#3335. Send them a DM if you like!\nCurrently this bot doesn't do much at the moment."
        await message.channel.send(response)

client.run(TOKEN)
