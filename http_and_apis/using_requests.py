import requests
import json
from pprint import pprint

# address = "https://api.postcodes.io/postcodes/PR8 6TL"
# req_response = requests.get(address)

# print(req_response)
# print(type(req_response))
# print(req_response.status_code)
# pprint(req_response.content)
# The class are bytes which is a type of raw data
# pprint(type(req_response.content))

# pprint(req_response.json())
#
# result = req_response.json()['result']
# # Print from dictionary using this format
#
# print(f"Eastings: {result['eastings']}; Northings: {result['northings']}")
# print(f"NUTS CODE: {result['codes']['nuts']}")

dict_body = {'postcodes': ["B7 4BB", "OX49 5NU", "M32 0JG", "NE30 1DP"]}
json_body = json.dumps(dict_body)
headers = {'Content-Type': 'application/json'}

address = "https://api.postcodes.io/postcodes/"
req_response = requests.post(address, headers=headers, data=json_body)

# pprint(req_response.json()['result'])

# Print the postcode, eastings, northings and NUTS code for each result
#
result = req_response.json()['result']
# print(result)

for postcode in req_response.json()['result']:
    result = postcode['result']
    print(f"Postcode: {result['postcode']}; Eastings: {result['eastings']};\
Northings: {result['northings']}; NUTS code: {result['codes']['nuts']}")

# Start to think about how we might want to construct a class
# Think about how you want those statuses to behave
# Test room development
