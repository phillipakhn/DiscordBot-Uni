import discord, random


#TOKEN = 'NTA1MTAzMjg4MzcxNTExMzA2.DrkK6A.91Vlom28r5Zgb-6P2vyUHI9psbo'
TOKEM = 'NTAyMjI2MDYzNzYyMzkxMDUw.Dqk38g.KFDtyaHwMfRNK6RRUKYfpDj9L9Y'

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return
   

#COIN TOSS#   
        
    if message.content.startswith('!coin heads'):
        
        x = random.randint(0,1)
        if x == 0:
            msg = ("You flipped a coin, it's tails. You lose")
            await client.send_message(message.channel, msg)
            
        elif x == 1:
            msg = ("You flipped a coin, it's heads. You win")
            await client.send_message(message.channel, msg)
            #await client.send_message(message.channel, leaderboards)
            
            

    if message.content.startswith('!coin tails'):


        x = random.randint(0,1)
        if x == 0:
            msg = ("You flipped a coin, it's tails. You win")
            await client.send_message(message.channel, msg)
            #await client.send_message(message.channel, leaderboards)
            
           
        elif x == 1:
            msg = ("You flipped a coin, it's heads. You lose")
            await client.send_message(message.channel, msg)

#RUSSIAN ROULETTE#

    if message.content.startswith('!russia'):
        russia = random.randint(0,5)
        if russia == 0:
            msg = ('You are dead')
            await client.send_message(message.channel, msg)
            async def kick(ctx, userName: discord.User):
                """Kick A User from server"""
                await client.kick(userName)
        elif russia > 0:
            msg = ('Lucky you')
            await client.send_message(message.channel, msg)
            


#ROCK PAPER SCISSORS#


    if message.content.startswith('!rps'):

        await client.send_message(message.channel, '!rock, !paper, !scissors?')

        


        
        await client.wait_for_message(author=message.author, content='!rock')
    
        enemy = random.randint(0,2)  #0 = rock, 1 = paper, 2 = scissors

        if enemy == 0:
            await client.send_message(message.channel, "rock vs rock  DRAW!")
             
        elif enemy == 1:
            await client.send_message(message.channel, "rock vs paper YOU LOST!")
      
        elif enemy == 2:
            await client.send_message(message.channel, "rock vs scissors YOU WON!")
            
      


        await client.wait_for_message(author=message.author, content='!paper')

        enemy = random.randint(0,2)  #0 = rock, 1 = paper, 2 = scissors
    
        if enemy == 0:
            await client.send_message(message.channel, "paper vs rock YOU WON!")
      
        elif enemy == 1:
            await client.send_message(message.channel, "paper vs paper DRAW!")
      
        elif enemy == 2:
            await client.send_message(message.channel, "paper vs scissors YOU LOST!")
      
      
        await client.wait_for_message(author=message.author, content='!scissors')
        
        enemy = random.randint(0,2)  #0 = rock, 1 = paper, 2 = scissors
    
        if enemy == 0:
            await client.send_message(message.channel, "scissors vs rock YOU LOST!")
      
        elif enemy == 1:
            await client.send_message(message.channel, "scissors vs paper YOU WON!")
      
        elif enemy == 2:
            await client.send_message(message.channel, "scissors vs scissors DRAW!")


        
    
client.run(TOKEN)
