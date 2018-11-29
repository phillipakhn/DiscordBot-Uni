import math

import discord

TOKEN = 'NTAyMjI2MDYzNzYyMzkxMDUw.Dqk38g.KFDtyaHwMfRNK6RRUKYfpDj9L9Y'

client = discord.Client()

@client.event
async def SineCalAngle(message):#Function for calculating the missing angle using inverse sin.
    if message.content.startswith('!SineCalAngle'):#This is what the user will have to input onto Discord for the program to run. 
        Sinemsg = str(message.content)
        Sinemsg = Sinemsg.strip('!SineCalAngle ')
        Sinemsg = str(Sinemsg)
        
        SinemsgH = "What is the length of the Hypotenuse?"
        await client.send_message(message.channel,(SinemsgH))#This will output a message to the user so that the user can then input the hypotenuse to the chatbot.
        SinemsgH = SinemsgH.replace('None', '')
        SinemsgH = "                 " + SinemsgH + " "
        
        SinemsgO = "What is the length of the opposite?"
        await client.send_message(message.channel,(SinemsgO))#This will output a message to the user so that the user can then input the opposite to the chatbot.
        SinemsgO = SinemsgO.replace('None', '')
        SinemsgO = "                 " + SinemsgO + " "
        
        SinemsgA = "What is the size of the angle?"
        await client.send_message(message.channel,(SinemsgA))#This will output a message to the user so that the user can then input the angle to the chatbot.
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
            SineCalculationR = (round(SineCalculation, 2))#This line of code is to round the previous calculation to two decimal places to get the final answer.
            SineCalculationAns = "The answer for your sine calculation to the nearest 2 decimal places is " + str(SineCalculationR) + "°"
            await client.send_message(message.channel,(SineCalculationAns))#This is the message will be outputted to the user after the calculation is solved. 
                 
@client.event
async def on_message(message):
    print(message.content)
    await SineCalAngle(message)
    
@client.event
async def on_ready():
	print('Logged in as ' + client.user.name)
    
client.run(TOKEN)


@client.event
async def SineCalLength(message):#This is to find out the missing side for a question using sine.
    if message.content.startswith('!SineCalLength'):#This is what the user will have to input onto Discord for the program to run. 
        Sinemsg = str(message.content)
        Sinemsg = Sinemsg.strip('!SineCalLength ')
        Sinemsg = str(Sinemsg)
        
        Length1 = "What is the length of the first side?"
        await client.send_message(message.channel,(Length1))#This will output a message to the user so that the user can then input the first side to the chatbot.
        Length1 = Length1.replace('None', '')
        Length1 = "                 " + Length1 + " "
        
        SineAngle1 = "What is the angle size of the 1st angle?"
        await client.send_message(message.channel,(SineAngle1))#This will output a message to the user so that the user can then input the first angle to the chatbot.
        SineAngle1 = SineAngle1.replace('None', '')
        SineAngle1 = "                 " + SineAngle1 + " "
        
        SineAngle2 = "What is the angle size of the second angle?" 
        await client.send_message(message.channel,(SineAngle2))#This will output a message to the user so that the user can then input the second angle to the chatbot.
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
            SineCalculationSent = "The answer for your sine calculation to 3 decimal places is " + str(SineCalculation) + " cm"
            await client.send_message(message.channel,(SineCalculationSent))#This is the message will be outputted to the user after the calculation is solved.
                               
@client.event
async def on_message(message):
    print(message.content)
    await SineCalLength(message)
    
@client.event
async def on_ready():
	print('Logged in as ' + client.user.name)
client.run(TOKEN)


@client.event
async def CosineCalLength(message):#This is for finding out the missing length using cosine.
    if message.content.startswith('!CosineCalLength'):#This is what the user will have to input onto Discord for the program to run. 
        Cosinemsg = str(message.content)
        Cosinemsg = Sinemsg.strip('!CosineCalLength ')
        Cosinemsg = str(Cosinemsg)
        
        Side1 = "What is the length of the smaller side?" 
        await client.send_message(message.channel,(Side1))#This will output a message to the user so that the user can then input the smaller side to the chatbot. 
        Side1 = Side1.replace('None', '')
        Side1 = "                 " + Side1 + " "
        
        Side2 = "What is the length of the longer side?" 
        await client.send_message(message.channel,(Side2))#This will output a message to the user so that the user can then input the longer side to the chatbot.
        Side2 = Side2.replace('None', '')
        Side2 = "                 " + Side2 + " "
        
        Angle = "What is the size of the angle?"
        await client.send_message(message.channel,(Angle))#This will output a message to the user so that the user can then input a angle for the chatbot.
        print(Cosinemsg)
        print(Side1)
        print(Side2)
        print(Angle)
        
        if type(Side1) or type(Side2) or (Angle) == int:
            Powers = (Side1**2) + (Side2**2)
            CosineAngle = math.cos(math.radians(Angle))
            Cosine = (2 * Side1 * Side2) * CosineAngle
            CosineCalculation = Powers - (2 * Side1 * Side2 * CosineAngle) 
            SquaredCosine = math.sqrt(CosineCalculation)#This square roots the calculation from above.
            RSCosine = (round(SquaredCosine, 2))#This line of code is to round the previous calculation to two decimal places to get the final answer.  
            RSCosineSent = "The answer for your Cosine calculation to 2 signifcant figures is " + str(RSCosine) + " cm"
            await client.send_message(message.channel,(RSCosineSent))#This is the message will be outputted to the user after the calculation is solved.
                          
                                      
@client.event
async def on_message(message):
    print(message.content)
    await CosineCalLength(message)
    
@client.event
async def on_ready():
	print('Logged in as ' + client.user.name)

