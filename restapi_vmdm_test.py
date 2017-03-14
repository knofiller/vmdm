import requests
from requests.packages.urllib3.exceptions import *
requests.packages.urllib3.disable_warnings()

headers = {
	'Accept': 'application/json',
	'Content-Type': 'application/json'
}

payload = {
	'username': 'admin',
	'password': 'admin',
	'tenant': 'qaLandlord'
}

url = 'https://10.25.80.114:8443/api/v1/login'

r = requests.post(url, headers=headers, data=payload, verify=False)

print(r.headers)