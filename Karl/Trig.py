import math
import discord


TOKEN = 'NTAyMjI2MDYzNzYyMzkxMDUw.Dqk38g.KFDtyaHwMfRNK6RRUKYfpDj9L9Y'

client = discord.Client()

@client.event
async def SineCalAngle(message): 
    if message.content.startswith('!SineCalAngle'):#This is what the user will have to input onto Discord for the program to run. 
        Sinemsg = str(message.content)
        Sinemsg = Sinemsg.strip('!SineCalAngle ')
        Sinemsg = str(Sinemsg)
        
        SinemsgH = await client.send_message(message.channel,"What is the length of the Hypotenuse?")#This message will be asked to the users for them to answer using Discord.
        SinemsgH = SinemsgH.replace('None', '')
        SinemsgH = "                 " + SinemsgH + " "
        
        SinemsgO = await client.send_message(message.channel,"What is the length of the opposite?")#This message will be asked to the users for them to answer using Discord.
        SinemsgO = SinemsgO.replace('None', '')
        SinemsgO = "                 " + SinemsgO + " "
        
        SinemsgA = await client.send_message(message.channel,"What is the size of the angle?")#This message will be asked to the users for them to answer using Discord.
        SinemsgA = SinemsgA.replace('None', '')
        SinemsgA = "                 " + SinemsgA + " "
        print(Sinemsg)
        print(SinemsgH)
        print(SinemsgO)
        print(SinemsgA)
        
        if type(SinemsgH) and type(SinemsgO) and type(SinemsgA)== int:
            AngleWithS = math.sin(math.radians(SineAngle))#Here I have used sin from the math libary using math.radians so that I can use it to get the sin of the angle the user has inputted.
            Sine = SinemsgA * SinemsgO / SinemsgH 
            SineCalculation = math.degrees(math.asin(Sine)) #This then does inverse sin of the previous calculation above so that the angle can be made. 
            SineCalculation2 = (round(SineCalculation, 2))#This line of code is to round the previous calculation to two decimal places to get the final answer.
            return(SineCalculation2)
            await client.send_message(message.channel, "The answer for your sine calculation to the nearest 2 Decimal places is " + str(SineCalAngle(0)) + "°" )#This is the message that will be outputted to the user after the calculation is solved. 
        else:
            await client.send_message(message.channel, "You have not inputted integers.")
            return False
    # function for calulating the missing angle using inverse sin.
    
        
@client.event
async def on_message(message):
    print(message.content)
    await SineCalAngle(message)
    
@client.event
async def on_ready():
	print('Logged in as ' + client.user.name)
    
client.run(TOKEN)



@client.event
async def SineCalLength(message): 
    if message.content.startswith('!SineCalLength'):#This is what the user will have to input onto Discord for the program to run. 
        Sinemsg = str(message.content)
        Sinemsg = Sinemsg.strip('!SineCalLength ')
        Sinemsg = str(Sinemsg)
        Length1 = await client.send_message(message.channel,"What is the length of the first side?")#This message will be asked to the users for them to answer using Discord.
        Length1 = Length1.replace('None', '')
        Length1 = "                 " + Length1 + " "
        
        SineAngle1 = await client.send_message(message.channel,"What is the angle size of the 1st angle?")#This message will be asked to the users for them to answer using Discord.
        
        SineAngle1 = SineAngle1.replace('None', '')
        SineAngle1 = "                 " + SineAngle1 + " "
        
        SineAngle2 = await client.send_message(message.channel,"What is the angle size of the second angle?")#This message will be asked to the users for them to answer using Discord.  
        SineAngle2 = SineAngle2.replace('None', '')
        SineAngle2 = "                 " + SineAngle2 + " "
        
        print(Length1)
        print(SineAngle1)
        print(SineAngle2)
        if type(Length1) or type(SineAngle1) or type(SineAngle2)==int:
            Angle1 = math.sin(math.radians(SineAngle1))#This gets inverse sine of the 1st angle.
            Angle2 = math.sin(math.radians(SineAngle2))#This gets inverse sine of the 2nd angle.
            Sine = Length1 * Angle1 / Angle2
            SineCalculation = (round(Sine, 3))#This line of code is to round the previous calculation to three decimal places to get the final answer.
            return(SineCalculation)
            await client.send_message(message.channel, "The answer for your sine calculation to 3 decimal places is " + str(SineCalLength(0)) + " cm" )
        else:
            await client.send_message(message.channel, "You have not inputted integers.")
            return False
       #This is to find out the missing side for a question using sine.
     
                          
@client.event
async def on_message(message):
    print(message.content)
    await SineCalLength(message)
    
@client.event
async def on_ready():
	print('Logged in as ' + client.user.name)
client.run(TOKEN)


