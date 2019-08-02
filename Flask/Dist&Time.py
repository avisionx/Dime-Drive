import requests
import json
loc1 = 'IIITD+Boys+Hostel'
loc2 = 'Cariappa+Vihar'
response = requests.get('https://maps.googleapis.com/maps/api/distancematrix/json?origins='+loc1+'&destinations=' + loc2 + '&mode=driving&language=fr-FR&key=AIzaSyD8EOCipsqcYeuJP76Ey7MumLdY0ojRmPs')
result = response.json()
distance = result.get('rows')[0].get('elements')[0].get('distance').get('text')
time     = result.get('rows')[0].get('elements')[0].get('duration').get('text')
print(distance)
print(time)
