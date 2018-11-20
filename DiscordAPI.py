import discord
import Location as maps

TOKEN = 'NTAyMjI2MDYzNzYyMzkxMDUw.Dqk38g.KFDtyaHwMfRNK6RRUKYfpDj9L9Y' # The Discord Bot's token

client = discord.Client()

'''Input:Object (message), Output:String (msg)'''
@client.event
async def Server(message):
	if message.author == client.user: # To prevent the bot from replying to itself
		return
	msg = ""
	if message.content.startswith('!GoogleMaps'):
		run = 0
		msg = msg + str(maps.Google(message,run)) # Calls function "Google" from GoogleMaps.py
		await client.send_message(message.channel, msg)
	elif message.content.startswith('!Timezone'):
		run = 1
		msg = msg + str(maps.Google(message,run))
		await client.send_message(message.channel, msg)
	elif message.content.startswith('!Weather'):
		run = 2
		content = maps.Google(message,run)
		Advice = str(content[2]) +"\n" + str(content[3])	
		embed = discord.Embed()
		embed.set_image(url=content[1])
		while True:
			try:
				await client.send_message(message.channel,content[0],embed=embed)
				await client.send_message(message.channel,Advice)
				break		
			except:
				msg = "That location doesn't exist or it is not specific enough!"
				await client.send_message(message.channel,msg)
				break
	elif not msg: # To prevent an empty message being sent
		return
	
'''Input: Object (message), Output:Object (message)'''
@client.event
async def on_message(message): # Must be called "on_message"
	print(message.content)
	await Server(message) # "await" to allow print("message.content") to be executed

'''Prints to console'''
@client.event
async def on_ready(): # Must be called "on_ready" 
	print('Logged in as ' + client.user.name)

client.run(TOKEN) # To run the Discord Bot


