import discord, logging, time, random, pickle, os, datetime
from requests import get
import alastair as a #Import custom library

TOKEN = #TOKEN HERE

a.removeDuplicates() #Remove duplicates from the stored lists

client = discord.Client() #Assign the client

global oldmsg 
oldmsg = ""

startup = datetime.datetime.now()

@client.event
async def modules(message):
	global oldmsg
	if message.author == client.user: #Make sure that the bot doesn't reply to itself
		return
	a.pyStart(message)
	msg = "" #Assign empty message
	#msg = msg + str(a.pyStart(message))
	msg = msg + str(a.human(message))
	msg = msg + str(a.ignore(message))
	if "RETUR" in msg: #Stops the function if the message is 'RETUR' as these are not supposed to be run
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
	a.removeDuplicates() #Remove any duplicates in the stored lists
	msg = msg + str(a.webcam(message))
	#print("MESSAGE" + msg)
	msg = msg.replace('None', '')
	if message.content.startswith("!Webcam"):
		msgcont = message.content
		if "displayall" in msgcont: #Displays all the saved images 
			from os import listdir
			allImages = os.listdir("Photos") #Makes a list of all the file names
			await client.send_message(message.channel, "Here are all saved images:")
			for i in allImages: #Goes through all images from the webcam and sends them to the channel
				dir = "Photos/" + i 
				await client.send_file(message.channel, dir) #Sends the file to the channel
			return
		else:
			await client.send_message(message.channel, msg) #Displays the old message
			await client.send_file(message.channel, "webcam.jpg") #Displays the previous photo
			return
	if not msg:
		msg = str(a.notInMem(message)) #If there isn't any content in the msg 
	if message.content.startswith('!BotInfo'): #Give the uptime of the bot
		extip = get('https://api.ipify.org').text
		Uptime = datetime.datetime.now() - startup
		msg = extip + " - Uptime: " + str(Uptime.days)+ " day(s), " + str(Uptime.seconds//3600) + " hour(s), "+ str(int((Uptime.seconds//60)%60)) + " minute(s) and " + str(int(Uptime.seconds%60)) + " second(s)" 
	a.add(oldmsg, message)
	oldmsg = str(message.content)
	msg = msg.replace('None', '')
	msg = "                 " + msg + "                 "
	if message.content == "!TempCode": 
		await client.send_file(message.channel, "sourcecode.html") #Sens the file sourcecode.html
		return
	else:
		await client.send_message(message.channel, msg)
		if message.content.startswith("!TempF"):
			await client.send_file(message.channel, "celcius.png") #Displays a map of the world of who uses celcius vs farenheit
	
@client.event
async def on_message(message):
	global lstmsg
	print(message.content)	
	await modules(message) 

@client.event
async def on_ready():
	print('Logged in as ' + client.user.name)
	msg = "Bot Started at " + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + " on " + str(get('https://api.ipify.org').text) #Displays the IP that the bot is running on
	await client.send_message(client.get_channel('502223039912476694'), msg)

client.run(TOKEN)
