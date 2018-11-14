import discord, random, sys, openpyxl


TOKEN = 'NTA1MTAzMjg4MzcxNTExMzA2.DrkK6A.91Vlom28r5Zgb-6P2vyUHI9psbo'

client = discord.Client()


wb = openpyxl.load_workbook('example1.xlsx')
#type(wb)
sheet = wb['Sheet1']
#sheet['A1'].value = 0
sheet['B1'].value = 'Matt'
sheet['B2'].value = 'Alastair'
sheet['B3'].value = 'Kieran'
@client.event
async def on_message(message):
    if message.author == client.user:
        return
   





#COIN TOSS#   
        
    if message.content.startswith('!coin heads'):
        if author.id == "182146954384506880": #Tree
            
        
            x = random.randint(0,1)
            if x == 0:
                msg = ("You flipped a coin, it's tails. You lose")
                await client.send_message(message.channel, msg)
            
            elif x == 1:
                msg = ("You flipped a coin, it's heads. You win")
                await client.send_message(message.channel, msg)

                sheet['A1'].value = int(sheet['A1'].value) + 1
                score = sheet['A1'].value
                player =  ' {0.author.mention}'.format(message)
                await client.send_message(message.channel, player)
                await client.send_message(message.channel, score)
                wb.save('example1.xlsx')
                
        if author.id == "326831993520390154": #Alastair

            x = random.randint(0,1)
            if x == 0:
                msg = ("You flipped a coin, it's tails. You lose")
                await client.send_message(message.channel, msg)
            
            elif x == 1:
                msg = ("You flipped a coin, it's heads. You win")
                await client.send_message(message.channel, msg)

                sheet['A2'].value = int(sheet['A2'].value) + 1
                score = sheet['A2'].value
                player =  ' {0.author.mention}'.format(message)
                await client.send_message(message.channel, player)
                await client.send_message(message.channel, score)
                wb.save('example1.xlsx')


        if author.id == "187259473050599424": #Kieran
            
        
            x = random.randint(0,1)
            if x == 0:
                msg = ("You flipped a coin, it's tails. You lose")
                await client.send_message(message.channel, msg)
            
            elif x == 1:
                msg = ("You flipped a coin, it's heads. You win")
                await client.send_message(message.channel, msg)

                sheet['A3'].value = int(sheet['A3'].value) + 1
                score = sheet['A3'].value
                player =  ' {0.author.mention}'.format(message)
                await client.send_message(message.channel, player)
                await client.send_message(message.channel, score)
                wb.save('example1.xlsx')
                
        if author.id == "497343538242125834": #Tomas

            x = random.randint(0,1)
            if x == 0:
                msg = ("You flipped a coin, it's tails. You lose")
                await client.send_message(message.channel, msg)
            
            elif x == 1:
                msg = ("You flipped a coin, it's heads. You win")
                await client.send_message(message.channel, msg)

                sheet['A4'].value = int(sheet['A4'].value) + 1
                score = sheet['A4'].value
                player =  ' {0.author.mention}'.format(message)
                await client.send_message(message.channel, player)
                await client.send_message(message.channel, score)
                wb.save('example1.xlsx')


        if author.id == "497343197429628941": #Mango
            
        
            x = random.randint(0,1)
            if x == 0:
                msg = ("You flipped a coin, it's tails. You lose")
                await client.send_message(message.channel, msg)
            
            elif x == 1:
                msg = ("You flipped a coin, it's heads. You win")
                await client.send_message(message.channel, msg)

                sheet['A5'].value = int(sheet['A5'].value) + 1
                score = sheet['A5'].value
                player =  ' {0.author.mention}'.format(message)
                await client.send_message(message.channel, player)
                await client.send_message(message.channel, score)
                wb.save('example1.xlsx')
                
        if author.id == "497345883437006849": #Karl

            x = random.randint(0,1)
            if x == 0:
                msg = ("You flipped a coin, it's tails. You lose")
                await client.send_message(message.channel, msg)
            
            elif x == 1:
                msg = ("You flipped a coin, it's heads. You win")
                await client.send_message(message.channel, msg)

                sheet['A6'].value = int(sheet['A6'].value) + 1
                score = sheet['A6'].value
                player =  ' {0.author.mention}'.format(message)
                await client.send_message(message.channel, player)
                await client.send_message(message.channel, score)
                wb.save('example1.xlsx')
        
            
            





    if message.content.startswith('!coin tails'):
        if author.id == "182146954384506880": #Tree

            x = random.randint(0,1)
            if x == 0:
                msg = ("You flipped a coin, it's tails. You win")
                await client.send_message(message.channel, msg)

                sheet['A1'].value = int(sheet['A1'].value) + 1
                score = sheet['A1'].value
                player = ' {0.author.mention}'.format(message)
                await client.send_message(message.channel, player)
                await client.send_message(message.channel, score)
                wb.save('example1.xlsx')
            
           
            elif x == 1:
                msg = ("You flipped a coin, it's heads. You lose")
                await client.send_message(message.channel, msg)

        if author.id == "326831993520390154": #Alastair

            x = random.randint(0,1)
            if x == 0:
                msg = ("You flipped a coin, it's tails. You win")
                await client.send_message(message.channel, msg)

                sheet['A2'].value = int(sheet['A2'].value) + 1
                score = sheet['A2'].value
                player = ' {0.author.mention}'.format(message)
                await client.send_message(message.channel, player)
                await client.send_message(message.channel, score)
                wb.save('example1.xlsx')
            
           
            elif x == 1:
                msg = ("You flipped a coin, it's heads. You lose")
                await client.send_message(message.channel, msg)



        if author.id == "187259473050599424": #Kieran

            x = random.randint(0,1)
            if x == 0:
                msg = ("You flipped a coin, it's tails. You win")
                await client.send_message(message.channel, msg)

                sheet['A3'].value = int(sheet['A3'].value) + 1
                score = sheet['A3'].value
                player = ' {0.author.mention}'.format(message)
                await client.send_message(message.channel, player)
                await client.send_message(message.channel, score)
                wb.save('example1.xlsx')
            
           
            elif x == 1:
                msg = ("You flipped a coin, it's heads. You lose")
                await client.send_message(message.channel, msg)


        if author.id == "497343538242125834": #Tomas

            x = random.randint(0,1)
            if x == 0:
                msg = ("You flipped a coin, it's tails. You win")
                await client.send_message(message.channel, msg)

                sheet['A4'].value = int(sheet['A4'].value) + 1
                score = sheet['A4'].value
                player = ' {0.author.mention}'.format(message)
                await client.send_message(message.channel, player)
                await client.send_message(message.channel, score)
                wb.save('example1.xlsx')
            
           
            elif x == 1:
                msg = ("You flipped a coin, it's heads. You lose")
                await client.send_message(message.channel, msg)


        if author.id == "497343197429628941": #Mango

            x = random.randint(0,1)
            if x == 0:
                msg = ("You flipped a coin, it's tails. You win")
                await client.send_message(message.channel, msg)

                sheet['A5'].value = int(sheet['A5'].value) + 1
                score = sheet['A5'].value
                player = ' {0.author.mention}'.format(message)
                await client.send_message(message.channel, player)
                await client.send_message(message.channel, score)
                wb.save('example1.xlsx')
            
           
            elif x == 1:
                msg = ("You flipped a coin, it's heads. You lose")
                await client.send_message(message.channel, msg)


        if author.id == "497345883437006849": #Karl

            x = random.randint(0,1)
            if x == 0:
                msg = ("You flipped a coin, it's tails. You win")
                await client.send_message(message.channel, msg)

                sheet['A6'].value = int(sheet['A6'].value) + 1
                score = sheet['A6'].value
                player = ' {0.author.mention}'.format(message)
                await client.send_message(message.channel, player)
                await client.send_message(message.channel, score)
                wb.save('example1.xlsx')
            
           
            elif x == 1:
                msg = ("You flipped a coin, it's heads. You lose")
                await client.send_message(message.channel, msg)

        






    if message.content.startswith('!leaderboards'):
        tree_score = sheet['A1'].value
        tree_name = sheet['B1'].value
        alastair_score = sheet['A2'].value
        alastair_name = sheet['B2'].value
        kieran_score = sheet['A3'].value
        kieran_name = sheet['B3'].value
        tomas_score = sheet['A4'].value
        tomas_name = sheet['B4'].value
        mango_score = sheet['A5'].value
        mango_name = sheet['B5'].value
        karl_score = sheet['A6'].value
        karl_name = sheet['B6'].value
        
        await client.send_message(message.channel, tree_score)
        await client.send_message(message.channel, tree_name)
        await client.send_message(message.channel, alastair_score)
        await client.send_message(message.channel, alastair_name)
        await client.send_message(message.channel, kieran_score)
        await client.send_message(message.channel, kieran_name)
        await client.send_message(message.channel, tomas_score)
        await client.send_message(message.channel, tomas_name)
        await client.send_message(message.channel, mango_score)
        await client.send_message(message.channel, mango_name)
        await client.send_message(message.channel, karl_score)
        await client.send_message(message.channel, karl_name)







        
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
            msg = ("rock vs rock  DRAW!")
            await client.send_message(message.channel, msg)
             
      
        elif enemy == 1:
            msg = ("rock vs paper YOU LOST!")
            await client.send_message(message.channel, msg)
      
        elif enemy == 2:
            msg = ("rock vs scissors YOU WON!")
            await client.send_message(message.channel, msg)
            
      


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
