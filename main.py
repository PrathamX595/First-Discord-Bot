import discord
import os
from dotenv import load_dotenv
load_dotenv() 

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        print(client.user)

    if message.content.startswith('$hi'):
        await message.channel.send('Hello sir how are you?')

client.run(os.getenv('TOKEN'))
