import os
import discord
import requests
import json
from api_requests import *

intents = discord.Intents().all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
	print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
	#When user types "!", the bot types the API response in the chat
  if message.content.startswith('!'):
    desc = spells()
    await message.channel.send(desc)

client.run(os.environ['TOKEN'])



#todo: dynamic spell look up by the user
#todo: add more look ups: feats, traits, skills, monsters

