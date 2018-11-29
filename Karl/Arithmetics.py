import discord

import math 

TOKEN = 'NTAyMjI2MDYzNzYyMzkxMDUw.Dqk38g.KFDtyaHwMfRNK6RRUKYfpDj9L9Y'

client = discord.Client()

@client.event
async def Arithmetics(message):
    if message.content.startswith('!Arithmetics'):#This is what the user will have to input on Discord for the program to run.
        Arithmeticmsg = str(message.content)
        Arithmeticmsg = Arithmeticmsg.strip('!Arithmetics ')
        Arithmeticmsg = str(Arithmeticmsg)
        print(Arithmeticmsg)
        mathOperator = "Which operator would you like to use to work out your calculation with?: Add, Sub, Mult or Div?"        
        await client.send_message(message.channel,(mathOperator))#This will output a message asking the user to pick which maths operator they want to use.
                                  
        if mathOperator == Add or add:#This is what the user must enter in order for the function to work for adding the numbers.
            Number1 = "What is the first number that you want to use for your addition calculation?"
            await client.send_message(message.channel,(Number1))#This will output a message asking the user for the first number.
            if Number1 == int:#This is to check that the Number1 is an integer instead of a string so that the numbers can be added together.
                Number1 = Number1.replace('None', '')
                Number1 = "                 " + Number1 + " "            
            Number2 = "What is the second number that you want to use for your addition calculation?"
            await client.send_message(message.channel,(Number2))#This will output a message asking the user for the second number.
            if Number2 == int:#This is to check that the Number2 is an integer instead of a string so that the numbers can be added.
                Number2 = Number2.replace('None', '')
                Number2 = "                 " + Number2 + " "
            ansAdd = Number1 + Number2 
            ansAddSent = "The answer for your addition calculation is" + str(ansAdd)
            await client.send_message(message.channel,(ansAddSent))#This will output a message that will have the answer for the addition calculation to the user.
            
        if mathOperator == 'Subtraction' or 'subtraction':#This is what the user must enter in order for the function to work for subtracting the numbers.
            Number1 = "What is the first number that you want to use for your subtraction calculation?"
            await client.send_message(message.channel,(Number1))#This will output a message asking the user for the first number.
            if Number1 == int:#This is to check that the Number1 is an integer instead of a string so that the number can be used in the subtraction calculation.
                Number1 = Number1.replace('None', '')
                Number1 = "                 " + Number1 + " "
            Number2 = "What is the second number that you want to use for your subtraction calculation?"
            await client.send_message(message.channel,(Number2))#This will output a message asking the user for the second number.
            if Number2 == int:#This is to check that the Number2 is an integer instead of a string so that the number can be used in the subtraction calculation.
                Number2 = Number2.replace('None', '')
                Number2 = "                 " + Number2 + " "
            ansSub = Number1 - Number2 
            ansSubSent = "The answer for your subtraction calculation is" + str(ansSub)
            await client.send_message(message.channel,(ansSubSent))#This will output a message that will have the answer for the subtraction calculation to the user.       
        
        if mathOperator == 'Multiply' or 'multiply':#This is what the user must enter in order for the function to work for multiplying the numbers.
            Number1 = "What is the first number that you want to use for your multiplication calculation?"
            await client.send_message(message.channel,(Number1))#This will output a message asking the user for the first number.
            if Number1 == int:#This is to check that the Number1 is an integer instead of a string so that the number can be used in the multiplication calculation.
                Number1 = Number1.replace('None', '')
                Number1 = "                 " + Number1 + " "
            Number2 = "What is the second number that you want to use for your multiplication calculation?"
            await client.send_message(message.channel,(Number2))#This will output a message asking the user for the second number.
            if Number2 == int:#This is to check that the Number2 is an integer instead of a string so that the number can be used in the multiplication calculation.
                Number2 = Number2.replace('None', '')
                Number2 = "                 " + Number2 + " "
            ansMult = Number1 * Number2
            ansMultSent = "The answer for your multiplication calculation is" + str(ansMult)
            await client.send_message(message.channel,(ansMultSent))#This will output a message that will have the answer for the multiplication calculation to the user.
        
        if mathOperator == 'Division' or 'division':#This is what the user must enter in order for the function to work for dividing the numbers.
            Number1 = "What is the first number that you want to use for your division calculation?"
            await client.send_message(message.channel,(Number1))#This will output a message asking the user for the first number.
            if Number1 == int:#This is to check that the Number1 is an integer instead of a string so that the number can be used in the divison calculation.
                Number1 = Number1.replace('None', '')
                Number1 = "                 " + Number1 + "  "
            Number2 = "What is the second number that you want to use for your division calculation?"
            await client.send_message(message.channel,(Number2))#This will output a message asking the user for the second number.
            if Number2 == int:#This is to check that the Number2 is an integer instead of a string so that the number can be used in the divison calculation.
                Number2 = Number2.replace('None', '')
                Number2 = "                 " + Number2 + " "
            ansDivide = Number1 / Number2 
            ansDivideSent = "The answer for your division calculation is" + str(ansDivide)
            await client.send_message(message.channel,(ansDivideSent))#This will output a message that will have the answer for the division calculation to the user.
          
        
@client.event
async def on_message(message):
    print(message.content)
    await Arithmetics(message)
    
@client.event
async def on_ready():
	print('Logged in as ' + client.user.name)

client.run(TOKEN)

  
        
      









