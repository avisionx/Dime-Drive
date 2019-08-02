import requests
import json
from uber_rides.session import Session
from uber_rides.client import UberRidesClient
import random
import copy 

# Violet Line
violet_line = ["Kashmere Gate","Lal Quila","Jama Masjid","Delhi Gate","ITO","Mandi House","Janpath","Central Secretariat","Khan Market","Jawaharlal Nehru Stadium","Jangpura","Lajpat Nagar","Moolchand","Kailash Colony","Nehru Place","Kalkaji Mandir","Govind Puri","Harkesh Nagar Okhla","Jasola Apollo","Sarita Vihar","Mohan Estate","Tughlakabad","Badarpur","Sarai","NHPC Chowk","Mewala Maharajpur","Sector- 28","Manav Rachna - Badkal Mor","Old Faridabad","Lakhani Armaan - Neelam Chowk Ajronda","Bata Chowk","Escorts Mujesar"]


# Pink Line 1
pink_line_1 = ["Shiv Vihar" ,"Johri Enclave" ,"Gokulpuri" ,"Maujpur- Babarpur" ,"I.P. Extension" ,"Jafrabad" ,"Welcome" ,"East Azad Nagar" ,"Krishna Nagar" ,"Karkarduma Court" ,"Karkarduma" ,"Anand Vihar ISBT" ,"IP Extension" ,"Trilokpuri- Sanjay Lake"]

# Pink Line 2
pink_line_2 = ["Lajpat Nagar" ,"South Extension" ,"Ina" ,"Sarojini Nagar" ,"Bhikaji Cama Place GAIL" ,"Sir Vishveshwaraiah Moti Bagh" ,"Durgabai Deshmukh South Campus" ,"Delhi Cantt." ,"Naraina Vihar" ,"Mayapuri" ,"Rajouri Garden" ,"ESI Basaidarapur" ,"Punjabi Bagh" ,"Shakurpur" ,"Netaji Subhash Place" ,"Shalimar Bagh" ,"Azadpur" ,"Majlis Park"]

# Red Line
red_line = ["Rithala" ,"Rohini West" ,"Rohini East" ,"Pitampura" ,"Kohat Enclave" ,"Netaji Subhash Place" ,"Keshav Puram" ,"Kanhaiya Nagar" ,"Inderlok" ,"Shastri Nagar" ,"Pratap Nagar" ,"Pulbangash" ,"Tis Hazari" ,"Kashmere Gate" ,"Shastri Park" ,"Seelampur" ,"Welcome" ,"Shahdara" ,"Mansarovar Park" ,"Jhilmil" ,"Dilshad Garden" ]

# Magenta Line
magenta_line = ["Botanical Garden" ,"Okhla Bird Sanctuary" ,"Kalindi Kunj" ,"Jasola Vihar Shaheen Bagh" ,"Okhla Vihar" ,"Jamia Millia Islamia" ,"Sukhdev Vihar" ,"Okhla NSIC" ,"Kalkaji Mandir" ,"Nehru Enclave" ,"Greater Kailash" ,"Chirag Delhi" ,"Panchsheel Park" ,"Hauz Khas" ,"IIT" ,"R.K. Puram" ,"Munirka" ,"Vasant Vihar" ,"Shankar Vihar" ,"Terminal 1 IGI Airport" ,"Sadar Bazar" ,"Palam" ,"Dashrathpuri" ,"Dabri Mor- Janakpuri South" ,"Janakpuri West" ]

# Yellow Line
yellow_line = ["Shalimar Huda City Center" ,"IFFCO Chowk" ,"M G Road Metro station" ,"Sikanderpur Metro Station" ,"IndiGo Guru Dronacharya" ,"Arjan Garh" ,"Ghitorni" ,"Sultanpur" ,"Chhattarpur" ,"Qutab Minar" ,"Saket" ,"Malviya Nagar" ,"Hauz Khas" ,"Green Park" ,"AIIMS" ,"Ina" ,"Jorbagh" ,"Lok Kalyan Marg" ,"Udyog Bhawan" ,"Central Secretariat" ,"Patel Chowk" ,"Rajiv Chowk" ,"New Delhi Metro Station" ,"Chawri Bazar" ,"Chandni Chowk" ,"Kashmere Gate" ,"Civil Lines" ,"Vidhan Sabha" ,"Vishwavidyalaya" ,"GTB Nagar Metro Rail Station" ,"Model Town" ,"Azadpur" ,"Adarsh Nagar" ,"Jahangirpuri" ,"Haiderpur Badli Mor" ,"Rohini Sector 18" ,"Badli"]

