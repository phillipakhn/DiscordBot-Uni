#Arithmetics
import discord
import math 
TOKEN = 'NTAyMjI2MDYzNzYyMzkxMDUw.Dqk38g.KFDtyaHwMfRNK6RRUKYfpDj9L9Y'

client = discord.Client()
@client.event
async def Arithmetics(message):
    if message.content.startswith('!Arithmetics'):
        Arithmeticmsg = str(message.content)#
        Arithmeticmsg = Arithmeticmsg.strip('!Arithmetics ')
        Arithmeticmsg = str(Arithmeticmsg)
        print(Arithmeticmsg)
        mathOperator = await client.send_message(message.channel, "Which operator would you like to use to work out your calulation with?: Add, Sub, Mult or Div?")
        
        if mathOperator == Add or add:
            Number1 = await client.send_message(message.channel,"What is the first number that you want to use for your addition calulation?")
            if Number1 == int: 
                Arithmeticmsg = Arithmeticmsg.replace('None', '')
                Arithmeticmsg = "                 " + Arithmeticmsg + " 
            Number2 = await client.send_message(message.channel,"What is the second number that you want to use for your addition calulation?")
            if Number2 == int:
                Arithmeticmsg = Arithmeticmsg.replace('None', '')
                Arithmeticmsg = "                 " + Arithmeticmsg + " 
            ansAdd = Number1 + Number2 
            return ansAdd
        await client.send_message(message.channel,"The answer for your addition calulation is" + (ansAdd)) 
        
        
        
        if mathOperator == 'Subtraction' or 'subtraction':
            Number1 = await client.send_message(message.channel,"What is the first number that you want to use for your subtraction calulation?")
            if Number1 == int: 
                Arithmeticmsg = Arithmeticmsg.replace('None', '')
                Arithmeticmsg = "                 " + Arithmeticmsg + " 
            Number2 = await client.send_message(message.channel,"What is the second number that you want to use for your subtraction calulation?")
            if Number2 == int: 
                Arithmeticmsg = Arithmeticmsg.replace('None', '')
                Arithmeticmsg = "                 " + Arithmeticmsg + " 
            ansSub = Number1 - Number2 
            return ansSub 
        await client.send_message(message.channel,"The answer for your subtraction calulation is" + (ansSub))
        
        
        
        if mathOperator == 'Multiply' or 'multiply':
            Number1 = await client.send_message(message.channel,"What is the first number that you want to use for your multiply calulation?")
            if Number1 == int: 
                Arithmeticmsg = Arithmeticmsg.replace('None', '')
                Arithmeticmsg = "                 " + Arithmeticmsg + " 
            Number2 = await client.send_message(message.channel,"What is the second number that you want to use for your multiply calulation?")
            if Number2 == int: 
                Arithmeticmsg = Arithmeticmsg.replace('None', '')
                Arithmeticmsg = "                 " + Arithmeticmsg + " 
            ansMult = Number1 * Number2
            return ansMult
        await client.send_message(message.channel,"The answer for your multiplication calulation is" + (ansMult))
        
        
        
        
        if mathOperator == 'Division' or 'divison':
            Number1 = await client.send_message(message.channel,"What is the first number that you want to use for your divison calulation?")
            if Number1 == int: 
                Arithmeticmsg = Arithmeticmsg.replace('None', '')
                Arithmeticmsg = "                 " + Arithmeticmsg + " 
            Number2 = await client.send_message(message.channel,"What is the second number that you want to use for your divison calulation?")
            if Number2 == int:
                Arithmeticmsg = Arithmeticmsg.replace('None', '')
                Arithmeticmsg = "                 " + Arithmeticmsg + " 
            ansDivide = Number1 + Number2 
            return ansDivide 
        await client.send_message(message.channel,"The answer for your divison calulation is" + (ansDivide))
        
        
        
        else:
            await client.send_message(message.channel,"Calculations are not valid.")
        return False
   

   @client.event
async def on_message(message):
    print(message.content)
    await Arithmetics(message)
#This part of the code is not mine...    
@client.event
async def on_ready():
	print('Logged in as ' + client.user.name)
#This part of the code is not mine....
client.run(TOKEN)

async def Square(message):
    if message.content.startswith('!Square'):
        Squaremsg = str(message.content)
        Squaremsg = Squaremsg.strip('!Squaremsg ')
	Squaremsg = int(Squaremsg)
        print(Squaremsg)
        SquaredNum = int(message) * int(message)
        await client.send_message(message.channel,"The square number for the number" + str(message) "and the square value of the number is" + str(SquaredNum))
    else:
        await client.send_message(message.channel,"Square number has failed.")
    
@client.event
async def on_message(message):
    print(message.content)
    await Square(message)
#This part of the code is not mine...    
@client.event
async def on_ready():
	print('Logged in as ' + client.user.name)
#This part of the code is not mine....
client.run(TOKEN)















