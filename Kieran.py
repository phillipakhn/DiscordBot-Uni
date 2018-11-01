import discord
import GoogleMaps as e

TOKEN = 'NTAyMjI2MDYzNzYyMzkxMDUw.Dqk38g.KFDtyaHwMfRNK6RRUKYfpDj9L9Y' # The Discord Bot's token

client = discord.Client()

'''Input:Object (message), Output:String (msg)'''
@client.event
async def Server(message):
	if message.author == client.user: # To prevent the bot from replying to itself
		return
	msg = ""
	if message.content.startswith('!GoogleMaps'):
		msg = msg + str(e.Google(message)) # Calls function "Google" from GoogleMaps.py
	if not msg: # To prevent an empty message being sent
		return
	await client.send_message(message.channel, msg) # Send "msg" to discord
	
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


