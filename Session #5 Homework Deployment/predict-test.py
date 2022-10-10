
import requests


url = 'http://localhost:5000/predict'

client_id = 'xyz-123'
client = {"reports": 0, "share": 0.245, "expenditure": 3.438, "owner": "yes"}

response = requests.post(url, json=client).json()
print(response)

if response['card'] == True:
    print('sending promo email to %s' % client_id)
else:
    print('not sending promo email to %s' % client_id)