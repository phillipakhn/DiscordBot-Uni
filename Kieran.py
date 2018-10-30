import discord, logging, time, random, pickle, os
TOKEN = 'NTAyMjI2MDYzNzYyMzkxMDUw.Dqk38g.KFDtyaHwMfRNK6RRUKYfpDj9L9Y'


client = discord.Client()

@client.event
async def kieran(message):
	if message.author == client.user:
		return
	msg = ""
	msg = msg + str(e.Google(message))
	await client.send_message(message.channel, msg) # send message to discord
	

@client.event
async def on_message(message):
	
	global lstmsg

	print(message.content)
		
	await kieran(message)


@client.event
async def on_ready():
	print('Logged in as ' + client.user.name)

client.run(TOKEN)

####
