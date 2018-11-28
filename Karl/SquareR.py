async def sRoot(message):
        if message.content.startswith('!SquareRoot'):#This is the message that the user will have to input on Discord for the program to start
        sRootmsg = str(message.content)
        sRootmsg = sRootmsg.strip('!SquareRoot ')
        sRootmsg = int(sRootmsg)# This changes the value of the variable so that it can get the square root of value
        print(sRootmsg)
        ans = math.sqrt(sRootmsg)#This is the square root function which I am using from the math library so that it can be used for the calulation.
        return(ans)
        await client.send_message(message.channel,"The square root for the number" + str(sRootmsg) "is" + (ans))#This is the message that shows the user the answer for the value they have entered using the function

@client.event
async def on_message(message):
    print(message.content)
    await sRoot(message)
    
@client.event
async def on_ready():
	print('Logged in as ' + client.user.name)

client.run(TOKEN)