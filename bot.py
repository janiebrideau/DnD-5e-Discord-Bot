import os
import discord
from api_requests import spells

#You will need to inlude your own discord bot's token as an env variable
#You can do this under "Secrets" in replit
bot_token = os.environ['TOKEN']

#default intents, enalbing members and message_content
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

client = discord.Client(intents = intents)

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
	#If the ! is followed by a known spell, it will return values
	if message.content.startswith('!'):
		spell_name = message.content[1:]
		spell_name = spell_name.strip().lower().replace(" ", "-")
		spell_info = spells(spell_name)
		await message.channel.send(spell_info)

client.run(bot_token)


