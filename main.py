import os
import discord

intents = discord.Intents().all()
client = discord.Client(intents=intents);

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('!Hello'):
    await message.channel.send('Beep Boop!')

client.run(os.environ['TOKEN'])

