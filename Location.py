import APIMaps as maps
from PIL import Image
import requests

'''Input:Object (message), Output: String (msg)'''
def Google(message,run):
		while True:
			try:
				Location = str(message.content) # converting the discord message to a string
				Location = Location.replace("!GoogleMaps","")
				Location = Location.replace("!Timezone","")
				Location = Location.replace("!Weather","")
				Location = Location.lstrip(' ')
				Location = Location.title()
				content = maps.Results(Location,run)
				if run == 0:
					msg = "Here you go " + str(content)
					return msg # Returns to Discord.py
				elif run == 1:
					msg = "The current time in " + maps.Format_Adr(Location) + " is "+ str(content[0]) + " " + str(content[2]) + " taken from " + str(content[1])
					return msg # Returns to Discord.py
				else:
					icon = content['weather'][0]['icon']
					icon_url = "http://openweathermap.org/img/w/"+str(icon)+".png"
					msg = "The current weather in " + maps.Format_Adr(Location) + " is " + str(content['weather'][0]['description'])
					Celsius = round((content['main']['temp'])- 273.15,1) # Coverting Kelvin to Celsius
					Temp = "The temperature is " + str(Celsius) + "ºC"
					print(Temp)
					if content['weather'][0]['main'] == "Rain" or content['weather'][0]['main'] == 'Thunderstorm':
						Rain = True
					else:
						Rain = False
					Condition = Advice(Celsius,Rain)
					return(msg,icon_url,Temp,Condition) # Returns to DiscordAPI.py
			except IndexError: # When the location is out of range
				msg = "That location doesn't exist or it is not specific enough!"
				return msg # Returns to Discord.py


def Advice(Celsius,Rain):
	if -20 < Celsius < 0:
		Condition = "It's FREEZING! Make sure to wrap up warm if you plan to go outside there!"
	elif Celsius < -19:
		Condition = "It's beyond FREEZING! Only go outside if it's necessary and make sure to wear very insulating clothes."
	elif 0 < Celsius < 16:
		Condition = "It's CHILLY out there! Make sure put a jumper on!"
		if Rain == True:
			Condition = Condition + " "+ "Also don't forget your coat!"
	elif 16 < Celsius < 21:
		Condition = "It's warm out there, but not quite shorts weather!"
		if Rain == True:
			Condition = Condition + " " + "Also don't forget your coat!"
	elif 20 < Celsius < 31:
		Condition = "It's nice and warm! Have fun but make sure to put suncream on if you burn easily."
		if Rain == True:
			Condition =  "It's nice and warm! However, it's raining so don't forget your coat!"
	elif 30 < Celsius < 51:
		Condition = "It's very HOT out there! Perfect holiday weather! Make sure to use suncream and drink plenty of water!"
		if Rain == True:
			Condition =  "It's very HOT out there! However, it's raining so not beach weather, also don't forget your coat!"
	elif Celsius > 50:
		Condition = "It's RIDICULOUSLY HOT! Don't go outside unless necessary!" 
	return Condition	
