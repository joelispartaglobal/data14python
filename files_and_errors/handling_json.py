import json
from pprint import pprint

# with open("film.json", "r") as jsonfile:
#     film = json.load(jsonfile)
#
# pprint(film)

# pprint or pretty print orders things alphabetically
#
# film = {
#     "name": "The Godfather",
#     "length": 178,
#     "release_year": 1972,
#     "cast": {
#         "Marlon Brando": "Vito",
#         "Al Pachino": "Michael"
#     }
# }
#
# print(film)
# print(json.dumps(film))
# with open ("godfather.json", "w") as jsonfile:
#     json.dump(film, jsonfile)


# define a class
# store same attributes as defined in your json
# read your json file
# create an instance of your film class
# for your film
#

class JsonReader:

    def __init__(self, film_json):
        # Load in json file
        with open(film_json, "r") as jsonfile:
            film_dict = json.load(jsonfile)
        # reference the keys in json file
        self.name = film_dict['film_name']
        self.year = film_dict['year']
        self.studio = film_dict['studio']

lion = JsonReader("film.json")
print(lion.name, lion.year, lion.studio)



