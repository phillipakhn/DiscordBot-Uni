import discord, time, random, pickle, os, sys

TOKEN = 'NTAyMjI2MDYzNzYyMzkxMDUw.Dqk38g.KFDtyaHwMfRNK6RRUKYfpDj9L9Y'
client = discord.Client()

def human(message):
	if message.content.startswith('!Human'):
		return "RETUR"
	return
		
def ignore(message):
	with open("ignore.txt",'rb') as rfp:
		ignore = pickle.load(rfp)
	for i in ignore:	
		if message.content.startswith(i):
			return "RETUR"
	return
			
def greetings(message):
	with open("greetings.txt",'rb') as rfp:
		greetings = pickle.load(rfp)
	for i in greetings:	
		if message.content.startswith(i):
			msg = greetings[random.randint(0, len(greetings)-1)] + ' {0.author.mention}'.format(message)
			if 100 > random.randint(0, 100):
				msg = msg + "\n" + askQuestion()
			return msg
	return
			
#def fQuestion(message):
#	with open("fQuestion.txt",'rb') as rfp:
#		fQuestion = pickle.load(rfp)
#	for i in fQuestion:	
#		if i in message.content:
#			msg = 'How are you {0.author.mention}?'.format(message)
#			return msg

def fResponse(message):
	response = str(message)
	with open("fResponse.txt",'rb') as rfp:
		fresponse = pickle.load(rfp)
	for i in fresponse:
		if response in i:
			msg = fresponse[random.randint(0, len(fresponse)-1)]
			return msg
	return
		
def fQuestion(message):
	question = str(message)
	with open("fQuestion.txt",'rb') as rfp:
		fquestion = pickle.load(rfp)
	with open("fResponse.txt",'rb') as rfp:
		fresponse = pickle.load(rfp)
	for i in fquestion:
		if question in i:
			msg = fresponse[random.randint(0, len(fresponse)-1)]
			return msg
	return
			
def askQuestion():
	with open("fQuestion.txt",'rb') as rfp:
		fquestion = pickle.load(rfp)
	msg = fquestion[random.randint(0, len(fquestion)-1)]
	return msg
			
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
			
def test(message):
	if message.content.startswith('!Test'):
		msg = 'This is working'
		return msg
	return
		
def update(message):
	if message.content.startswith('!Update'):
		os.system('cd ~ \n ./update.sh')
		exit()
	return
		
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
		
def exitBot(message):
	if message.content.startswith('!Exit'):
		exit()
		
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
			webContent = url.read()
			#webContent = str(webContent.splitlines())
			webContent = webContent.replace("\n", " \n ")
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
			t = "The Current Temperature at Godiva Place is " + t
		else:
			t = "There is currently an error with the weather station. Please try again later"
		return t
	return
		
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
		
def notInMem(message):
	lstmsg = message.content
	msg = "I can't find that within my memory, type a category. \n Categories: \n !greeting, !addurl, !friendlyResponse, !friendlyQuestion or !ignore"
	return msg
	
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
			
def testInput(message):
	print(message)
	
