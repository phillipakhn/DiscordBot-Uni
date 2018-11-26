import discord, time, random, pickle, os, sys, requests

TOKEN = 'NTAyMjI2MDYzNzYyMzkxMDUw.Dqk38g.KFDtyaHwMfRNK6RRUKYfpDj9L9Y'
client = discord.Client()

'''Allows people to send messages to the channel without the bot replying to them'''
def human(message):
	if message.content.startswith('!Human'): 
		return "RETUR" #This is recognised by Discord_Bot.py and returns
	return
		
'''Allows people to use their own commands without this bot replying to them'''
def ignore(message):
	with open("ignore.txt",'rb') as rfp: #Opens ignore.txt as a list
		ignore = pickle.load(rfp)
	for i in ignore: #Check to see if that command is in the ignore list
		if message.content.startswith(i):
			return "RETUR"
	return
		
'''Checks to see if the message recieved is a greeting and then replies back with a random greeting back'''
def greetings(message):
	with open("greetings.txt",'rb') as rfp: #Open greetings.txt as a list
		greetings = pickle.load(rfp)
	for i in greetings:	
		if message.content.startswith(i): #Check to see if the message is within the list
			msg = greetings[random.randint(0, len(greetings)-1)] + ' {0.author.mention}'.format(message)  #Sets the message with username
			if 100 > random.randint(0, 100): #Sets the chance of the bot to ask a follow up question, currently set to 100%
				msg = msg + "\n" + askQuestion() #Adds askQuestion() string to msg
			return msg
	return
			
#def fQuestion(message):
#	with open("fQuestion.txt",'rb') as rfp:
#		fQuestion = pickle.load(rfp)
#	for i in fQuestion:	
#		if i in message.content:
#			msg = 'How are you {0.author.mention}?'.format(message)
#			return msg

'''Responds to a question with a random response stored in memory'''
def fResponse(message):
	response = str(message) #Sets the message as a string
	with open("fResponse.txt",'rb') as rfp: #Open the friendly responses as a list
		fresponse = pickle.load(rfp)
	for i in fresponse: 
		if response in i: #If the response matches an entry in the list
			msg = fresponse[random.randint(0, len(fresponse)-1)] #Set a random response
			return msg
	return
		
'''Asks a random question to the user'''
def fQuestion(message):
	question = str(message)
	with open("fQuestion.txt",'rb') as rfp:  #Open the friendly questions as a list
		fquestion = pickle.load(rfp)
	with open("fResponse.txt",'rb') as rfp: #Open the friendly responses as a list
		fresponse = pickle.load(rfp)
	for i in fquestion:
		if question in i: #If the question matches an entry in the list
			msg = fresponse[random.randint(0, len(fresponse)-1)] #Sends a random response from friendly response
			return msg
	return
		
'''Asks a random question from the user with prompt from the greetings function'''
def askQuestion():
	with open("fQuestion.txt",'rb') as rfp: #Open the friendly questions as a list
		fquestion = pickle.load(rfp)
	msg = fquestion[random.randint(0, len(fquestion)-1)] #Asks a random question
	return msg
		
'''Checks to see if the user is asking for the URL's and then displays all the stored URLs'''
def url(message):
	if message.content.startswith('!URL'):
		i = 0
		with open("url.txt",'rb') as rfp:
			url = pickle.load(rfp)
		msg = ""
		while i <= (len(url)-1):	
			msg = msg + "\n" + url[i]
			i = i + 1
		return msg
	return
	
'''Tests to see if the bot is running'''			
def test(message):
	if message.content.startswith('!Test'):
		msg = 'This is proof that it is working'
		return msg
	return
		
'''Starts a shell script stored on the Raspberry Pi that is running the bot'''
def update(message):
	if message.content.startswith('!Update'):
		os.system('cd ~ \n ./update.sh')
		exit()
	return
		
'''Starts another program in the DiscordBot folder'''
def pyStart(message):
	if message.content.startswith('!PyStart'):
		t = str(message.content) 
		t = t.replace("!PyStart ", "")
		#m = "python3 " + t
		#os.system(m)
		sys.argv = [t, 'arg']  # argv[0] should still be the script name
		exec(compile(open(t, "rb").read(), t, 'exec'))
		return "Started Program"
	return
		