# Blue Line 1
blue_line_1 = ["Dwarka Sector- 21" ,"Dwarka Sector 8" ,"Dwarka Sec 9" ,"PNB Dwarka Sector- 10" ,"Dwarka Sector- 11" ,"Dwarka Sector 12" ,"Dwarka Sector 13" ,"Dwarka Sector 14" ,"Dwarka" ,"Dwarka Mor" ,"Nawada" ,"Uttam Nagar West" ,"Uttam Nagar East" ,"Janakpuri West" ,"Janak Puri East" ,"Tilak Nagar" ,"Subhash Nagar" ,"Tagore Garden" ,"Rajouri Garden" ,"Ramesh Nagar" ,"Moti Nagar" ,"Kirti Nagar" ,"Shadipur" ,"Patel Nagar" ,"Rajendra Place" ,"Karol Bagh" ,"Jhandewalan" ,"Ramakrishna Ashram Marg" ,"Rajiv Chowk" ,"Barakhamba Road" ,"Mandi House" ,"Pragati Maidan" ,"Indraprastha" ,"Yamuna Bank" ,"Laxmi Nagar" ,"Nirman Vihar" ,"Preet Vihar" ,"Karkar Duma" ,"Anand Vihar ISBT" ,"Kaushambi" ,"Vaishali"]

# Blue Line 2

blue_line_2 = ["Dwarka Sector- 21" ,"Dwarka Sector 8" ,"Dwarka Sec 9" ,"PNB Dwarka Sector- 10" ,"Dwarka Sector- 11" ,"Dwarka Sector 12" ,"Dwarka Sector 13" ,"Dwarka Sector 14" ,"Dwarka" ,"Dwarka Mor" ,"Nawada" ,"Uttam Nagar West" ,"Uttam Nagar East" ,"Janakpuri West" ,"Janak Puri East" ,"Tilak Nagar" ,"Subhash Nagar" ,"Tagore Garden" ,"Rajouri Garden" ,"Ramesh Nagar" ,"Moti Nagar" ,"Kirti Nagar" ,"Shadipur" ,"Patel Nagar" ,"Rajendra Place" ,"Karol Bagh" ,"Jhandewalan" ,"Ramakrishna Ashram Marg" ,"Rajiv Chowk" ,"Barakhamba Road" ,"Mandi House" ,"Pragati Maidan" ,"Indraprastha" ,"Yamuna Bank","Akshardham" ,"Mayur Vihar-1" ,"Mayur Vihar Extension" ,"New Ashok Nagar" ,"Noida Sector- 15" ,"Noida Sec.16" ,"Noida Sec.-18" ,"Botanical Garden" ,"Golf Course" ,"Wave City Center Noida"]

# Airport Line
airport_metro = ["New Delhi Metro Station" ,"Shivaji Stadium Station" ,"Dhaula Kuan" ,"Delhi Aerocity" ,"I.G.I Airport" ,"Dwarka Sector- 21"]

# Rapid Metro
rapid_metro = ["Sector 55-56" ,"Sector 54 Chowk" ,"Sector 53-54" ,"Sector 42-43" ,"Phase- 1" ,"Sikanderpur Metro Station" ,"Phase- 2" ,"Vodafone Belvedere Tower" ,"IndusInd Bank Cyber City" ,"Micromax Moulsari Avenue" ,"Phase- 3"]

# Green Line 1
green_line_1 = ["Mundka" ,"Rajdhani Park" ,"Nangloi Railway Station" ,"Nangloi" ,"Maharaja Surajmal Stadium" ,"Udyog Nagar" ,"Peera Garhi" ,"Paschim Vihar West" ,"Paschim Vihar East" ,"Madipur" ,"Shivaji Park" ,"Punjabi Bagh" ,"Ashok Park Main" ,"Satguru Ram Singh Marg" ,"Kirti Nagar"]

