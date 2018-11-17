import discord, logging, time, random, pickle, os, datetime
from requests import get
import alastair as a
#import Kieran as k
#import Prime as p
#import tomas as t
#import mateusz as m
#import mango as mngo
#from Kieran import GoogleEarth as e
TOKEN = 'NTAyMjI2MDYzNzYyMzkxMDUw.Dqk38g.KFDtyaHwMfRNK6RRUKYfpDj9L9Y'

#global greetings
#greetings = ["Hello", "Hi", "Yo"]
#url = ["https://github.coventry.ac.uk/hollan84/DiscordBot"]

#Update test

#print(greetings)

a.removeDuplicates()

#ignore = ["!GoogleMaps"]
#pickle.dump(ignore, open("ignore.txt",'wb') )
#pickle.dump(url, open("url.txt",'wb') )
#pickle.dump(greetings, open("greetings.txt",'wb') )

client = discord.Client()

#print("502223039912476692".get_channel())

global oldmsg
oldmsg = ""

startup = datetime.datetime.now()

@client.event
async def modules(message):
	global oldmsg
	if message.author == client.user:
		return
#	if not lstmsg:
#		lstmsg = ""
	#a.dab(message)
	a.pyStart(message)
	msg = ""
	#msg = msg + str(a.pyStart(message))
	msg = msg + str(a.human(message))
	msg = msg + str(a.ignore(message))
	if "RETUR" in msg:
		return
	msg = msg + str(a.greetings(message))
	msg = msg + str(a.url(message))
	msg = msg + str(a.test(message))
	msg = msg + str(a.update(message))
	msg = msg + str(a.exitBot(message))
	msg = msg + str(a.code(message))
	msg = msg + str(a.gitHelp(message))
	msg = msg + str(a.temperature(message))
	msg = msg + str(a.fQuestion(message.content))
	msg = msg + str(a.fResponse(message.content))
	msg = msg + str(a.add(oldmsg, message))
	msg = msg + str(a.remove(message))
	msg = msg + str(a.display(message))
	msg = msg + str(a.displayCommands(message))
	msg = msg.replace('None', '')
	a.removeDuplicates()
	a.webcam(message)
	#print("MESSAGE" + msg)
	if not msg:
		msg = str(a.notInMem(message))
	if message.content.startswith('!BotInfo'):
		extip = get('https://api.ipify.org').text
		Uptime = datetime.datetime.now() - startup
		msg = extip + " - Uptime: " + str(Uptime.days)+ " day(s), " + str(Uptime.seconds//3600) + " hour(s), "+ str(int((Uptime.seconds//60)%60)) + " minute(s) and " + str(int(Uptime.seconds%60)) + " second(s)" 
	a.add(oldmsg, message)
	oldmsg = str(message.content)
	msg = "                 " + msg + "                 "
	if message.content == "!TempCode":
		await client.send_file(message.channel, "sourcecode.html")
		return
	if message.content.startswith("!Webcam"):
		#msg = "This photo was taken on " + datetime.datetime.now().strftime("%Y-%m-%d at %H:%M:%S") + " at Godiva Place"
		await client.send_message(message.channel, msg)
		await client.send_file(message.channel, "webcam.jpg")
		return
	else:
		await client.send_message(message.channel, msg)
	
#@client.event
#async def kieran(message):
#	msg = ""
#	msg = msg + k.Server(message)
#	if not msg:
#		return
#	await client.send_message(message.channel, msg)
	
@client.event
async def on_message(message):
	
	global lstmsg

	print(message.content)
		
	await modules(message)
	#await kieran(message)
	#await karl(message)
	#await 







@client.event
async def on_ready():
	print('Logged in as ' + client.user.name)
	msg = "Bot Started at " + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + " on " + str(get('https://api.ipify.org').text)
	await client.send_message(client.get_channel('502223039912476694'), msg)
	#await client.change_presence(name='test', type=2)

client.run(TOKEN)
