import math
import discord


TOKEN = 'NTAyMjI2MDYzNzYyMzkxMDUw.Dqk38g.KFDtyaHwMfRNK6RRUKYfpDj9L9Y'

client = discord.Client()

@client.event
async def SineCalAngle(message): 
    if message.content.startswith('!SineCalAngle'):
        Sinemsg = str(message.content)
        Sinemsg = Sinemsg.strip('!SineCalAngle ')
        Sinemsg = int(Sinemsg)
        SinemsgH = await client.send_message(message.channel,"What is the length of the Hypotenuse?")
        SinemsgO = await client.send_message(message.channel,"What is the length of the opposite?")
        SinemsgA = await client.send_message(message.channel,"What is the size of the angle?")
        print(Sinemsg)
        print(SinemsgH)
        print(SinemsgO)
        print(SinemsgA)
        if type(SinemsgH) and type(SinemsgO) and type(SinemsgA)== int:
            AngleWithS = math.sin(math.radians(SineAngle))
            Sine = SinemsgA * SinemsgO / SinemsgH 
            SineCalculation = math.degrees(math.asin(Sine)) 
            SineCalculation2 = (round(SineCalculation, 2))
            return(SineCalculation2)
            await client.send_message(message.channel, "The answer for your sine calculation to the nearest 2 Decimal places is " + str(SineCalAngle(0)) + "°" )
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


pass
@client.event
async def SineCalLength(message): 
    if message.content.startswith('!SineCalLength'):
        Sinemsg = str(message.content)
        Sinemsg = Sinemsg.strip('!SineCalLength ')
        Sinemsg = float(Sinemsg)
        Length1 = await client.send_message(message.channel,"What is the length of the first side?")
        SineAngle1 = await client.send_message(message.channel,"What is the angle size of the 1st angle?")
        SineAngle2 = await client.send_message(message.channel,"What is the angle size of the second angle?")     
        print(Length1)
        print(SineAngle1)
        print(SineAngle2)
        if type(Length1) or type(SineAngle1) or type(SineAngle2)==int:
            Angle1 = math.sin(math.radians(SineAngle1))
            Angle2 = math.sin(math.radians(SineAngle2))
            Sine = Length1 * Angle1 / Angle2
            SineCalculation = (round(Sine, 3))
            return(SineCalculation)
            await client.send_message(message.channel, "The answer for your sine calculation to 3 signifcant figures is " + str(SineCalLength(0)) + " cm" )
        else:
            await client.send_message(message.channel, "You have not inputted integers.")
            return False
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
async def CosineCalLength(message):
    if message.content.startswith('!CosineCalLength'):
        Cosinemsg = str(message.content)
        Cosinemsg = Sinemsg.strip('!CosineCalLength ')
        Cosinemsg = float(Cosinemsg)
        Side1 = await client.send_message(message.channel,"What is the length of the smaller side?")
        Side2 = await client.send_message(message.channel,"What is the length of the longer side?")
        Angle = await client.send_message(message.channel,"What is the size of the angle?")
        print(Cosinemsg)
        print(Side1)
        print(Side2)
        print(Angle)
        if type(Side1) or type(Side2) or (Angle) == int:
            Powers = (Side1**2) + (Side2**2)
            CosineAngle = math.cos(math.radians(Angle))
            Cosine = (2 * Side1 * Side2) * CosineAngle
            CosineCalculation = Powers - (2 * Side1 * Side2 * CosineAngle) 
            SquaredCosine = math.sqrt(CosineCalculation)
            RSCosine = (round(SquaredCosine, 2))
            return(RSCosine)
            await client.send_message(message.channel, "The answer for your Cosine calculation to 2 signifcant figures is " + str(CosineCalLength(0)) + " cm" )
        else:
            await client.send_message(message.channel, "You have not inputted any numbers.")
            return False
        #this is for finding out the missing length using cosine.                  
                                      
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
        Side1 = await client.send_message(message.channel,"What is the length of the smaller side?")
        Side2 = await client.send_message(message.channel,"What is the length of the longer side?")
        Side3 = await client.send_message(message.channel,"What is the length of the other side?")
        print(Cosinemsg)
        print(Side1)
        print(Side2)
        print(Side3)
        if type(Side1) and type(Side2) and type(Side3) == float:
            Powers = ((Side1**2) + (Side2**2)) - (Side3**2) 
            Angle = 2 * (Side1) * (Side2) 
            Cosine = Powers / Angle
            InCosine = math.degrees(math.acos(Cosine))
            InCosineCal = (round(InCosine, 1))
            return(InCosineCal)
            await client.send_message(message.channel, "The answer for your Cosine calculation to 1 decimal place is " + str(CosineCalAngle(0)) + "°")                                          
            return(InCosine)
        else:
            await client.send_message(message.channel, "You have not inputted a valid value.")
            return False
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
        Tanmsg = str(message.content)
        Tanmsg = Tanmsg.strip('!TanCalAngle ')
        Tanmsg = float(Tanmsg)
        TanOpp = await client.send_message(message.channel,"What is the size of the opposite length?")
        TanAdj = await client.send_message(message.channel,"What is the size of the Adjacent length?")
    print(Tanmsg)
    print(TanOpp)
    print(TanAdj)
    if type(TanOpp) and type(TanAdj) == int:
        Angle = TanOpp / TanAdj
        TanAngleCalc= math.degrees(math.atan(Angle))
        TanAngleCalcR = (round(TanAngleCalc, 1))
        return(TanAngleCalcR)
        await client.send_message(message.channel, "The answer for your Tan calculation to one Decimal place is " + str(TanCalAngle(0)) + "°")
    else:
        await client.send_message(message.channel, "The value you have inputted isn't a integer.")
        return False


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
        Length1 = await client.send_message(message.channel,"What is the size of the length of the Adjacent?")
        Angle = await client.send_message(message.channel,"What is the size of the angle?")
        print(Tanmsg)
        print(Length1)
        print(Angle)
        if type(Length1) and type(Angle) == int:
            TanAngle = math.tan(math.radians(Angle))
            Calculation = Length1 * TanAngle 
            TanCalculation = (round(Calculation, 2))
            return (TanCalculation)
            await client.send_message(message.channel, "The answer for your Tan calculation to 2 decimal places is " + str(TanCalLength(0)) + " cm" )
        else:
            await client.send_message(message.channel, "The value you have inputted is not a integer.")
            return False
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
                           
                           
                           
                           
                           