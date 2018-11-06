#Trigonometry

import math 


TOKEN = 'NTAyMjI2MDYzNzYyMzkxMDUw.Dqk38g.KFDtyaHwMfRNK6RRUKYfpDj9L9Y'

client = discord.Client()

@client.event
async def SineCalAngle(message): 
	if message.content.startswith('!SineCalAngle'):
        Sinemsg = str(message.content)#
        Sinemsg = Sinemsg.strip('!SineCalAngle ')#This is what the user will have to type in on discord so that it can detect work out the sum for the sine
        Sinemsg = float(Sinemsg)
        SineHyp = int(input("What is the length of the Hypotenuse?"))#This asks what the size of the Hypotenuse.
        SineOpp = int(input("What is the length of the opposite?"))#This asks what the size of the opposite.
        SineAngle = int(input("What is the angle size of the angle?"))#This asks what the size of the opposite.
        AngleWithS = math.sin(math.radians(SineAngle))
        Sine = AngleWithS * SineOpp / SineHyp 
        SineCalculation = math.sin-1(math.radians(Sine))             
        print("The answer for your sine finding missing angle calculation to the nearest 3 Decimal places is " + str(round(3)(SineCalculation) ))
        await client.send_message(message.channel, "The answer for your sine calculation to the nearest 3 Decimal places is " + str(round(3)(SineCalculation) ))
       # This is to find out a missing angle for a question using sine.
		# Function not working just yet.

        
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



@client.event
async def SineCalLength(message): 
	if message.content.startswith('!SineCalLength'):
        Sinemsg = str(message.content)#
        Sinemsg = Sinemsg.strip('!SineCalLength ')#This is what the user will have to type in on discord so that it can detect work out the sum for the sine
        Sinemsg = float(Sinemsg)
        Length1 = float(input("What is the length of the first side?"))
        SineAngle1 = int(input("What is the angle size of the 1st angle?"))
        SineAngle2 = int(input("What is the angle size of the second angle?"))     
        Angle1 = math.sin(math.radians(SineAngle1))
        Angle2 = math.sin(math.radians(SineAngle2))
        Sine  = Length1 * Angle1 / Angle2
        SineCalculation = (round(Sine, 3))
        print(SineCalculation)
      #  print("The answer for your sine calculation to 3 signifcant figures is " + str(round(3)(SineCalculation) ))
        await client.send_message(message.channel, "The answer for your sine calculation to 3 signifcant figures is " + str(round(3)(SineCalculation) ))
       #This is to find out the missing side for a question using sine.
     
                          
@client.event
async def on_message(message):
    print(message.content)
    await SineCalLength(message)
#This part of the code is not mine...    
@client.event
async def on_ready():
	print('Logged in as ' + client.user.name)
#This part of the code is not mine....
client.run(TOKEN)


@client.event
async def CosineCalLength(message)
	if message.content.startswith('!CosineCalLength'):
        Cosinemsg = str(message.content)#
        Cosinemsg = Sinemsg.strip('!CosineCalLength ')
        Cosinemsg = float(Cosinemsg)
        Side1 = float(input("What is the length of the smaller side?"))
        Side2 = float(input("What is the length of the longer side?"))
        Angle = int(input("What is the size of the angle?"))
        Powers = (Side1**2) + (Side2**2)
        CosineAngle = math.cos(math.radians(Angle))
        Cosine = (2 * Side1 * Side2) * CosineAngle
        CosineCalculation = Powers - (2 * Side1 * Side2 * CosineAngle) 
        SquaredCosine = math.sqrt(CosineCalculation)
        print(SquaredCosine)
        RSCosine = print(round(SquaredCosine, 2))
        await client.send_message(message.channel, "The answer for your Cosine calculation to 3 signifcant figures is " + str(RSCosine) )
                           
                                      
@client.event
async def on_message(message):
    print(message.content)
    await CosineCalLength(message)
#This part of the code is not mine...    
@client.event
async def on_ready():
	print('Logged in as ' + client.user.name)
#This part of the code is not mine....
client.run(TOKEN)                           
                           
               
                                                    
@client.event
async def CosineCalAngle(message):
    if message.content.startswith('!CosineCalAngle'):
        Cosinemsg = str(message.content)#
        Cosinemsg = Sinemsg.strip('!CosineCalAngle ')
        Cosinemsg = float(Cosinemsg)
        Side1 = float(input("What is the length of the smaller side?"))
        Side2 = float(input("What is the length of the longer side?"))
        Side3 = float(input("What is the length of the other side?"))
        Powers = ((Side1**2) + (Side2**2)) - (Side3**2)
        Angle = 2 * (Side1) * (Side2) 
        Cosine = Powers / Angle
        InCosine = math.degrees(math.acos(Cosine))
        print(InCosine)
                                                      
               
                                                   
@client.event
async def on_message(message):
    print(message.content)
    await CosineCalAngle(message)
#This part of the code is not mine...    
@client.event
async def on_ready():
	print('Logged in as ' + client.user.name)
#This part of the code is not mine....
client.run(TOKEN)                           




@client.event
async def TanCalAngle(message):
if message.content.startswith('!TanCalAngle'):
    Tanmsg = str(message.content)#
Tanmsg = Tanmsg.strip('!TanCalAngle ')
Tanmsg = float(Tanmsg)
TanOpp = int(input("What is the size of the opposite length?"))
TanAdj = int(input("What is the size of the Adjacent length?"))
Angle = TanOpp / TanAdj
TanAngleCalc= math.degrees(math.atan(Angle))
print(TanAngleCalc)



@client.event
async def on_message(message):
    print(message.content)
    await TanCalAngle(message)
#This part of the code is not mine...    
@client.event
async def on_ready():
	print('Logged in as ' + client.user.name)
#This part of the code is not mine....
client.run(TOKEN)    
    
    
    
    
    
@client.event
async def TanCalLength(message):
    if message.content.startswith('!TanCalLength'):
        Tanmsg = str(message.content)#
        Tanmsg = Tanmsg.strip('!TanCalLength ')
        Tanmsg = float(Tanmsg)
        Length1 = int(input("What is the size of the length of the Adjacent?"))
        Angle = int(input("What is the size of the angle?"))
        TanAngle = math.tan(math.radians(Angle))
        Calculation = Length1 * TanAngle 
        print (Calculation)
# using Tan to find the opposite length of the triangle.


@client.event
async def on_message(message):
    print(message.content)
    await TanCalLength(message)
#This part of the code is not mine...    
@client.event
async def on_ready():
	print('Logged in as ' + client.user.name)
#This part of the code is not mine....
client.run(TOKEN)  
                           
                           
                           
                           
                           