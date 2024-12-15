import requests
from loadex01 import load_env_ex01

token = load_env_ex01()
url = 'https://notify-api.line.me/api/notify'
headers = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+token}

msg = "1234"
r = requests.post(url, headers=headers, data = {'message':msg})
print (r.text)