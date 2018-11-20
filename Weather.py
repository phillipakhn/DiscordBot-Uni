import discord
from flask import Flask, jsonify
import requests
from Key import Weather_key


'''Input: Float(Lat,Lng), Output: Dictionary(Search_json)'''
def Forecast(Lat,Lng):
	Lat = str(Lat)
	Lng = str(Lng)
	Weather_api = "http://api.openweathermap.org/data/2.5/weather?lat="+(Lat)+"&lon="+(Lng)
	Search_input = { "APPID":Weather_key,}
	Search_req = requests.get(Weather_api,Search_input) # Requests the data from the Open Weather API
	Search_json = Search_req.json()
	print(Search_json)
	return(Search_json) # Returns to APIMaps.py


