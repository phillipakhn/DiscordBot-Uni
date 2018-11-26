def Square(message):
    if message.content.startswith('!Square'):
        Squaremsg = str(message.content)
        Squaremsg = Squaremsg.strip('!Square ')
        Squaremsg = int(Squaremsg)
        print(Squaremsg)
        SquaredNum = int(message) * int(message)
        return True
        await client.send_message(message.channel,"The square number for the number" + str(message) "and the square value of the number is" + str(SquaredNum))
        
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