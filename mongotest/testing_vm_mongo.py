import pymongo
client = pymongo.MongoClient("54.93.34.44:27017")
db = client.sparta

for item in db.test.find({}):
    print(item)