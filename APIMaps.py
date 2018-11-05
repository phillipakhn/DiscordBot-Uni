from flask import Flask, jsonify
import requests
from Key import key

Search = "https://maps.googleapis.com/maps/api/place/textsearch/json"
Details ="https://maps.googleapis.com/maps/api/place/details/json"


"""Input: String(query), Output:String(url)"""
def Results(query):
	Search_payload = {"key":key, "query":query}
	Search_req = requests.get(Search, params = Search_payload)
	Search_json = Search_req.json()
	place_id = Search_json["results"][0]["place_id"]
	
	Details_payload = {"key":key, "placeid":place_id}
	Details_resp = requests.get(Details, params=Details_payload)
	Details_json = Details_resp.json()

	url = Details_json["result"]["url"]
	return(url)
	