@client.event
async def CosineCalLength(message):
    if message.content.startswith('!CosineCalLength'):#This is what the user will have to input onto Discord for the program to run. 
        Cosinemsg = str(message.content)
        Cosinemsg = Sinemsg.strip('!CosineCalLength ')
        Cosinemsg = str(Cosinemsg)
        
        Side1 = await client.send_message(message.channel,"What is the length of the smaller side?")#This message will be asked to the users for them to answer using Discord.
        
        Side2 = await client.send_message(message.channel,"What is the length of the longer side?")#This message will be asked to the users for them to answer using Discord.
        
        Angle = await client.send_message(message.channel,"What is the size of the angle?")#This message will be asked to the users for them to answer using Discord.
        
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
            RSCosine = (round(SquaredCosine, 2))#This line of code is to round the previous calculation to two decimal places to get the final answer.
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
    
@client.event
async def on_ready():
	print('Logged in as ' + client.user.name)

client.run(TOKEN)                           
                           
               
                                                    
@client.event
async def CosineCalAngle(message):
    if message.content.startswith('!CosineCalAngle'):#This is what the user will have to input onto Discord for the program to run.
        Cosinemsg = str(message.content)#
        Cosinemsg = Sinemsg.strip('!CosineCalAngle ')
        Cosinemsg = str(Cosinemsg)
        
        Side1 = await client.send_message(message.channel,"What is the length of the smaller side?")#This message will be asked to the users for them to answer using Discord.
        
        Side2 = await client.send_message(message.channel,"What is the length of the longer side?")#This message will be asked to the users for them to answer using Discord.
        
        Side3 = await client.send_message(message.channel,"What is the length of the other side?")#This message will be asked to the users for them to answer using Discord.
        
        print(Cosinemsg)
        print(Side1)
        print(Side2)
        print(Side3)
        if type(Side1) and type(Side2) and type(Side3) == float:
            Powers = ((Side1**2) + (Side2**2)) - (Side3**2) 
            Angle = 2 * (Side1) * (Side2) 
            Cosine = Powers / Angle
            InCosine = math.degrees(math.acos(Cosine))
            InCosineCal = (round(InCosine, 1))#This line of code is to round the previous calculation to one decimal places to get the final answer.
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
    
@client.event
async def on_ready():
	print('Logged in as ' + client.user.name)

client.run(TOKEN)                           




@client.event
async def TanCalAngle(message):
    if message.content.startswith('!TanCalAngle'):#This is what the user will have to input onto Discord for the program to run. 
        Tanmsg = str(message.content)
        Tanmsg = Tanmsg.strip('!TanCalAngle ')
        Tanmsg = str(Tanmsg)
        
        TanOpp = await client.send_message(message.channel,"What is the size of the opposite length?")#This message will be asked to the users for them to answer using Discord.
        
        TanAdj = await client.send_message(message.channel,"What is the size of the Adjacent length?")#This message will be asked to the users for them to answer using Discord.
        print(Tanmsg)
        print(TanOpp)
        print(TanAdj)
    if type(TanOpp) and type(TanAdj) == int:
        Angle = TanOpp / TanAdj
        TanAngleCalc= math.degrees(math.atan(Angle))
        TanAngleCalcR = (round(TanAngleCalc, 1))#This line of code is to round the previous calculation to one decimal places to get the final answer.
        return(TanAngleCalcR)
        await client.send_message(message.channel, "The answer for your Tan calculation to one Decimal place is " + str(TanCalAngle(0)) + "°")
    else:
        await client.send_message(message.channel, "The value you have inputted isn't a integer.")
        return False


@client.event
async def on_message(message):
    print(message.content)
    await TanCalAngle(message)
    
@client.event
async def on_ready():
	print('Logged in as ' + client.user.name)

client.run(TOKEN)    
    
    
    
    
    
@client.event
async def TanCalLength(message):
    if message.content.startswith('!TanCalLength'):#This is what the user will have to input onto Discord for the program to run. 
        Tanmsg = str(message.content)#
        Tanmsg = Tanmsg.strip('!TanCalLength ')
        Tanmsg = str(Tanmsg)
        
        Length1 = await client.send_message(message.channel,"What is the size of the length of the Adjacent?")#This message will be asked to the users for them to answer using Discord.
        
        Angle = await client.send_message(message.channel,"What is the size of the angle?")#This message will be asked to the users for them to answer using Discord.
        
        print(Tanmsg)
        print(Length1)
        print(Angle)
        if type(Length1) and type(Angle) == int:
            TanAngle = math.tan(math.radians(Angle))#This gets
            Calculation = Length1 * TanAngle 
            TanCalculation = (round(Calculation, 2))#This line of code is to round the previous calculation to two decimal places to get the final answer.
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
    
@client.event
async def on_ready():
	print('Logged in as ' + client.user.name)

client.run(TOKEN)  
                           
                           
                           
                           
                           
