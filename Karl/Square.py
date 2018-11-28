import discord
import math 

TOKEN = 'NTAyMjI2MDYzNzYyMzkxMDUw.Dqk38g.KFDtyaHwMfRNK6RRUKYfpDj9L9Y'

client = discord.Client()

@client.event
async def Square(message):
    if message.content.startswith('!Square'):#This is what the user has to enter to so that this can run. 
        Squaremsg = str(message.content)
        Squaremsg = Squaremsg.strip('!Square ')
        Squaremsg = int(Squaremsg)#Here I have changed the user input to an integer instead of a string so that it can be used for the calculation.
        print(Squaremsg)
        SquaredNum = int(message) * int(message)#This just multiples the number by itself to get the squared value of it.
        SquareNumAns = "The square number for the number" + str(message) + "and the square value of the number is" + str(SquaredNum)#This message will be outputted to the user once they have ran the code
        await client.send_message(message.channel,(SquareNumAns))#This gets the variable from above so that the message can be seen through Discord for the users.
        
@client.event
async def on_message(message):
    print(message.content)
    await Square(message)

@client.event
async def on_ready():
	print('Logged in as ' + client.user.name)

client.run(TOKEN)
 