client.run(TOKEN)                           
                           
        
                                                    
@client.event
async def CosineCalAngle(message):#Function for working out the missing angle using inverse cosine.
    if message.content.startswith('!CosineCalAngle'):#This is what the user will have to input onto Discord for the program to run.
        Cosinemsg = str(message.content)#
        Cosinemsg = Sinemsg.strip('!CosineCalAngle ')
        Cosinemsg = str(Cosinemsg)
        
        Side1 = "What is the length of the smaller side?"
        await client.send_message(message.channel,(Side1))#This will output a message to the user so that the user can then input a length for the smaller side for the chatbot.
        Side1 = Side1.replace('None', '')
        Side1 = "                 " + Side1 + " "
        
        Side2 = "What is the length of the longer side?"
        await client.send_message(message.channel,(Side2))#This will output a message to the user so that the user can then input the longer side for the chatbot.
        Side2 = Side2.replace('None', '')
        Side2 = "                 " + Side2 + " "
        
        Side3 = "What is the length of the other side?" 
        await client.send_message(message.channel,(Side3))#This will output a message to the user so that they can input the final side for the chatbot.
        Side3 = Side3.replace('None', '')
        Side3 = "                 " + Side3 + " "
        
        print(Cosinemsg)
        print(Side1)
        print(Side2)
        print(Side3)
        
        if type(Side1) and type(Side2) and type(Side3) == float:
            Powers = ((Side1**2) + (Side2**2)) - (Side3**2) 
            Angle = 2 * (Side1) * (Side2) 
            Cosine = Powers / Angle
            InCosine = math.degrees(math.acos(Cosine))#This uses inverse cosine functiom so that it can find the angle.
            InCosineCal = (round(InCosine, 1))#This line of code is to round the previous calculation to one decimal places to get the final answer.
            InCosineCalSent = "The answer for your Cosine calculation to 1 decimal place is " + str(InCosineCal) + "°"
            await client.send_message(message.channel,(InCosineCalSent))#This is the message that will be outputted to the user from the chatbot that is containing the calculation.                                        
            

@client.event
async def on_message(message):
    print(message.content)
    await CosineCalAngle(message)
    
@client.event
async def on_ready():
	print('Logged in as ' + client.user.name)

client.run(TOKEN)                           

@client.event
async def TanCalAngle(message):#Function for working out the missing angle using inverse tangent.
    if message.content.startswith('!TanCalAngle'):#This is what the user will have to input onto Discord for the program to run. 
        Tanmsg = str(message.content)
        Tanmsg = Tanmsg.strip('!TanCalAngle ')
        Tanmsg = str(Tanmsg)
        
        TanOpp = "What is the size of the opposite length?"
        await client.send_message(message.channel,(TanOpp))#This will output a message to the user so that they can input the opposite side.
        TanOpp = TanOpp.replace('None', '')
        TanOpp = "                 " + TanOpp + " "
        
        TanAdj = "What is the size of the Adjacent length?" 
        await client.send_message(message.channel,(TanAdj))#This will output a message to the user so that they can input the adjacent side.
        TanAdj = TanAdj.replace('None', '')
        TanAdj = "                 " + TanAdj + " "
        print(Tanmsg)
        print(TanOpp)
        print(TanAdj)
        
    if type(TanOpp) and type(TanAdj) == int:
        Angle = TanOpp / TanAdj
        TanAngleCalc= math.degrees(math.atan(Angle))#This is where the inverse tangent built in function from math is used for the calculation to find the length.
        TanAngleCalcR = (round(TanAngleCalc, 1))#This line of code is to round the previous calculation to one decimal places to get the final answer.
        TanAngleCalcRSent = "The answer for your Tan calculation to one decimal place is " + str(TanAngleCalcR) + "°"
        await client.send_message(message.channel,(TanAngleCalcRSent))#This is the message that will be outputted to the user from the chatbot that is containing the calculation. 



@client.event
async def on_message(message):
    print(message.content)
    await TanCalAngle(message)
    
@client.event
async def on_ready():
	print('Logged in as ' + client.user.name)

client.run(TOKEN)    
    

@client.event
async def TanCalLength(message):#Function for calculating the length of a side using tangent.
    if message.content.startswith('!TanCalLength'):#This is what the user will have to input onto Discord for the program to run. 
        Tanmsg = str(message.content)
        Tanmsg = Tanmsg.strip('!TanCalLength ')
        Tanmsg = str(Tanmsg)
        
        Length1 = "What is the size of the length of the Adjacent?"
        await client.send_message(message.channel,(Length1))#
        Length1 = Length1.replace('None', '')
        Length1 = "                 " + Length1 + " "
        
        Angle = "What is the size of the angle?"
        await client.send_message(message.channel,(Angle))
        Angle = Angle.replace('None', '')
        Angle = "                 " + Angle + " "
        print(Tanmsg)
        print(Length1)
        print(Angle)
        
        if type(Length1) and type(Angle) == int:
            TanAngle = math.tan(math.radians(Angle))#This uses tangent so that it can find out the missing length.
            Calculation = Length1 * TanAngle 
            TanCalculation = (round(Calculation, 2))#This line of code is to round the previous calculation to two decimal places to get the final answer.
            TanCalculationSent = "The answer for your Tan calculation to 2 decimal places is " + str(TanCalculation) + " cm"
            await client.send_message(message.channel,(TanCalculationSent))#This is the message that will be outputted to the user


@client.event
async def on_message(message):
    print(message.content)
    await TanCalLength(message)
    
@client.event
async def on_ready():
	print('Logged in as ' + client.user.name)

client.run(TOKEN)  
                           
                           
                           
                           
                           