'''Stops the bot'''
def exitBot(message):
	if message.content.startswith('!Exit'):
		exit()
		
'''Adds the previous memory into storage'''
def add(lstmsg, message):
	if message.content.startswith('!addurl'):
		with open("url.txt",'rb') as rfp:
			url = pickle.load(rfp)
		url.append(lstmsg)
		print(url)
		pickle.dump(url, open("url.txt",'wb'))
		return "Added URL    "
	if message.content.startswith('!greeting'):
		with open("greetings.txt",'rb') as rfp:
			greetings = pickle.load(rfp)
		greetings.append(lstmsg)
		print(greetings)
		pickle.dump(greetings, open("greetings.txt",'wb') )
		return "Added Greeting    "
	if message.content.startswith('!friendlyQuestion'):
		with open("fQuestion.txt",'rb') as rfp:
			fQuestion = pickle.load(rfp)
		fQuestion.append(lstmsg)
		print(fQuestion)
		pickle.dump(fQuestion, open("fQuestion.txt",'wb') )
		return "Added Friendly Question     "
	if message.content.startswith('!friendlyResponse'):
		with open("fResponse.txt",'rb') as rfp:
			fresponse = pickle.load(rfp)
		fresponse.append(lstmsg)
		pickle.dump(fresponse, open("fResponse.txt",'wb') )
		return "Added Friendly Response     "
	if message.content.startswith('!ignore'):
		if lstmsg == "!ignore":
			return "Can't add !ignore"
		with open("ignore.txt",'rb') as rfp:
			ignore = pickle.load(rfp)
		ignore.append(lstmsg)
		pickle.dump(ignore, open("ignore.txt",'wb') )
		msg = "Added '" + lstmsg + "' to ignore "
		return msg
	return
	
'''Remove an entry in the memory'''
def remove(message):
	if message.content.startswith('!Remove'):
		msg = str(message.content)
		msg = msg.replace("!Remove ", "")
		if msg.lower() == "help":
			msg = "Syntax: !Remove [value_to_remove] from [list_to_remove_from] \n"
			msg = msg + "Lists: greeting, ignore, url, fResponse, fQuestion"
			return msg
		wordList = msg.split(" from ")
		toRemove = wordList[0]
		removeFrom = wordList[1]
		print(toRemove)
		print(removeFrom)
		if removeFrom == "greeting":
			fileName = "greetings.txt"
			with open(fileName,'rb') as rfp:
				listRemove = pickle.load(rfp)
		elif removeFrom == "ignore":
			fileName = "ignore.txt"
			with open(fileName,'rb') as rfp:
				listRemove = pickle.load(rfp)
		elif removeFrom == "url":
			fileName = "url.txt"
			with open(fileName,'rb') as rfp:
				listRemove = pickle.load(rfp)
		elif removeFrom == "fResponse":
			fileName = "fResponse.txt"
			with open(fileName,'rb') as rfp:
				listRemove = pickle.load(rfp)
		elif removeFrom == "fQuestion":
			fileName = "fQuestion.txt"
			with open(fileName,'rb') as rfp:
				listRemove = pickle.load(rfp)
		else:
			msg = "Syntax: !Remove [value_to_remove] from [list_to_remove_from] \n"
			msg = msg + "Lists: greeting, ignore, url, fResponse, fQuestion"
			return msg
		if toRemove in listRemove:
			while toRemove in listRemove:
				listRemove.remove(toRemove)
			pickle.dump(listRemove, open(fileName,'wb'))
			msg = "Removed '" + toRemove + "' from " + removeFrom
			return msg
		elif toRemove not in listRemove:
			msg = "'" + toRemove + " is not in " + removeFrom
			return msg
		
