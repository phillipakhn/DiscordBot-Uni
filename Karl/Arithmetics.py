#Arithmetics
import discord
import math 
import operator
TOKEN = 'NTAyMjI2MDYzNzYyMzkxMDUw.Dqk38g.KFDtyaHwMfRNK6RRUKYfpDj9L9Y'

client = discord.Client()
@client.event
async def Arithmetics(message):
    if message.content.startswith('!Arithmetics'):
        Arithmeticmsg = str(message.content)#
        Arithmeticmsg = Arithmeticmsg.strip('!Arithmetics ')#This is what the user will have to type in on discord so that it can detect whether the number is a prime or not
        Arithmeticmsg = int(Arithmeticmsg)#Changes the user's inputted message which was string to a integer
        print(Arithmeticmsg)
        operator = input("Which operator would you like to use to work out your calulation with: Add, Sub, Mult or Div?")
        if Arithmeticmsg == str:
            await client.send_message(message.channel, "You have not inputted a integer or decimal to be calculated.")
            return False
        if operator == :
            operator.add
        if operator == Sub:
            operator.
            
            
            
            
        
        




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















