asnyc def Square(message):
    if message.content.startswith('!Square'):
        Squaremsg = str(message.content)
        Squaremsg = Squaremsg.strip('!Square ')
        Squaremsg = int(Squaremsg)
        print(Squaremsg)
        SquaredNum = int(message) * int(message)
        return True
        await client.send_message(message.channel,"The square number for the number" + str(message) "and the square value of the number is" + str(SquaredNum))
    else:
        return False
        await client.send_message(message.channel,"Square number has failed.")