# Google Maps
import WebSite as w

'''Funtion: Sets "message" to a string and then manipulates it.
Input:Object (message), Output: String (msg)'''
def Google(message):
		Postcode = str(message.content) # converting the discord message to a string
		Postcode = Postcode.replace("!GoogleMaps","")
		Postcode = Postcode.replace(" ","")
		Valid = Validate(Postcode)
		if Valid == False:
			msg = "That postcode is impossible!"
			return msg
		else:
			msg = w.Maps(Postcode) # Calls the "Maps" function in "WebSite.py".
			msg = "Here you go " + str(msg)
			return msg	


'''Function: Validates the postcode.
Input: String (Postcode) , Output: Boolean'''		
def Validate(Postcode):
	length = len(Postcode)		
	if length > 7 or length < 5:
		return False
		print("Invalid postcode")		
	elif Postcode[0].isalpha() == False: # Checking if the first index is a letter.
		return False
	elif Postcode[length-1].isalpha() == False: # must be length-1 becuase length does'nt include index 0
		return False
	else:
		return True	 	
