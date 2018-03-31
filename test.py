import requests
headers = {"X-App-Token":"Q2ll9CnTdOoSiA8Krr6pOhcno"}

r = requests.get('https://data.cityofchicago.org/resource/8v9j-bter.json',headers=headers)
print(r.json())
