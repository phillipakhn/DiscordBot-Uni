#PrimeNumbers
import math, discord 

TOKEN = 'NTAyMjI2MDYzNzYyMzkxMDUw.Dqk38g.KFDtyaHwMfRNK6RRUKYfpDj9L9Y'

client = discord.Client()

def Prime(message):

	if message.content.startswith('!Prime'):

		return

def primeN(message):
    for x in range(2,int(message**0.5)+1):#
        if message%x==0:
            return False

    return True
    #
    
    #def primeN(message):
    #for x in range(2,int(message**0.5)+1):
     #   if message%x==0 is False:
     #       print("Not Prime")
     #       return False
      #  if message%x==0 is True:
       #     print("This is a Prime Number.")
       #     return True
    
def exit(message):
    if message.content.startswith('!Exit'):
        exit()