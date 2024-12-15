import requests
from pprint import pprint
import json
from datetime import datetime
from loadex04 import load_env_ex04

token = load_env_ex04()
headers = {
    'accept': "application/json",
    'authorization': f"Bearer {token}"
}


url = "https://data.tmd.go.th/nwpapi/v1/forecast/location/hourly/place"


querystring = {"province":u"ชุมพร", "amphoe":u"", "tambon" : u"",
               "fields":"tc,rh,cond", 
               "date":datetime.now().strftime("%Y-%m-%d"), 
               "hour":"5", 
               "duration":"24"}


response = requests.request("GET", url, headers=headers, params=querystring)



if response.status_code == 200:
    data = response.json()
    import json 
    json_output = (json.dumps(json.loads(response.text), sort_keys=False, indent=4, separators=(" , ", " : ")))
    print(json_output)
else:
    print(f"respone Error{response}")

