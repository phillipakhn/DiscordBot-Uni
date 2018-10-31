# Google Earth
import webbrowser
import discord
import WebSite as w

def Google(message):
		Postcode = str(message.content) # converting the discord message to a string
		Postcode = Postcode.replace("!GoogleMaps","")
		Postcode = Postcode.replace(" ","")
		Valid = Validate(Postcode)
		if Valid == False:
			msg = "That postcode is impossible!"
			return msg
		else:
			w.Maps(Postcode)
			msg = "Here you go "
			return msg	
		
def Validate(Postcode):
	length = len(Postcode)		
	if length > 7 or length < 5:
		return False
		print("Invalid postcode")		
	elif Postcode[0].isalpha() == False:
		return False
	elif Postcode[length-1].isalpha() == False: # must be length-1 becuase length does'nt include index 0
		return False
	else:
		return True	 	
