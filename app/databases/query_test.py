from pymongo import MongoClient
from bson.objectid import ObjectId

# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
user = "seen"
password = "ifFvApoasv9lLvqR"
up = user + ":" + password

db = MongoClient("mongodb+srv://"+up+"@animes.4nkye.mongodb.net/Animes?retryWrites=true&w=majority")
db = db["database"]
db = db["animes"]

result = db.find({ "_id": ObjectId("605128692d0accf2d480f2c2") }).limit(1)
print(result[0])