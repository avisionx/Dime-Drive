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

ans = getuberprice(77.2732,28.5456,77.1628,28.5956)
print(ans.get('high_estimate'))


# Uber Codes
#qMOnL1l20oAwreTtKAPuXhuFmWCTIJXe0tXZkjVe
#APuykJdS83wzrNLDuRa13hIXci-DZ-VK7454kH_S
#mHUzAGLUDv9Fp1j-H1O3nVIx02gtDtL7NGpWJqz5
#JA2aaRKKIsdXNSOG0ZtRzedVUegdQYsnrZ9pPvWE