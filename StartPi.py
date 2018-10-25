import discord, logging, time, random, pickle, os
TOKEN = 'NTAyMjI2MDYzNzYyMzkxMDUw.Dqk38g.KFDtyaHwMfRNK6RRUKYfpDj9L9Y'

client = discord.Client()

@client.event
async def on_message(message):
	if message.author == client.user:
		return 	
	if message.content.startswith('!Start'):
		os.system('python3 Discord_Bot.py')
		return
@client.event
async def on_ready():
	print('Logged in as ' + client.user.name)

client.run(TOKEN)
