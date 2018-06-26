import pdb
import requests
import json
import datetime
import time

print "What is your Hue IP?"
hue_ip = raw_input()
print "What is your Hue user name?"
hue_user = raw_input()



def hue(brightness):
    url = "http://%s/api/%s/groups/0/action" % (hue_ip, hue_user)
    body = dict()
    body['on'] = True
    body['hue'] = 54346
    body['sat'] = 25
    body['bri'] = brightness
    body = json.dumps(body)
    # pdb.set_trace()
    response = requests.put(url, data=body)



latitude = "37.367931"
longitude = "-121.914402"   
url = "https://api.sunrise-sunset.org/json?lat=%s&lng=%s&formatted=0" % (latitude, longitude)

# url = "http://10.0.0.200/api/0DgsyolfyHyIvFzWDtLp4Sj4yeEvLFdhQ2VtISzj/lights"


# This code will send a GET request and store its response into response variable as a response data type
response = requests.get(url)

# This code will convert unicode (string) of response.text value to dictionary and overwrite response variable 
response = json.loads(response.text)

# This code will access sunset key in nested dictionary and stored into new variables
twilight_start = response['results']['sunset'] 
twilight_end = response['results']['astronomical_twilight_end']
twilight_start = datetime.datetime.strptime(twilight_start[:-6], "%Y-%m-%dT%H:%M:%S")
twilight_end = datetime.datetime.strptime(twilight_end[:-6], "%Y-%m-%dT%H:%M:%S")
twilight_duration = (twilight_end - twilight_start).seconds
pdt_twilight_start = twilight_start - datetime.timedelta(hours=7)

# pdb.set_trace()

while (pdt_twilight_start - datetime.datetime.today()).seconds > 1:
	print (pdt_twilight_start - datetime.datetime.today()).seconds
	continue


for brightness in range(1, 256):
	hue(brightness)
	time.sleep(twilight_duration / 255)

# print response["1"]["name"]
# print response["2"]["config"]["function"]
# print response["9"]["capabilities"]["control"]["colorgamut"][1][1]




