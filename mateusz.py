import discord, random, sys, openpyxl, time   

TOKEN = 'NTAyMjI2MDYzNzYyMzkxMDUw.Dqk38g.KFDtyaHwMfRNK6RRUKYfpDj9L9Y'   #- dc bot's token
#TOKEN = 'NTA1MTAzMjg4MzcxNTExMzA2.DrkK6A.91Vlom28r5Zgb-6P2vyUHI9psbo'   - previous bot

client = discord.Client()


wb = openpyxl.load_workbook('example1.xlsx') #to open excel file
sheet = wb['Sheet1']    # to operate on this excel file
#sheet['A1'].value = 0 #setting value for the first time
sheet['B1'].value = 'Matt'
sheet['B2'].value = 'Alastair'
sheet['B3'].value = 'Kieran'
#sheet['C1'].value = 100000 #setting value for the first time 


#tried to change the coin toss into a function to save some lines of code, but I kept
#getting errors.

#@client.event
#def cointossheads(column):
#    x = random.randint(0,1)
#    if x == 0:
#        msg = ("You flipped a coin, it's tails. You lose")
#        await client.send_message(message.channel, msg)
#            
#    elif x == 1:
#        msg = ("You flipped a coin, it's heads. You win")
#        await client.send_message(message.channel, msg)
#
#        sheet[column].value = int(sheet[column].value) + 1
#        score = sheet[column].value
#        player =  ' {0.author.mention}'.format(message)
#        await client.send_message(message.channel, player)
#        await client.send_message(message.channel, score)
#        wb.save('example1.xlsx')

@client.event
async def on_message(message):
    if message.author == client.user: #to prevent bot from responding to himself
        return
   





#COIN TOSS#   
        
    if message.content.startswith('!coin heads'):

        #cointossheads("A1")  - tried calling a function but kept getting errors.

        author = message.author
        #if author.id == "182146954384506880": #Tree 
            
        
        x = random.randint(0,1)
        if x == 0:
            msg = ("You flipped a coin, it's tails. You lose")
            await client.send_message(message.channel, msg) # sending message to discord server
            
        elif x == 1:
            
            msg = ("You flipped a coin, it's heads. You win")
            await client.send_message(message.channel, msg)
            
            if author.id == "182146954384506880": #Tree
                sheet['A1'].value = int(sheet['A1'].value) + 1 #after winning a bet, add 1 to leaderboards
                score = sheet['A1'].value

            elif author.id == "326831993520390154": #Alastair
                sheet['A2'].value = int(sheet['A2'].value) + 1
                score = sheet['A2'].value

            elif author.id == "187259473050599424": #Kieran
                sheet['A3'].value = int(sheet['A3'].value) + 1
                score = sheet['A3'].value

            elif author.id == "497343538242125834": #Tomas
                sheet['A4'].value = int(sheet['A4'].value) + 1
                score = sheet['A4'].value

            elif author.id == "497343197429628941": #Mango
                sheet['A5'].value = int(sheet['A5'].value) + 1
                score = sheet['A5'].value

            elif author.id == "497345883437006849": #Karl
                sheet['A6'].value = int(sheet['A6'].value) + 1
                score = sheet['A6'].value

                

            player =  ' {0.author.mention}'.format(message) #bot mentions the winner in a message
            await client.send_message(message.channel, player)
            await client.send_message(message.channel, score)
            wb.save('example1.xlsx') #saving excel file in the end of each game
                




    if message.content.startswith('!coin tails'):
        author = message.author
        

        x = random.randint(0,1)
        if x == 0:
            msg = ("You flipped a coin, it's tails. You win")
            await client.send_message(message.channel, msg)

            if author.id == "182146954384506880": #Tree
                sheet['A1'].value = int(sheet['A1'].value) + 1 
                score = sheet['A1'].value

            elif author.id == "326831993520390154": #Alastair
                sheet['A2'].value = int(sheet['A2'].value) + 1
                score = sheet['A2'].value

            elif author.id == "187259473050599424": #Kieran
                sheet['A3'].value = int(sheet['A3'].value) + 1
                score = sheet['A3'].value

            elif author.id == "497343538242125834": #Tomas
                sheet['A4'].value = int(sheet['A4'].value) + 1
                score = sheet['A4'].value

            elif author.id == "497343197429628941": #Mango
                sheet['A5'].value = int(sheet['A5'].value) + 1
                score = sheet['A5'].value

            elif author.id == "497345883437006849": #Karl
                sheet['A6'].value = int(sheet['A6'].value) + 1
                score = sheet['A6'].value
                
            player = ' {0.author.mention}'.format(message)
            await client.send_message(message.channel, player)
            await client.send_message(message.channel, score)
            wb.save('example1.xlsx')
            
           
        elif x == 1:
            msg = ("You flipped a coin, it's heads. You lose")
            await client.send_message(message.channel, msg)


 
        





