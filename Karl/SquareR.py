import discord
import math
TOKEN = 'NTAyMjI2MDYzNzYyMzkxMDUw.Dqk38g.KFDtyaHwMfRNK6RRUKYfpDj9L9Y'

client = discord.Client()

@client.event
async def sRoot(message):
    if message.content.startswith('!SquareRoot'):#This is the message that the user will have to input on Discord for the program to start
        sRootmsg = str(message.content)
        sRootmsg = sRootmsg.strip('!SquareRoot ')
        sRootmsg = int(sRootmsg)# This changes the value of the variable so that it can get the square root of value
        print(sRootmsg)
        ans = math.sqrt(sRootmsg)#This is the square root function which I am using from the math library so that it can be used for the calulation.
        lineAnswer = "The square root for the number" + str(sRootmsg) + "is" + (ans)#This is the message that shows the user the answer for the value they have entered using the function
        await client.send_message(message.channel,(lineAnswer))#This line allows the message to be seen to the user when accessing discord.
                                  
@client.event
async def on_message(message):
    print(message.content)
    await sRoot(message)
    
@client.event
async def on_ready():
	print('Logged in as ' + client.user.name)

client.run(TOKEN)