# Green Line 2
green_line_2 = ["Mundka" ,"Rajdhani Park" ,"Nangloi Railway Station" ,"Nangloi" ,"Maharaja Surajmal Stadium" ,"Udyog Nagar" ,"Peera Garhi" ,"Paschim Vihar West" ,"Paschim Vihar East" ,"Madipur" ,"Shivaji Park" ,"Punjabi Bagh" ,"Ashok Park Main" ,"Inderlok"]

def metro_breakpoints(source, destination, line):
    print(line)
    current_metro_line = []
    if line == "Yellow Line":
        current_metro_line = yellow_line
    elif line == "Violet Line":
        current_metro_line = violet_line
    elif line == "Red Line":
        current_metro_line = red_line
    elif line == "Magenta Line":
        current_metro_line = magenta_line
    elif line == "Airport Line":
        current_metro_line = airport_metro
    elif line == "Rapid Metro":
        current_metro_line = rapid_metro
    elif line == "Blue Line":
        if source in blue_line_1 and destination in blue_line_1:
            current_metro_line = blue_line_1
        elif source in blue_line_2 and destination in blue_line_2:
            current_metro_line = blue_line_2
    elif line == "Green Line":
        if source in green_line_1 and destination in green_line_1:
            current_metro_line = green_line_1
        elif source in green_line_2 and destination in green_line_2:
            current_metro_line = green_line_2
    elif line == "Pink Line":
        if source in pink_line_1 and destination in pink_line_1:
            current_metro_line = pink_line_1
            print("ooo")
        elif source in pink_line_2 and destination in pink_line_2:
            current_metro_line = pink_line_2
            print("zdz")
    else:
        return -1
    print("curr")
    print(current_metro_line)
    start = current_metro_line.index(source)
    end = current_metro_line.index(destination)
    intermediate_stations = abs(end - start) - 1
    print("wecfacad",intermediate_stations)

    path = []
    itr = min(start,end) + 1
    high = max(start,end)
    while itr < high:
        path.append(current_metro_line[itr])
        itr += 1

    break_points = 0

    if intermediate_stations < 0:
        return -1
    elif 0 <= intermediate_stations < 10:
    	break_points = 0
    elif 10 <= intermediate_stations < 15:
        break_points = 1
    elif 15 <= intermediate_stations <= 20:
        break_points = 2
    else:
        break_points = 3

    if break_points == 0:
        indices = []
    elif break_points == 1:
        indices = [intermediate_stations // 2]
    elif break_points == 2:
        indices = [(intermediate_stations//4) + 1, (3*(intermediate_stations)//4)]
    else:
        indices = [((intermediate_stations//6) + 1), (intermediate_stations//2), (5*(intermediate_stations)//6)]

    stations = [path[i] for i in indices]
    intermediaries = [i+1 for i in indices]

    data_array = [[stations[i], intermediaries[i]] for i in range(len(indices))]

    return data_array

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
			return i


def geolocator(loc):
	print(loc)
	response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address='+loc+'&key=AIzaSyB9d8y-4zZB9_0ZOn6Pk3AjAWxlBd_J168')
	result = response.json()
	coor = []
	coor.append(result.get('results')[0].get('geometry').get('location').get('lat'))
	coor.append(result.get('results')[0].get('geometry').get('location').get('lng'))
	return coor

def func(source, destination):
	loc1 = source
	loc2 = destination
	coor1 = geolocator(source)
	coor2 = geolocator(destination)
	lat1 = coor1[0]
	lng1 = coor1[1]
	lat2 = coor2[0]
	lng2 = coor2[1]

	response = requests.get('https://maps.googleapis.com/maps/api/directions/json?origin='+loc1+'&destination=' + loc2 + '&mode=transit&alternatives=true&key=AIzaSyB9d8y-4zZB9_0ZOn6Pk3AjAWxlBd_J168')
	result = response.json()
	#print(result)
	lolresponse = requests.get('https://maps.googleapis.com/maps/api/directions/json?origin='+loc1+'&destination=' + loc2 + '&mode=driving&key=AIzaSyB9d8y-4zZB9_0ZOn6Pk3AjAWxlBd_J168')
	lolresult = lolresponse.json()
	overview_polyline = lolresult.get('routes')[0].get('overview_polyline').get('points')

	routes = result.get('routes')
	counter = 0
	Finalroutes = []
	Finalroutesmodes = []
	FinalPrice = [] 
	Finaltimes = []
	FinalInstructions = []
	Finaldistance = []
	Finalvary = []

	#sendiing all uber
	lolroutes = lolresult.get('routes')
	bb = []
	bb.append(overview_polyline)
	Finalroutes.append(bb)
	Finaldistance.append(lolroutes[0].get('legs')[0].get('distance').get('value'))
	Finaltimes.append(lolroutes[0].get('legs')[0].get('duration').get('value'))
	aa=[]
	aa.append("All from Uber")
	FinalInstructions.append(aa)
	alluber = getuberprice(lng1,lat1,lng2,lat2)
	FinalPrice.append(alluber.get('high_estimate'))
	tt = alluber.get('high_estimate') - alluber.get('low_estimate')
	Finalvary.append(tt)
	rr = []
	rr.append("Car")
	Finalroutesmodes.append(rr)


	for i in routes:
		#remove this line
		if counter!=0:
			break
		counter+=1
		Instruction = []
		Metro_Stations = []
		Bus_Stations = []
		Polyline = []
		Polylinemode = [] 
		leg = i.get('legs')[0]
		step = leg.get('steps')
		totaltime = leg.get('duration').get('value')
		totaldistance = leg.get('distance').get('value')
		time = 0
		distance = 0
		price = 0
		ctr=0
		for i in step :
		    ctr = ctr+1
		    # print(len(step))
		    # print(i.get('html_instructions'))
		    
		    poly = i.get('polyline')
		    Polyline.append(poly.get('points'))
		    text =  i.get('html_instructions')

		    if (text[:10].find("Bus") != -1):
		        Polylinemode.append("Bus")

		        time = time + i.get('duration').get('value')
		        distance = distance + i.get('distance').get('value')
		        if (i.get('distance').get('value') > 10000):
		        	price = price + 15
		        elif (i.get('distance').get('value') > 4000):
		        	price = price + 10
		        else:
		        	price = price + 5		
		        Transit_Details = i.get('transit_details')
		        Bus_Stations.append(Transit_Details.get('departure_stop').get('name'))
		        Bus_Stations.append(Transit_Details.get('arrival_stop').get('name'))
		        Instruction.append(i.get('html_instructions')+ " and " +  "stop at " + Transit_Details.get('arrival_stop').get('name'))
		        c1 = i.get('start_location')
		        c2 = i.get('end_location')
		        
		        uberfromhere = getuberprice(c2.get('lng'),c2.get('lat'),lng2,lat2)
		        price =  price + uberfromhere.get('high_estimate')
		        vary = uberfromhere.get('high_estimate') - uberfromhere.get('low_estimate')
		        Finalvary.append(vary)
		        newresponse = requests.get('https://maps.googleapis.com/maps/api/directions/json?origin='+ str(c2.get('lat')) + ','+ str(c2.get('lng'))+'&destination='+ str(lat2) + ','+str(lng2)  + '&mode=driving&key=AIzaSyB9d8y-4zZB9_0ZOn6Pk3AjAWxlBd_J168')
		        newresult = newresponse.json()
		        newoverview_polyline = newresult.get('routes')[0].get('overview_polyline').get('points')

		        deep_copy_Polyline = copy.deepcopy(Polyline)
		        deep_copy_Polyline.append(newoverview_polyline)
		        Finalroutes.append(deep_copy_Polyline)

		        deep_copy_Polylinemode = copy.deepcopy(Polylinemode)
		        deep_copy_Polylinemode.append("Car")
		        Finalroutesmodes.append(deep_copy_Polylinemode)

		        newtime = newresult.get('routes')[0].get('legs')[0].get('duration').get('value')
		        newdist = newresult.get('routes')[0].get('legs')[0].get('distance').get('value')
		        time = time + newtime
		        distance = distance + newdist
		        Finaltimes.append(time)
		        Finaldistance.append(distance)
		        FinalPrice.append(price)
		        
		        deep_copy_Instruction = copy.deepcopy(Instruction)
		        deep_copy_Instruction.append("Travel rest by uber")
		        FinalInstructions.append(deep_copy_Instruction)
		        
		        time = time - newtime
		        distance = distance - newdist
		        price = price -uberfromhere.get('high_estimate')

		    elif (text[:10].find("Walk") != -1):
		        Polylinemode.append("Walk")
		        Instruction.append(i.get('html_instructions')) 
		        time = time + i.get('duration').get('value')
		        distance = distance + i.get('distance').get('value')
		        if (ctr==len(step)):
		        	Finaltimes.append(time)
		        	Finaldistance.append(distance)
		        	FinalInstructions.append(Instruction)
		        	FinalPrice.append(price)
		        	Finalroutes.append(Polyline)
		        	Finalvary.append(0)
		        	Finalroutesmodes.append(Polylinemode)
		    elif (text[:10].find("Metro") != -1):
		        Polylinemode.append("Metro")
		        Transit_Details = i.get('transit_details')
		        Metro_Stations.append(Transit_Details.get('departure_stop').get('name'))
		        Metro_Stations.append(Transit_Details.get('arrival_stop').get('name'))

		        # //departure_stop + get_breakpoints + colorofline + nofofstations +++ newarrival_stop
		        # for all breakboints
		        # uber and append to the list
		        line = Transit_Details.get('line').get('name')
		        print(Transit_Details.get('departure_stop').get('name'), Transit_Details.get('arrival_stop').get('name'), line)
		        breakpoints = metro_breakpoints(Transit_Details.get('departure_stop').get('name'), Transit_Details.get('arrival_stop').get('name'), line)
		        print(breakpoints)
		        if (not (breakpoints ==None or breakpoints == -1)):
			        for breakpoint in breakpoints:
			        	name = breakpoint[0]
			        	no_stations = breakpoint[1]
			        	another_response = requests.get('https://maps.googleapis.com/maps/api/directions/json?origin='+ Transit_Details.get('departure_stop').get('name') +'&destination=' + name + '&mode=transit&alternatives=true&key=AIzaSyB9d8y-4zZB9_0ZOn6Pk3AjAWxlBd_J168')
			        	another_result = another_response.json()
			        	another_overview_polyline = another_result.get('routes')[0].get('overview_polyline').get('points')
			        	another_time = another_result.get('routes')[0].get('legs')[0].get('duration').get('value')
			        	another_dist = another_result.get('routes')[0].get('legs')[0].get('distance').get('value')

			        	copyinstruction = copy.deepcopy(Instruction)
			        	copyPolyline = copy.deepcopy(Polyline)
			        	copyPolylinemode = copy.deepcopy(Polylinemode)

			        	copyinstruction.append(i.get('html_instructions')+ " and " +  "stop at " + name)
			        	copyPolyline.append(another_overview_polyline)
			        	
			        	cc1 = Transit_Details.get('arrival_stop').get('location')
			        	another_uber = getuberprice(cc1.get('lng'),cc1.get('lat'),lng2,lat2)
			        	price =  price + another_uber.get('high_estimate')
			        	cvary = another_uber.get('high_estimate') - another_uber.get('low_estimate')
			        	Finalvary.append(cvary)
			        	cnewresponse = requests.get('https://maps.googleapis.com/maps/api/directions/json?origin='+ str(cc1.get('lat')) + ','+ str(cc1.get('lng'))+'&destination='+ str(lat2) + ','+str(lng2)  + '&mode=driving&key=AIzaSyB9d8y-4zZB9_0ZOn6Pk3AjAWxlBd_J168')
			        	cnewresult = cnewresponse.json()
			        	coverview_polyline = cnewresult.get('routes')[0].get('overview_polyline').get('points')
			        	copyPolyline.append(coverview_polyline)
			        	Finalroutes.append(copyPolyline)
			        	##check up
			        	copyPolylinemode.append("Car")
			        	Finalroutesmodes.append(copyPolylinemode)

			        	cnewtime = cnewresult.get('routes')[0].get('legs')[0].get('duration').get('value')
			        	cnewdist = cnewresult.get('routes')[0].get('legs')[0].get('distance').get('value')

			        	time = time + cnewtime
				        distance = distance + cnewdist
				        Finaltimes.append(time)
				        Finaldistance.append(distance)
				        FinalPrice.append(price)

				        copyinstruction.append("Travel rest by uber")
				        FinalInstructions.append(copyinstruction)

				        time = time - cnewtime
				        distance = distance - cnewdist
				        price =  price - another_uber.get('high_estimate')

		        ###########################################################################################################################################
		        time = time + i.get('duration').get('value')
		        distance = distance + i.get('distance').get('value')
		        if (i.get('distance').get('value') > 32000):
		        	price = price + 50
		        elif (i.get('distance').get('value') > 21000):
		        	price = price + 40
		        elif (i.get('distance').get('value') > 12000):
		        	price = price + 30
		        elif (i.get('distance').get('value') > 5000):
		        	price = price + 15
		        elif (i.get('distance').get('value') > 2000):
		        	price = price + 10			
		        else:
		        	price = price + 5
		        Instruction.append(i.get('html_instructions')+ " and " +  "stop at " + Transit_Details.get('arrival_stop').get('name'))
		        c1 = i.get('start_location')
		        c2 = i.get('end_location')
		        uberfromhere = getuberprice(c2.get('lng'),c2.get('lat'),lng2,lat2)
		        #print(uberfromhere)
		        price =  price + uberfromhere.get('high_estimate')
		        vary = uberfromhere.get('high_estimate') - uberfromhere.get('low_estimate')
		        Finalvary.append(vary)
		        newresponse = requests.get('https://maps.googleapis.com/maps/api/directions/json?origin='+ str(c2.get('lat')) + ','+ str(c2.get('lng'))+'&destination='+ str(lat2) + ','+str(lng2)  + '&mode=driving&key=AIzaSyB9d8y-4zZB9_0ZOn6Pk3AjAWxlBd_J168')
		        newresult = newresponse.json()
		        newoverview_polyline = newresult.get('routes')[0].get('overview_polyline').get('points')
		        deep_copy_Polyline = copy.deepcopy(Polyline)
		        deep_copy_Polyline.append(newoverview_polyline)
		        Finalroutes.append(deep_copy_Polyline)

		        deep_copy_Polylinemode = copy.deepcopy(Polylinemode)
		        deep_copy_Polylinemode.append("Car")
		        Finalroutesmodes.append(deep_copy_Polylinemode)

		        newtime = newresult.get('routes')[0].get('legs')[0].get('duration').get('value')
		        newdist = newresult.get('routes')[0].get('legs')[0].get('distance').get('value')
		        time = time + newtime
		        distance = distance + newdist
		        Finaltimes.append(time)
		        Finaldistance.append(distance)
		        FinalPrice.append(price)
		        
		        deep_copy_Instruction = copy.deepcopy(Instruction)
		        deep_copy_Instruction.append("Travel rest by uber ")
		        FinalInstructions.append(deep_copy_Instruction)
		        
		        time = time - newtime
		        distance = distance - newdist
		        price =  price - uberfromhere.get('high_estimate')
	#return ....
	print("lolo")
	print()
	print("Instructions : ")
	for i in FinalInstructions:
		for j in i:
			print(j)
		print("_________________________________")
		print()

	print()
	print("RoutesMode")
	for i in Finalroutesmodes:
		print(i)
	print()

	print("Vary : ")
	for i in Finalvary:
		print(i)
	print()

	print("Prices : ")
	for i in FinalPrice:
		print(i)
	print()

	print("time : ")		
	for i in Finaltimes:
		print(i)
	print()

	print("distances :")	

	for i in Finaldistance:
		print(i)
	print("========================================")
	print()


	for i in Finalroutes:
		for j in i:
			print(j)
			print("*******************************************************")
			print()
		print("-----------------------------------------")
		print()
 
func("IIITD BOYS HOSTEL", "Cariappa Vihar")