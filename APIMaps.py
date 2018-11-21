from flask import Flask, jsonify
import requests
from Key import key
import TimeZone as timez
import Weather as weather

Search_api = "https://maps.googleapis.com/maps/api/place/textsearch/json"
Details_api ="https://maps.googleapis.com/maps/api/place/details/json"


"""Input: String(Location),Integer(run), Output: String(url,timez.Tzone(Lat,Lng)) Dictionary:(weather.Forecast(Lat,Lng)),"""
def Results(Location,run):
	Search_input = {"key":key, "query":Location} # My API key and the location
	Search_req = requests.get(Search_api,Search_input) # Requests the location with my key
	Search_json = Search_req.json() # Json representaion of data returned
	print(Search_json) 
	if run == 0:
		Place_id = Search_json["results"][0]["place_id"]# Searches Google's API for the Location
		Details_input = {"key":key, "placeid":Place_id}
		Details_req = requests.get(Details_api, params = Details_input)
		Details_json = Details_req.json()
		Url = Details_json["result"]["url"] # Fetches the URL of the Location
		return Url # Returns to Location.py
	else:
		Lat = Search_json["results"][0]["geometry"]["location"]["lat"]
		Lng = Search_json["results"][0]["geometry"]["location"]["lng"]
		if run == 1:
			return(timez.Tzone(Lat,Lng)) # Returns to Location.py
		else:
			return(weather.Forecast(Lat,Lng)) # Returns to Location.py

"""Input: String(Location), Output: String(Address)"""
def Format_Adr(Location):
	Search_input = {"key":key, "query":Location} # My API key and the location
	Search_req = requests.get(Search_api,Search_input) # Requests the location with my key
	Search_json = Search_req.json() # Json representaion of data returned
	Address = Search_json["results"][0]["formatted_address"]
	return Address
	

