import discord

TOKEN = 'NTAyMjI2MDYzNzYyMzkxMDUw.Dqk38g.KFDtyaHwMfRNK6RRUKYfpDj9L9Y'

client = discord.Client()

@client.event
async def primeN(message):
    if message.content.startswith('!Primes'):
        Primemsg = str(message.content)#
        Primemsg = Primemsg.strip('!Primes ')#This is what the user will have to type in on discord so that it can detect whether the number is a prime or not
        Primemsg = int(Primemsg)#Changes the user's inputted message which was string to a integer
        print(Primemsg)
        if (Primemsg==1):
            await client.send_message(message.channel, "This is not a prime number.")#
            return False
        elif (Primemsg==2):
            await client.send_message(message.channel, "This is a prime number.")#this waits to check for what the user has enter on discord so that they
            return True
        else:
            for x in range(2,Primemsg):
                if(Primemsg%x == 0):#The modulus here will be used to divide the user input from any random number to check whether the number they have entered is valid or not due to it returning and remainder.
                    print("This is not a prime number.")
                    await client.send_message(message.channel, "This is not a prime number.")#
                    return False 
            print("This is a prime number.") 
            await client.send_message(message.channel, "This is a prime number.")#This message gets outputted by the computer science bot on discord
            return True 
    
@client.event
async def on_message(message):
    print(message.content)
    await primeN(message)
#This part of the code is not mine...    
@client.event
async def on_ready():
	print('Logged in as ' + client.user.name)
#This part of the code is not mine....
client.run(TOKEN)
