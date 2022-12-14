import os
import discord
from api_requests import spells

#You will need to inlude your own discord bot's token as an env variable
#You can do this under "Secrets" in replit
bot_token = os.environ['TOKEN']

#All intents enabled for now
client = discord.Client(intents=discord.Intents().all())


#When the bot first starts, it displays in the console that you are logged in as (bot user)
@client.event
async def on_ready():
	print('We have logged in as {0.user}'.format(client))

#This is to avoid the bot answering to itself
@client.event
async def on_message(message):
	if message.author == client.user:
		return

	#When user types "!", the bot types the API response in the chat
	if message.content.startswith('!'):
		spell_name = " Acid Arrow "
		spell_name = spell_name.strip().lower().replace(" ", "-")
		spell_info = spells(spell_name)
		await message.channel.send(spell_info)
	#TO DO: read the user's input and give the spell info accordingly.


client.run(bot_token)

#todo: dynamic spell look up by the user
#todo: add more look ups: feats, traits, skills, monsters
#todo: Bot sends message to current server members or new members in a PM (only once!) explaining what it does and which commands it responds to.
