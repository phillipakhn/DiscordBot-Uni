# Google Earth
import webbrowser
import discord

def Google(message):
	if message.content.startswith('!GoogleEarth'):
		webbrowser.open('https://earth.google.com/web/')
		msg = 'Working'
		return msg
#


