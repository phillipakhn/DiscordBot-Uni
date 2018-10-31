#PrimeNumbers
import math, discord 

TOKEN = 'NTAyMjI2MDYzNzYyMzkxMDUw.Dqk38g.KFDtyaHwMfRNK6RRUKYfpDj9L9Y'
client = discord.Client()

@client.event
async def primeN(message):
    if message.content.startswith('!Primes'):
        if (message==1):
            return False
    elif (message==2):
        return True
    else:
        for x in range(2,message):
            if(message % x==0):
                print("This is not a prime number.")
                await client.send_message(message.channel, "This is not a prime number.")
                return False 
        print("This is a prime number.") 
        await client.send_message(message.channel, "This is a prime number.")
        return True 
    

#def primeN(Message):
#    if (Message==1):
#        return False
#    elif (Message==2):
#        return True;
#    else:
#        for x in range(2,Message):
#            if(Message % x==0):
#                return False print("This is not a prime number.")
#        return True print("This is a prime number.") 
         
def exitFunc(message):
    if message.content.startswith('!Exit'):
        exit()
        #when users enters exit it will end the primes game for the user 