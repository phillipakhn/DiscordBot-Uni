import discord, logging, time, random, pickle, os, datetime
import alastair as a
#import karl as k
#import tomas as t
#import mateusz as m
#import mango as mngo
#from Kieran import GoogleEarth as e
TOKEN = 'NTAyMjI2MDYzNzYyMzkxMDUw.Dqk38g.KFDtyaHwMfRNK6RRUKYfpDj9L9Y'

global greetings
greetings = ["Hello", "Hi", "Yo"]
url = ["https://github.coventry.ac.uk/hollan84/DiscordBot"]

#Update test

#print(greetings)

#pickle.dump(url, open("url.txt",'wb') )
#pickle.dump(greetings, open("greetings.txt",'wb') )

client = discord.Client()

#print("502223039912476692".get_channel())

startup = datetime.datetime.now()

@client.event
async def alastair(message):
	if message.author == client.user:
		return
#	if not lstmsg:
#		lstmsg = ""
	#a.dab(message)
	msg = ""
	msg = msg + str(a.human(message))
	msg = msg + str(a.greetings(message))
	msg = msg + str(a.url(message))
	msg = msg + str(a.test(message))
	msg = msg + str(a.update(message))
	msg = msg + str(a.exitBot(message))
	msg = msg + str(a.code(message))
	msg = msg + str(a.gitHelp(message))
	msg = msg + str(a.temperature(message))
	msg = msg.strip('None')
	#print("MESSAGE" + msg)
	if message.content.startswith('!BotInfo'):
		uptime = datetime.datetime.now() - startup
		msg = "Uptime: " + str(Uptime.days)+ " day(s), " + str(Uptime.seconds//3600) + " hour(s), "+ str(int((Uptime.seconds//60)%60)) + " minute(s) and " + str(int(Uptime.seconds%60)) + " second(s)" 
	#if not msg:
	await client.send_message(message.channel, msg)
	

@client.event
async def on_message(message):
	
	global lstmsg

	print(message.content)
		
	await alastair(message)
	#await kieran
	#await 







@client.event
async def on_ready():
	print('Logged in as ' + client.user.name)

client.run(TOKEN)
