from flask import Flask, jsonify
import requests
from Key import key
import TimeZone as timez

Search_api = "https://maps.googleapis.com/maps/api/place/textsearch/json"
Details_api ="https://maps.googleapis.com/maps/api/place/details/json"


"""Input: String(Location), Output:String(url)"""
def Results(Location,run):
	Search_input = {"key":key, "query":Location} # My API key and the location
	Search_req = requests.get(Search_api,Search_input) # Requests the location with my key
	Search_json = Search_req.json() # Json representaion of data returned 
	if run == 0:
		Place_id = Search_json["results"][0]["place_id"]# Searches Google's API for the Location
		Details_input = {"key":key, "placeid":Place_id}
		Details_req = requests.get(Details_api, params = Details_input)
		Details_json = Details_req.json()
		Url = Details_json["result"]["url"] # Fetches the URL of the Location
		return(Url)
	else:
		Lat = Search_json["results"][0]["geometry"]["location"]["lat"]
		Lng = Search_json["results"][0]["geometry"]["location"]["lng"]
		return(timez.Tzone(Lat,Lng))
		
	

