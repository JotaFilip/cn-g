from pymongo import MongoClient
from bson.objectid import ObjectId

# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
user = "seen"
password = "ifFvApoasv9lLvqR"
up = user + ":" + password

db = MongoClient("mongodb+srv://"+up+"@books.lnpq3.mongodb.net/Books?retryWrites=true&w=majority")
db = db["database"]
db = db["books"]

results = db.find({ "category": "Fiction" }).limit(1)
for r in results:
    print(r)