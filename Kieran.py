import discord
import GoogleMaps as e

TOKEN = 'NTAyMjI2MDYzNzYyMzkxMDUw.Dqk38g.KFDtyaHwMfRNK6RRUKYfpDj9L9Y' # to link bot to discord server


client = discord.Client()

@client.event
async def kieran(message):
	if message.author == client.user: #makes sure the bot doesn't reply to itself
		return
	msg = ""
	if message.content.startswith('!GoogleMaps'):
		msg = msg + str(e.Google(message))
	if not msg:
		return
	msg = msg.strip('None')
	await client.send_message(message.channel, msg) # send message to discord
	

@client.event
async def on_message(message):

	print(message.content)
		
	await kieran(message)


@client.event
async def on_ready():
	print('Logged in as ' + client.user.name)

client.run(TOKEN)

####