'''Display all entries stored in memory'''
def display(message):
	if message.content.startswith('!Display'):
		fileNames = ("greetings.txt", "ignore.txt", "url.txt", "fResponse.txt", "fQuestion.txt")
		msg = ""
		for files in fileNames:
			with open(files,'rb') as rfp:
				listDisplay = pickle.load(rfp)
			msg = msg + files.replace(".txt", " - ")
			msg = msg + str(listDisplay)
			msg = msg + "\n"
		return msg
		
'''Display commands stored in memory and can add and remove'''
def displayCommands(message):
	if message.content.startswith('!displayCommands'):
		commands = open("commands.txt", "r")
		msg = commands.read()
		commands.close()
		return msg
	if message.content.startswith('!addCommand'):
		commandToAdd = str(message.content)
		commandToAdd = commandToAdd.replace("!addCommand ", "")
		commands = open("commands.txt", "a")
		commandToAdd = "\n" + commandToAdd
		commands.write(commandToAdd)
		commands.close()
		commandToAdd = commandToAdd.replace("\n", "")
		msg = "'" + commandToAdd + "' was added to commands"
		return msg
	if message.content.startswith('!removeCommand'):
		commandToRemove = str(message.content)
		commandToRemove = commandToRemove.replace("!removeCommand ", "")
		commands = open("commands.txt", "r")
		commandFile = commands.read()
		if commandToRemove in commandFile:
			#commandToRemove = commandToRemove + "\n"
			commandFile.replace(commandToRemove, "")
			commands.close()
			commands = open("commands.txt", "w")
			commands.write(commandFile)
			commands.close()
			if commandToRemove not in commandFile:
				msg = "Removed '" + commandToRemove + "' from the commands"
				return msg
			else:
				msg = "Unable to remove '" + commandToRemove + "' from the commands"
				return msg
		else:
			msg = commandFile + " is not in commands"
			return msg
		
'''Opens all memory files and looks for duplicates in the lists'''
def removeDuplicates():
	fileNames = ("greetings.txt", "ignore.txt", "url.txt", "fResponse.txt", "fQuestion.txt")
	msg = ""
	for files in fileNames:
		with open(files,'rb') as rfp:
			listDisplay = pickle.load(rfp)
		listDisplay = list(set(listDisplay))
		pickle.dump(listDisplay, open(files,'wb'))
		
'''Gets the temperature from a seperate Raspberry Pi on the local network'''
def temperature(message):
	from lxml import html
	import requests
	if message.content.startswith('!TempInfo'):
		page = requests.get('http://100.90.93.150/about')
		tree = html.fromstring(page.content)
		t = (tree.xpath('//p/text()'))
		t = str(t)
		t = t.replace("[' ', ' ', ' ", "")
		t = t.replace(" ']", "")
		return t
	if message.content.startswith('!TempCode'):
		import urllib
		from urllib.request import urlopen
		url = 'http://100.90.93.150/source'
		with urllib.request.urlopen(url) as url:
			webContent = str(url.read())
			webContent = webContent.strip("b'")
			webContent = webContent[:-1]
			webContent = webContent.replace("<br>", "")
			webContent = webContent.replace("\\n", " <br> ")
			webContent = webContent.replace("\\t", "")
		f = open('sourcecode.html', 'w')
		f.write(webContent)
		f.close()
		return
	if message.content.startswith('!Temp'):
		page = requests.get('http://100.90.93.150')
		tree = html.fromstring(page.content)
		t = (tree.xpath('//h1/text()'))
		t = str(t)
		if "°C" in t:
			t = t.strip("[' ', '")
			t = t.replace("Â", "")
			t = t.strip("', ' ']")
			if message.content.startswith('!TempF'):
				import re
				c = t
				t = re.findall(r'\b\d+\b', t)
				t = float(t[0])
				t = (t*(9/5)) + 32
				t = str(t) + "°F (" + c + ")"
			t = "The Current Temperature at Godiva Place is " + t
			t = t + " \nIf you want to see a live image of the weather use !Webcam Godiva"
		else:
			t = "There is currently an error with the weather station. Please try again later"
		return t
	return

