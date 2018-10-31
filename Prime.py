import discord

TOKEN = 'NTAyMjI2MDYzNzYyMzkxMDUw.Dqk38g.KFDtyaHwMfRNK6RRUKYfpDj9L9Y'

client = discord.Client()

@client.event
async def primeN(message):
    if message.content.startswith('!Primes'):
        msg = str(message.content)
        msg = msg.strip('!Primes ')
        msg = int(msg)
        print(msg)
        if (msg==1):
            await client.send_message(message.channel, "This is not a prime number.")
            return False
        elif (msg==2):
            await client.send_message(message.channel, "This is a prime number.")
            return True
        else:
            for x in range(2,msg):
                if(msg%x == 0):
                    print("This is not a prime number.")
                    await client.send_message(message.channel, "This is not a prime number.")
                    return False 
            print("This is a prime number.") 
            await client.send_message(message.channel, "This is a prime number.")
            return True 
    
@client.event
async def on_message(message):
    print(message.content)
    await primeN(message)
    
@client.event
async def on_ready():
	print('Logged in as ' + client.user.name)

client.run(TOKEN)
