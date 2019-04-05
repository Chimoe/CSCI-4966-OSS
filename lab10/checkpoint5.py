from pymongo import MongoClient
import datetime

client = MongoClient('localhost', 27017)


def random_word_requester():
    db = client.mongo_db_lab.definitions
    for definition in db.aggregate([{"$sample": {"size": 1}}]):
        id = definition["_id"]
        db.update({"_id": id}, {"$push": {"timestamp": datetime.datetime.now()}})
        for definition in db.find({"_id": id}):
            print definition
    return


if __name__ == '__main__':
    print random_word_requester()
