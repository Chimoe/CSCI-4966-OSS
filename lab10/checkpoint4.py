from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient('localhost', 27017)

if __name__ == '__main__':
    db = client["mongo_db_lab"]
    collection = db['definitions']
    for x in collection.find():
        print(x)
    print(collection.find_one())
    print('----------------------')
    print(collection.find_one({"word": "Blech"}))
    print('----------------------')
    print(collection.find_one({"_id": ObjectId("56fe9e22bad6b23cde07b8c6")}))
    print('----------------------')
    collection.insert_one({"word": "MUR"})
