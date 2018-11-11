import discord, time, random, pickle, os, sys

TOKEN = 'NTAyMjI2MDYzNzYyMzkxMDUw.Dqk38g.KFDtyaHwMfRNK6RRUKYfpDj9L9Y'
client = discord.Client()

def human(message):
	if message.content.startswith('!Human'):
		return
			
def greetings(message):
	with open("greetings.txt",'rb') as rfp:
		greetings = pickle.load(rfp)
	for i in greetings:	
		if i in message.content:
			msg = greetings[random.randint(0, len(greetings)-1)] + ' {0.author.mention}'.format(message)
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
			
def test(message):
	if message.content.startswith('!Test'):
		msg = 'This is working'
		return msg
		
def update(message):
	if message.content.startswith('!Update'):
		os.system('cd ~ \n ./update.sh')
		exit()
		
def pyStart(message):
	if message.content.startswith('!PyStart'):
		t = str(message.content) 
		t = t.replace("!PyStart ", "")
		#m = "python3 " + t
		#os.system(m)
		sys.argv = [t, 'arg']  # argv[0] should still be the script name
		exec(compile(open(t, "rb").read(), t, 'exec'))
		return "Started Program"
		
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
		return
	if message.content.startswith('!greeting'):
		with open("greetings.txt",'rb') as rfp:
			greetings = pickle.load(rfp)
		greetings.append(lstmsg)
		print(greetings)
		pickle.dump(greetings, open("greetings.txt",'wb') )
		return
	if message.content.startswith('!friendlyQuestion'):
		with open("fQuestion.txt",'rb') as rfp:
			fQuestion = pickle.load(rfp)
		fQuestion.append(lstmsg)
		print(fQuestion)
		pickle.dump(fQuestion, open("fQuestion.txt",'wb') )
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
		
def code(message):
	if message.content.startswith('!Code'):
		C = open("/home/pi/DiscordBot/Discord_Bot.py", "r")
		msg = ('{0.author.mention}'.format(message) + " - Here is the code: \n" + C.read())
		C.close()
		return msg
		
#def dab(message):
#	if message.content.startswith('!dab4eva'):
#		while True:
#			msg = 'Dab'
#			await client.send_message(message.channel, msg)
		
def notInMem(message):
	lstmsg = message.content
	msg = "I can't find that within my memory, type a category. \n Categories: \n !greeting, !addurl"
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
			
def testInput(message):
	print(message)
	
