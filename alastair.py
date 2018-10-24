import discord, logging, time, random, pickle

TOKEN = 'NTAyMjI2MDYzNzYyMzkxMDUw.Dqk38g.KFDtyaHwMfRNK6RRUKYfpDj9L9Y'
client = discord.Client()

async def greetings(message, greetings):
	for i in greetings:	
		if i in message.content:
			msg = greetings[random.randint(0, len(greetings)-1)] + ' {0.author.mention}'.format(message)
			client.send_message(message.channel, msg)
			return
