import discord

TOKEN = 'NTAyMjI2MDYzNzYyMzkxMDUw.Dqk38g.KFDtyaHwMfRNK6RRUKYfpDj9L9Y'

client = discord.Client()

@client.event
async def primeN(message):
    if message.content.startswith('!Primes'):
        if (message==1):
            return False
    elif (message==2):
        return True
    else:
        for x in range(2,message):
            if(message % x==0):
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