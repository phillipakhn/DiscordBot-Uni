import discord, logging, time, random, pickle

TOKEN = 'NTAyMjI2MDYzNzYyMzkxMDUw.Dqk38g.KFDtyaHwMfRNK6RRUKYfpDj9L9Y'

global greetings
greetings = ["Hello", "Hi", "Yo"]
url = ["https://github.coventry.ac.uk/hollan84/DiscordBot"]

#print(greetings)

#pickle.dump(url, open("url.txt",'wb') )
#pickle.dump(greetings, open("greetings.txt",'wb') )

client = discord.Client()

#print("502223039912476692".get_channel())

#def Code():
	












@client.event
async def on_message(message):
	
	global lstmsg
	
	with open("greetings.txt",'rb') as rfp:
		greetings = pickle.load(rfp)
	with open("url.txt",'rb') as rfp:
		url = pickle.load(rfp)
		
	print(message.content)
	
	if message.author == client.user:
		return 
		
	for i in greetings:	
		if i in message.content:
			msg = greetings[random.randint(0, len(greetings)-1)] + ' {0.author.mention}'.format(message)
			await client.send_message(message.channel, msg)	
			return
	if message.content.startswith('!URL'):
		i = 0
		while i <= (len(url)-1):	
			msg = url[i]
			await client.send_message(message.channel, msg)	
			i = i + 1
		return
			
	if message.content.startswith('!Code'):
		C = open("/home/alastair/Documents/Discord_Bot.py", "r")
		msg = ('{0.author.mention}'.format(message) + " - Here is the code: \n" + C.read())
		await client.send_message(message.channel, msg)
		C.close()

	if message.content.startswith('!dab4eva'):
		while True:
			msg = 'Dab'
			await client.send_message(message.channel, msg)
	if message.content.startswith('!addurl'):
		#global lstmsg
		url.append(lstmsg)
		print(url)
		pickle.dump(url, open("url.txt",'wb'))
		return
	if message.content.startswith('!greeting'):
		greetings.append(lstmsg)
		print(greetings)
		pickle.dump(greetings, open("greetings.txt",'wb') )
		return
	else:
		lstmsg = message.content
		msg = "I can't find that within my memory, type a category."
		await client.send_message(message.channel, msg)
		msg = "Categories:"
		await client.send_message(message.channel, msg)
		msg = "!greeting, !addurl"
		await client.send_message(message.channel, msg)	

@client.event
async def on_ready():
	print('Logged in as ' + client.user.name)

client.run(TOKEN)
