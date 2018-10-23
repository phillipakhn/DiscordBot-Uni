import discord, logging, time, random, pickle



def greetings(message)
    for i in greetings:	
        if i in message.content:
            msg = greetings[random.randint(0, len(greetings)-1)] + ' {0.author.mention}'.format(message)
            await client.send_message(message.channel, msg)	
            return