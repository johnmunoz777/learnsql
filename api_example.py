import requests

endpoint = 'https://api.exchangerate-api.com/v4/latest/usd'

# Make a GET request to the API endpoint
response = requests.get(endpoint)
print(type(response))
response_json = response.json()
print(response_json)
print(type(response_json))
for key in response_dict:
    print(key, ":", response_dict[key])
    
currencies = ['EGP', 'GMD', 'CLP']
base_url = "https://api.exchangerate-api.com/v4/latest/"

for currency_code in currencies:
    url = base_url + currency_code
    response = requests.get(url)
    response = response.json()
    print(response['rates']['USD'])