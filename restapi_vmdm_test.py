import requests
from requests.packages.urllib3.exceptions import *
requests.packages.urllib3.disable_warnings()
import json

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

r = requests.post(url, headers=headers, data=json.dumps(payload), verify=False)

print(r.status_code)
print(r.content)

res = json.loads(r.content)

headers['X-Auth-Token'] = res['x-auth-token']

url = 'https://10.25.80.114:8443/api/v1/historicalDiscoveryMetrics'

r = requests.get(url,headers=headers, verify=False)

print(r.status_code)
print(r.content)