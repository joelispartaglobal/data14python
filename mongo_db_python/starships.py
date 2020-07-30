import pymongo
import json
import requests
import sys
client = pymongo.MongoClient()
db = client['starwars']

class Starship:
    # Fetch the star wars api starships
    def __init__(self):
        self.api = "http://swapi.dev/api/starships/?page="
        self.api_page = []
        self.req_response = requests.get(self.api)
        self.all_info = self.req_response.json()
        self.starship_list = []
        self.pilot_url_list = []
        self.pilot_name = []

    def load_starship(self):
        # Save starships to a list
        for i in range(1, 5):
            url = f"{self.api}{i}"
            info = requests.get(url).json()
            for each in info['results']:
                self.starship_list.append(each)

    def load_pilots(self):
        # Save pilot url to list
        for i in range(1, 5):
            url = f"{self.api}{i}"
            info = requests.get(url).json()
            for each in info['results']:
                self.pilot_url_list.append((each['pilots']))
            return self.pilot_url_list

    def pilot_name(self):
        # iterate through pilot url list to get pilot name
        for i in self.pilot_url_list:
            if i in self.pilot_url_list:
                url = f"{self.pilot_url_list[i]}"
                info = requests.get(url).json()
                for each in info:
                    self.pilot_name.append(each["name"])
                return self.pilot_name


    def query_name(self):
        # Take the list of pilot names
        # Iterate through the pilot names
        # For each iteration, use a mongodb query

        return


test = Starship()
print(test.pilot_name)


# for every starship list of pilots
# make a request for those pilot to grab name
# change list of url to name
# query mongodb character collection based on name
# grab objectid
# essentially change list of names into objectids
