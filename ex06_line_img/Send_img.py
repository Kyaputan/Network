import requests
import urllib.parse
import sys
from loadex06 import load_env_ex06

LINE_ACCESS_TOKEN = load_env_ex06()

print("LINE_ACCESS_TOKEN:", LINE_ACCESS_TOKEN)

url = "https://notify-api.line.me/api/notify"
file = {'imageFile':open('CodeCit\Lab5-Network\ex06_line_img\img_test.jpeg','rb')}
data = ({
        'message':'Test Image'
    })
LINE_HEADERS = {"Authorization":"Bearer "+LINE_ACCESS_TOKEN}
session = requests.Session()
r=session.post(url, headers=LINE_HEADERS, files=file, data=data)
print(r.text)