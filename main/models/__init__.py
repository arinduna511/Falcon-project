import pymongo
from mongoengine import *

client = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = client["mydatabase"]

mycol = mydb["timestamp"]


# d = {'name': "Archana", 'address': "Singh Sadan"}
# x = mycol.insert_one(d)
# print(x.inserted_id)


class TimeStamp(Document):

    timestamp = DateTimeField()
    value = IntField()


connect(mydb)
