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
        self.req_content = self.req_response.content
        self.all_info = self.req_response.json()
        self.starship_list = []
        self.pilot_url_list = []
        self.pilot_name_list = []

    def info(self):
        return self.req_content

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


    def pilot_name(self):
        # iterate through pilot url list to get pilot name
        for i in self.pilot_url_list:
            if self.pilot_url_list[i]:
                url = f"{self.pilot_url_list[i]}"
                info = requests.get(url).json()
                for each in info:
                    self.pilot_name_list.append(each)
                return self.pilot_name_list

    def query_name(self):
        # Take the list of pilot names
        # Iterate through the pilot names
        # For each iteration, use a mongodb query
        # iterate for a in self.pilot_name_list
        # variable = db.characters.find({name:"a"}, {_id:1})
        # append to a list that has the object
        return

    def replace_url(self):
        # iterate through the name of each starship list
        #
        return





test = Starship()
print(test.pilot_name())


# for every starship list of pilots
# make a request for those pilot to grab name
# change list of url to name
# query mongodb character collection based on name
# grab objectid
# essentially change list of names into objectids
