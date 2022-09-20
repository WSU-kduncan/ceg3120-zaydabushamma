

import os

import discord
import random
from dotenv import load_dotenv

load_dotenv()
#print(os.getenv('DISCORD_TOKEN'))
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

   

    Motivation_quotes = [
        'The road to success and the road to failure are almost exactly the same.',
        'Success is peace of mind, which is a direct result of self-satisfaction in knowing you made the effort to become the best of which you are capable.',
        'I never dreamed about success. I worked for it.',
        'You learn more from failure than from success. Don’t let it stop you. Failure builds character.',
    ]

    if message.content == 'quotes!':
        response = random.choice(Motivation_quotes)
        await message.channel.send(response)

client.run(TOKEN)
