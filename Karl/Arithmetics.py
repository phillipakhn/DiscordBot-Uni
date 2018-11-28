#Arithmetics
import discord
import math 
TOKEN = 'NTAyMjI2MDYzNzYyMzkxMDUw.Dqk38g.KFDtyaHwMfRNK6RRUKYfpDj9L9Y'

client = discord.Client()
@client.event
async def Arithmetics(message):
    if message.content.startswith('!Arithmetics'):#This is what the user will have to input on Discord for the program to run.
        Arithmeticmsg = str(message.content)#
        Arithmeticmsg = Arithmeticmsg.strip('!Arithmetics ')
        Arithmeticmsg = str(Arithmeticmsg)
        print(Arithmeticmsg)
        mathOperator = await client.send_message(message.channel, "Which operator would you like to use to work out your calulation with?: Add, Sub, Mult or Div?")
        
        if mathOperator == Add or add:
            Number1 = await client.send_message(message.channel,"What is the first number that you want to use for your addition calulation?")
            if Number1 == int: 
                Number1 = Number1.replace('None', '')
                Number1 = "                 " + Number1 + " "
            Number2 = await client.send_message(message.channel,"What is the second number that you want to use for your addition calulation?")
            if Number2 == int:
                Number2 = Number2.replace('None', '')
                Number2 = "                 " + Number2 + " "
            ansAdd = Number1 + Number2 
            return ansAdd
        await client.send_message(message.channel,"The answer for your addition calulation is" + (ansAdd)) 
        
        if mathOperator == 'Subtraction' or 'subtraction':
            Number1 = await client.send_message(message.channel,"What is the first number that you want to use for your subtraction calulation?")
            if Number1 == int: 
                Number1 = Number1.replace('None', '')
                Number1 = "                 " + Number1 + " "
            Number2 = await client.send_message(message.channel,"What is the second number that you want to use for your subtraction calulation?")
            if Number2 == int: 
                Number2 = Number2.replace('None', '')
                Number2 = "                 " + Number2 + " "
            ansSub = Number1 - Number2 
            return ansSub 
        await client.send_message(message.channel,"The answer for your subtraction calulation is" + (ansSub))
        
        if mathOperator == 'Multiply' or 'multiply':
            Number1 = await client.send_message(message.channel,"What is the first number that you want to use for your multiply calulation?")
            if Number1 == int: 
                Number1 = Number1.replace('None', '')
                Number1 = "                 " + Number1 + " "
            Number2 = await client.send_message(message.channel,"What is the second number that you want to use for your multiply calulation?")
            if Number2 == int: 
                Number2 = Number2.replace('None', '')
                Number2 = "                 " + Number2 + " "
            ansMult = Number1 * Number2
            return ansMult
        await client.send_message(message.channel,"The answer for your multiplication calulation is" + (ansMult))
        
        if mathOperator == 'Division' or 'divison':
            Number1 = await client.send_message(message.channel,"What is the first number that you want to use for your divison calulation?")
            if Number1 == int: 
                Number1 = Number1.replace('None', '')
                Number1 = "                 " + Number1 + "  "
            Number2 = await client.send_message(message.channel,"What is the second number that you want to use for your divison calulation?")
            if Number2 == int:
                Number2 = Number2.replace('None', '')
                Number2 = "                 " + Number2 + " "
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


  
        
      