#LEADERBOARDS
    if message.content.startswith('!leaderboards'):
        tree_score = sheet['A1'].value  #reading all scores and names of players from excel file
        tree_name = sheet['B1'].value + " "
        alastair_score = sheet['A2'].value
        alastair_name = sheet['B2'].value + " "
        kieran_score = sheet['A3'].value
        kieran_name = sheet['B3'].value + " "
        tomas_score = sheet['A4'].value
        tomas_name = sheet['B4'].value + " "
        mango_score = sheet['A5'].value
        mango_name = sheet['B5'].value + " "
        karl_score = sheet['A6'].value
        karl_name = sheet['B6'].value + " "
        reaction = sheet['C1'].value
        player = sheet['C2'].value
        
        await client.send_message(message.channel, "COIN FLIP:\n" + tree_name + str(tree_score) + "\n" + alastair_name + str(alastair_score) + "\n" + kieran_name + str(kieran_score) + "\n" + tomas_name + str(tomas_score) + "\n" + mango_name + str(mango_score) + "\n" + karl_name + str(karl_score) + "\nREACTION:\n " + str(reaction) + "ms - " + player) # sending messages with scores to chat
        #await client.send_message(message.channel, tree_name)
        #await client.send_message(message.channel, alastair_score)
        #await client.send_message(message.channel, alastair_name)
        #await client.send_message(message.channel, kieran_score)
        #await client.send_message(message.channel, kieran_name)
        #await client.send_message(message.channel, tomas_score)
        #await client.send_message(message.channel, tomas_name)
        #await client.send_message(message.channel, mango_score)
        #await client.send_message(message.channel, mango_name)
        #await client.send_message(message.channel, karl_score)
        #await client.send_message(message.channel, karl_name)







        
#RUSSIAN ROULETTE#

    if message.content.startswith('!russia'):
        #serv = discord.Server(id='502223039912476692')   getting server id to ban the player that loses the game
        author = message.author
        russia = random.randint(0,5)
        if russia == 3:
            msg = ('You are dead')
            await client.send_message(message.channel, msg)
                     
            #await client.ban("182146954384506880",serv,1)   kept getting tons of errors with ban           
            #await client.send_message("USER BANNED!!")
        else:
            msg = ('Lucky you')
            await client.send_message(message.channel, msg)
            


#ROCK PAPER SCISSORS#


    if message.content.startswith('!rps'):

        await client.send_message(message.channel, '!rock, !paper, !scissors?')

        


        
        await client.wait_for_message(author=message.author, content='!rock')
        #if message.content.startswith('!rock'):
    
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
        #if message.content.startswith('!paper'):

        enemy = random.randint(0,2)  #0 = rock, 1 = paper, 2 = scissors
    
        if enemy == 0:
            await client.send_message(message.channel, "paper vs rock YOU WON!")
            
        elif enemy == 1:
            await client.send_message(message.channel, "paper vs paper DRAW!")
            
        elif enemy == 2:
            await client.send_message(message.channel, "paper vs scissors YOU LOST!")
            
      


        await client.wait_for_message(author=message.author, content='!scissors')
        #if message.content.startswith('!scissors'):
        
        enemy = random.randint(0,2)  #0 = rock, 1 = paper, 2 = scissors
    
        if enemy == 0:
            await client.send_message(message.channel, "scissors vs rock YOU LOST!")
            
        elif enemy == 1:
            await client.send_message(message.channel, "scissors vs paper YOU WON!")
            
        elif enemy == 2:
            await client.send_message(message.channel, "scissors vs scissors DRAW!")
            


#REACTION
    if message.content.startswith("!reaction"):
        player = message.author
        await client.send_message(message.channel, "send q when you're ready")
        await client.wait_for_message(author=message.author, content="q") #can't just press enter so we have to send something
        time.sleep(.5)   #delay between 2 messages
        await client.send_message(message.channel, "Get ready!")
        time.sleep(random.randint(1,4))  #random delay so we don't know what to expect
        then = time.time()    #takes time
        await client.send_message(message.channel, "GO!")
        await client.wait_for_message(author=message.author, content='q')
        reaction_time = time.time()-then  #takes time and subtracts the previous time from it to get the reaction time
        msg = round(reaction_time*1000,2)   #transforming it to ms and rounding
        await client.send_message(message.channel, content = str(msg) + "ms") #NOTE due to latency, scores are inaccurate
        best = sheet['C1'].value
        if msg < best:
            sheet['C1'].value = msg
            sheet['C2'].value = str(player)
        wb.save('example1.xlsx')
        
    
client.run(TOKEN)  # runs the bot
