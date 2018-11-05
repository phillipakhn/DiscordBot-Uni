from flask import Flask, jsonify
import requests
from Key import key

Search_api = "https://maps.googleapis.com/maps/api/place/textsearch/json"
Details_api ="https://maps.googleapis.com/maps/api/place/details/json"


"""Input: String(query), Output:String(url)"""
def Results(Location):
	Search_input = {"key":key, "query":Location} # My API key and the location
	Search_req = requests.get(Search_api, params = Search_input) # Requests the location with my key, Params formats "Search_input" so that Google API can use it
	Search_json = Search_req.json() # Json representaion of data returned 
	Place_id = Search_json["results"][0]["place_id"]# Searches Google's API for the Location
	
	Details_input = {"key":key, "placeid":Place_id}
	Details_req = requests.get(Details_api, params = Details_input)
	Details_json = Details_req.json()

	url = Details_json["result"]["url"] # Fetches the URL of the Location
	return(url)
	

