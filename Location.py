import APIMaps as maps

'''Input:Object (message), Output: String (msg)'''
def Google(message,run):
		while True:
			try:
				Location = str(message.content) # converting the discord message to a string
				Location = Location.replace("!GoogleMaps","")
				Location = Location.replace("!Timezone","")
				Location = Location.lstrip(' ')
				msg = maps.Results(Location,run)
				if run == 0:
					msg = "Here you go " + str(msg)
				else:
					msg = "The time in " + Location + " is "+ str(msg[0]) + " " + str(msg[2]) + " taken from " + str(msg[1])
				return (msg)	
			except IndexError: # When the location is out of range
				msg = "That location doesn't exist or it is not specific enough!"
				return (msg)
