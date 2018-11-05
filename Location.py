import APIMaps as maps

'''Input:Object (message), Output: String (msg)'''
def Google(message):
		while True:
			try:
				Location = str(message.content) # converting the discord message to a string
				Location = Location.replace("!GoogleMaps","")
				Location = Location.replace(" ","")
				Valid = True
				msg = maps.Results(Location)
				msg = "Here you go " + str(msg)
				return msg	
			except IndexError: # When the location is out of range
				msg = "That location doesn't exist or it is not specific enough!"
				return msg
