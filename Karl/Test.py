import discord

TOKEN = 'NTAyMjI2MDYzNzYyMzkxMDUw.Dqk38g.KFDtyaHwMfRNK6RRUKYfpDj9L9Y'

client = discord.Client()

import math

@client.event
async def SineCalAngle(message): 
    if message.content.startswith('!SineCalAngle'):
        Sinemsg = str(message.content)
        Sinemsg = Sinemsg.strip('!SineCalAngle ')
        Sinemsg = int(Sinemsg)
        SinemsgH = int(input("What is the length of the Hypotenuse?"))
        SinemsgO = int(input("What is the length of the opposite?"))
        SinemsgA = int(input("What is the size of the angle?"))
        print(Sinemsg)
        print(SinemsgH)
        print(SinemsgO)
        print(SinemsgA)
        if type(SinemsgH) and type(SinemsgO) and type(SinemsgA)== int:
            AngleWithS = math.sin(math.radians(SineAngle))
            Sine = SinemsgA * SinemsgO / SinemsgH 
            SineCalculation = math.degrees(math.asin(Sine))           
            print(round(SineCalculation, 2))
            return True 
            await client.send_message(message.channel, "The answer for your sine calculation to the nearest 2 Decimal places is " + str(round(SineCalculation, 2) ))
        else:
            await client.send_message(message.channel, "You have not inputted integers.")
            return False
    # function for calulating the missing angle using inverse sin working.
    
        
@client.event
async def on_message(message):
    print(message.content)
    await SineCalAngle(message)
#This part of the code is not mine...    
@client.event
async def on_ready():
	print('Logged in as ' + client.user.name)
#This part of the code is not mine....
client.run(TOKEN)