# Time Zones
from flask import Flask, jsonify
import requests
from Key import key
import time
import datetime

Time_api = "https://maps.googleapis.com/maps/api/timezone/json?"

"""Input: integer(Lat,Lng), Output:String()"""
def Tzone(Lat,Lng):
	Timestamp = time.time() # Seconds since epoch 1st Jan 1970
	Search_input = {'location': "%s,%s" % (Lat, Lng), "timestamp":Timestamp,"key":key,} # My API key and the location in longitude and latitude
	print(Search_input)
	Search_req = requests.get(Time_api,Search_input) # Requests the location with my key
	print(Search_req)
	Search_json = Search_req.json() # Json representaion of data returned 
	print(Search_json)
	Time_Zone = Search_json["timeZoneId"]#Searches Google's API for the Location
	Time_Name = Search_json["timeZoneName"]
	Time_Time = int(Search_json["rawOffset"]/3600) # Searches for hourOffset and divides by 3600 to get it in hours
	print(Time_Zone,Time_Name)
	Newtime = Clock(Time_Time)
	return(Newtime,Time_Zone,Time_Name)

def Clock(Time_Time): 
	now = datetime.datetime.now()
	if now.hour+Time_Time>23:
		Adjust = Time_Time-24
	elif now.hour+Time_Time<0:
		Adjust = Time_Time+24
	else:
		Adjust = 0
	Newtime = datetime.time(now.hour+(Adjust), now.minute, now.second) # adjusts time to location
	Newtime = str(Newtime)
	print(Newtime)
	return(Newtime)
