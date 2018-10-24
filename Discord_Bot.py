import discord, logging, time, random, pickle, os
import alastair as a
TOKEN = 'NTAyMjI2MDYzNzYyMzkxMDUw.Dqk38g.KFDtyaHwMfRNK6RRUKYfpDj9L9Y'

global greetings
greetings = ["Hello", "Hi", "Yo"]
url = ["https://github.coventry.ac.uk/hollan84/DiscordBot"]

#print(greetings)

#pickle.dump(url, open("url.txt",'wb') )
#pickle.dump(greetings, open("greetings.txt",'wb') )

client = discord.Client()

#print("502223039912476692".get_channel())

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

    #a.greetings(message)
    	
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
		C = open("/home/pi/DiscordBot/Discord_Bot.py", "r")
		msg = ('{0.author.mention}'.format(message) + " - Here is the code: \n" + C.read())
		await client.send_message(message.channel, msg)
		C.close()
		
	if message.content.startswith('!Exit'):
		exit()
		
	if message.content.startswith('!Update'):
		os.system('cd ~ \n ./update.sh')
		await client.send_message(message.channel, "Git Updated")
		exit()

	if message.content.startswith('!dab4eva'):
		while True:
			msg = 'Dab'
			await client.send_message(message.channel, msg)
	if message.content.startswith('!help'):
		msg = '---CLONE GIT---'
		await client.send_message(message.channel, msg)
		msg = '1) git clone https://github.coventry.ac.uk/hollan84/DiscordBot'
		await client.send_message(message.channel, msg)
		msg = '2) (Put in Username and Password) \n'
		await client.send_message(message.channel, msg)
		msg = '---PUSH GIT---'
		await client.send_message(message.channel, msg)
		msg = '1) cd DiscordBot'
		await client.send_message(message.channel, msg)	
		msg = '2) git init'
		await client.send_message(message.channel, msg)	
		msg = '3) git add .'
		await client.send_message(message.channel, msg)
		msg = "4) git commit -m 'Discord'"
		await client.send_message(message.channel, msg)	
		msg = '5) git remote add origin https://github.coventry.ac.uk/hollan84/DiscordBot'
		await client.send_message(message.channel, msg)		
		msg = '6) git push -u origin master'
		await client.send_message(message.channel, msg)
		msg = '7) (Put in Username and Password)'
		await client.send_message(message.channel, msg)
		msg = '---PULL GIT---'
		await client.send_message(message.channel, msg)
		msg = '1) git pull'
		await client.send_message(message.channel, msg)
		msg = '2) (Put in Username and Password) \n'
		await client.send_message(message.channel, msg)
		return
	
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
