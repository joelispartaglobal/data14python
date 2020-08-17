import pymongo
import json
import requests
import sys

# for every starship list of pilots
# make a request for those pilot to grab name
# change list of url to name
# query mongodb character collection based on name
# grab objectid
# essentially change list of names into objectids


api = "http://swapi.dev/api/starships/?page="
starship_list = []
pilot_url_list = []
pilot_name_list = []
pilot_object_list = []

def get_starship():
    # iterate through all pages to get the starship data
    for i in range(1, 5):
        url = f"{api}{i}"
        info = requests.get(url).json()
        for each in info['results']:
            starship_list.append(each)
        print(starship_list)

def load_pilots():
    # Save all the pilot urls to a list
    for i in range(1, 5):
        url = f"{api}{i}"
        info = requests.get(url).json()
        for each in info['results']:
            pilot_url_list.append((each['pilots']))
        print(pilot_url_list)

def pilot_name():
    for link in pilot_url_list:
        if link in pilot_url_list:
            url = link
            info = requests.get(url).json()
            for each in info:
                pilot_name_list.append((each['name']))
            print(pilot_name_list)

def pilot_object():
    # Loop through each pilot name
    # for variable in pilot_name_list
    # variable = db.characters.find({name:"a"}, {_id:1})
    # append to pilot_object_list
    return

def join_object_pilot():
    # append pilot_url_list and pilot_object_list together
    return

def replace_url():
    # in starship_list replace the links in the pilot
    # with the objects
    return

def create_db():
    # client = pymongo.MongoClient()
    # db = client['starwars']
    # create a new collection starship
    return

def import_json():
    # with open() as f:
    #   file_data = json.load(f)
    # read dictionary into new collection
    # db.starship.insert_many(file_data)
    return

load_pilots()
pilot_name()

# after dealing with one starship document, insert one