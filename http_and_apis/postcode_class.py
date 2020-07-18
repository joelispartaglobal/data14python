import requests
import json

class Postcode:

    def __init__(self):
        self.dict_body = {'postcodes': ["B7 4BB"]}
        self.json_body = json.dumps(self.dict_body)
        self. headers = {'Content-Type': 'application/json'}
        self.address = "https://api.postcodes.io/postcodes/"
        self.req_response = requests.post(self.address, headers=self.headers, data=self.json_body)

    # Create a method to print the results from the json folder
    def result(self):
        return self.req_response.json()['result']

    # Create a method to print the details relating to the post code
    def post_details(self):
        for postcode in self.req_response.json()['result']:
            result = postcode['result']
            print(f"Postcode: {result['postcode']}; Eastings: {result['eastings']};\ Northings: {result['northings']}; NUTS code: {result['codes']['nuts']}")


if __name__ == "__main__":
    test = Postcode()
    print(test.post_details())
# You dont always have to assign a variable to a method
# You can create the instance of the object but you are not storing it
# You are defining something then dropping it
# If you dont know how many variables there are going to be
# But you want to create an object out of all of them
# You can make an iterative method
# One thing in python is that it cannot dynamically assign variables
# we could create a dictionary instead
# 