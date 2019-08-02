import requests
import json
from uber_rides.session import Session
from uber_rides.client import UberRidesClient
import random


def getuberprice(a,b,c,d):
	tokens = ["nHAekV4vBpJmbgf_1DzaW1GgVAl5ggceN-X1_ARo","qMOnL1l20oAwreTtKAPuXhuFmWCTIJXe0tXZkjVe","APuykJdS83wzrNLDuRa13hIXci-DZ-VK7454kH_S","JA2aaRKKIsdXNSOG0ZtRzedVUegdQYsnrZ9pPvWE","mHUzAGLUDv9Fp1j-H1O3nVIx02gtDtL7NGpWJqz5"]
	token = random.choice(tokens)
	session = Session(server_token=token)
	client = UberRidesClient(session)
	response = client.get_price_estimates(
	    start_longitude=a,
	    start_latitude=b,
	    end_longitude=c,
	    end_latitude=d,
	    seat_count=2
	)
	#print(response.json)
	estimate = response.json.get('prices')
	for i in estimate:
		if i.get("display_name")=="UberGo":
			priceanddur = i
			x = priceanddur
	#print(estimate)
	return x


def geolocator(str):
	s = loc.replace(" ","+")
	print(loc)
	response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address='+loc+'&key=AIzaSyD8EOCipsqcYeuJP76Ey7MumLdY0ojRmPs')
	result = response.json()
	coor = []
	coor.append(result.get('results')[0].get('geometry').get('location').get('lat'))
	coor.append(result.get('results')[0].get('geometry').get('location').get('lng'))
	return coor



loc1 = 'IIITD+Boys+Hostel'
loc2 = 'Patparganj'
response = requests.get('https://maps.googleapis.com/maps/api/directions/json?origin='+loc1+'&destination=' + loc2 + '&mode=transit&alternatives=true&key=AIzaSyD8EOCipsqcYeuJP76Ey7MumLdY0ojRmPs')
result = response.json()
print(result)
print("hgvsgvas")
overview_polyline = result.get('routes')[0].get('overview_polyline').get('points')

routes = result.get('routes')
counter = 0
finalroutes = []
finaltimes = []
for i in routes:
	#remove this line
	if counter!=0:
		break
	counter+=1
	Metro_Stations = []
	Bus_Stations = []
	Polyline = []
	Polylinemode = [] 
	leg = i.get('legs')[0]
	step = leg.get('steps')
	time = leg.get('duration').get('text')
	distance = leg.get('distance').get('text')
	for i in step :
	    print(i.get('html_instructions'))
	    poly = i.get('polyline')
	    Polyline.append(poly.get('points'))
	    text =  i.get('html_instructions')
	    if (text[:10].find("Bus") != -1):
	        Polylinemode.append("Bus")
	        Transit_Details = i.get('transit_details')
	        Bus_Stations.append(Transit_Details.get('departure_stop').get('name'))
	        Bus_Stations.append(Transit_Details.get('arrival_stop').get('name')) 
	    elif (text[:10].find("Walk") != -1):
	        Polylinemode.append("Walk")
	    elif (text[:10].find("Metro") != -1):
	        #print("Metro")
	        Polylinemode.append("Metro")
	        Transit_Details = i.get('transit_details')
	        Metro_Stations.append(Transit_Details.get('departure_stop').get('name'))
	        Metro_Stations.append(Transit_Details.get('arrival_stop').get('name'))	
	print()
	print(time)
	print(distance)
	print()
	for i in Metro_Stations:
		print(i)
	print()	
	for i in Bus_Stations:
		print(i)
	# for i in Polyline:
	# 	print(i)
	# 	print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")	
	# print("____________________________________________________")	  



 