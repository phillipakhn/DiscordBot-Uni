import discord

TOKEN = 'NTAyMjI2MDYzNzYyMzkxMDUw.Dqk38g.KFDtyaHwMfRNK6RRUKYfpDj9L9Y'

client = discord.Client()

@client.event
def primeN(message):
    if message.content.startswith('!Primes'):#This is what the user will have to type in on discord so that it can start program
        Primemsg = str(message.content)
        Primemsg = Primemsg.strip('!Primes ')
        Primemsg = int(Primemsg)#Changes the user's inputted message which was string to a integer
        print(Primemsg)
        if (Primemsg==1):
            await client.send_message(message.channel, "This is not a prime number.")# if the user has inputted 1 this will be outputted to them on Discord.
            return False
        elif (Primemsg==2):
            await client.send_message(message.channel, "This is a prime number.")#if the user has inputted 2 this message will be outputted to them on Discord.
            return True
        else:
            for x in range(2,Primemsg):#This just a search range which the program goes through when detecting and filtering through prime numbers value for the 
                if(Primemsg%x == 0):#The modulus operator is used just to show that the number the user has inputted using Discord is not divisble by x.
                    print("This is not a prime number.")
                    await client.send_message(message.channel, "This is not a prime number.")#This message gets outputted to the user on Discord only if the number they have inputted can only be divide by itself or 1.
                    return False 
            print("This is a prime number.") 
            await client.send_message(message.channel, "This is a prime number.")#This message gets outputted to the user on Discord if the number they have inputted is divisible with some other number different than 1 and itself 
            return True 
        
@client.event
async def on_message(message):
    print(message.content)
    await primeN(message)
    
@client.event
async def on_ready():
	print('Logged in as ' + client.user.name)

client.run(TOKEN)
#This part of the code is not mine and will be referenced in the documentation.