import pymongo
client = pymongo.MongoClient()
db = client['starwars']

# If we just specify find, we dip our cursor into the database
# If we use find_one, we can draw one document from the database
# luke = db.characters.find_one({"name": "Luke Skywalker"})
# print(luke)

# Lets print droid names
# droids = db.characters.find({"species.name": "Droid"})
# for droid in droids:
#     print(droid["name"])

# .insertOne() -- .insert_one()
# .updateMany() -- .update_many()

# Exercises
#
# Find the height of Darth Vader, only return results for the name and the height
# Find all characters with yellow eyes, only return results for the names of the characters
# Find male characters. Limit your results to only show the first 3
# Find the name of all the humans whose homeworld is Alderaan

# Find the height of Darth Vader, only return results for the name and the height
# darth = db.characters.find_one({"name": "Darth Vader"}, {"name":1, "height":1})
# print(darth)

# Find all characters with yellow eyes, only return results for the names of the characters
# yellow = db.characters.find({"eye_color": "yellow"}, {"name":1, "_id":0})
# for char in yellow:
#     print(char)

# Find male characters. Limit your results to only show the first 3
# male = db.characters.find({"gender": "male"}, {"name":1, "_id":0}).limit(3)
# for i in male:
#     print(i)

# Find the name of all the humans whose homeworld is Alderaan
# people = db.characters.find({"$and": [{"homeworld.name": "Alderaan"}, {"species.name": "Human"}]}, {"name":1, "_id":0)
# for i in people:
#     print(i)

# Find the average female height
# avg_female_height = db.characters.aggregate([{"$match":{"gender":"female"}},
#                                              {"$group":{"_id":"$gender", "avg_height":{"$avg":"$height"}}}])
# print(avg_female_height.next())
#
#
# When we use an aggregate, similar to find, will return cursor object
# this output will just be one object
# the .next() will go through our cursor object and grab the next thing
# If we have multiple, we need to use a for loop

