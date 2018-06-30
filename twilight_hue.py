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
    response = requests.put(url, data=body)


def get_location_by_ip():
    url = "http://ip-api.com/json"
    response = requests.get(url)
    response = json.loads(response.text)
    return response["lat"], response["lon"]

  
url = "https://api.sunrise-sunset.org/json?lat=%s&lng=%s&formatted=0" % (get_location_by_ip())


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


while (pdt_twilight_start - datetime.datetime.today()).seconds > 1:
	print (pdt_twilight_start - datetime.datetime.today()).seconds
	continue


for brightness in range(1, 256):
	hue(brightness)
	time.sleep(twilight_duration / 255)