'''Gets a webcam image and stores it to memory'''
def webcam(message):
	if message.content.startswith('!Webcam'):
		import datetime
		msg = message.content
		if "godiva" in msg.lower():
			try:
    				r = requests.get("http://100.90.113.111:8080/photoaf.jpg", timeout=10.0)
			except requests.Timeout as err:
				return "This webcam appears to be down"
			import urllib.request
			urllib.request.urlretrieve("http://100.90.113.111:8080/photoaf.jpg", "webcam.jpg")
			msg = "This photo was taken on " + datetime.datetime.now().strftime("%Y-%m-%d at %H:%M:%S") + " at Godiva Place"
			f = open("OldWebcam.txt", "w")
			f.write(msg)
			f.close()
			return msg
		if "ullswater" in msg.lower():
			import urllib.request
			urllib.request.urlretrieve("https://www.ullswater-steamers.co.uk/images/webcam/ispy.jpg", "webcam.jpg")
			msg = "This photo was taken on " + datetime.datetime.now().strftime("%Y-%m-%d at %H:%M:%S") + " at Ullswater"
			f = open("OldWebcam.txt", "w")
			f.write(msg)
			f.close()
			return msg
		if "warwick" in msg.lower():
			import urllib.request
			urllib.request.urlretrieve("https://images.webcams.travel/preview/1349463611.jpg", "webcam.jpg")
			msg = "This photo was taken on " + datetime.datetime.now().strftime("%Y-%m-%d at %H:%M:%S") + " in Warwick"
			f = open("OldWebcam.txt", "w")
			f.write(msg)
			f.close()
			return msg
		if "california" in msg.lower():
			import urllib.request
			urllib.request.urlretrieve("http://mk-webcam.net/MKB/mk-camB.jpg", "webcam.jpg")
			msg = "This photo was taken on " + datetime.datetime.now().strftime("%Y-%m-%d at %H:%M:%S") + " in Sequoia national park"
			f = open("OldWebcam.txt", "w")
			f.write(msg)
			f.close()
			return msg
		if "save" in msg.lower():
			import sys
			time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
			comm = "cp webcam.jpg Photos/" + time + ".jpg"
			os.system(comm)
			return "The following image has been saved to " + time + ".jpg"
		f = open("OldWebcam.txt", "r")
		msg = "Please specify a location; you will now be shown the last photo taken on this bot \n" + f.read()
		f.close()
		return msg

'''Displays the code for Discord_Bot.py'''
def code(message):
	if message.content.startswith('!Code'):
		C = open("/home/pi/DiscordBot/Discord_Bot.py", "r")
		msg = ('{0.author.mention}'.format(message) + " - Here is the code: \n" + C.read())
		C.close()
		return msg
	return
		
#def dab(message):
#	if message.content.startswith('!dab4eva'):
#		while True:
#			msg = 'Dab'
#			await client.send_message(message.channel, msg)

'''Displays an error code if the message is not recognised'''
def notInMem(message):
	lstmsg = message.content
	msg = "I can't find that within my memory, type a category. \n Categories: \n !greeting, !addurl, !friendlyResponse, !friendlyQuestion or !ignore"
	return msg
	
'''Displays all help due for the github'''
def gitHelp(message):
	if message.content.startswith('!help'):
		msg = '---CLONE GIT--- \n'
		msg = msg + '1) git clone https://github.coventry.ac.uk/hollan84/DiscordBot \n'
		msg = msg + '2) (Put in Username and Password) \n'
		msg = msg + '---PUSH GIT--- \n'
		msg = msg + '1) cd DiscordBot \n'
		msg = msg + '2) git init \n'
		msg = msg + '3) git add . \n'
		msg = msg + "4) git commit -m 'Discord' \n"
		msg = msg + '5) git remote add origin https://github.coventry.ac.uk/hollan84/DiscordBot \n'	
		msg = msg + '6) git push -u origin master \n'
		msg = msg + '7) (Put in Username and Password) \n'
		msg = msg + '---PULL GIT--- \n'
		msg = msg + '1) git pull \n'
		msg = msg + '2) (Put in Username and Password) \n'
		return msg
	return
	
'''Prints the message content'''
def testInput(message):
	print(message.content)
	
