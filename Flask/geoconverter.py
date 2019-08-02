import requests
import json

def geolocator(loc):
	s = loc.replace(" ","+")
	print(loc)
	response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address='+loc+'&key=AIzaSyD8EOCipsqcYeuJP76Ey7MumLdY0ojRmPs')
	result = response.json()
	coor = []
	coor.append(result.get('results')[0].get('geometry').get('location').get('lat'))
	coor.append(result.get('results')[0].get('geometry').get('location').get('lng'))
	return coor
a = geolocator("IIITD Boys Hostel")
print(a[0])
print(a[1])









