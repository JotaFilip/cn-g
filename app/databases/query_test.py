from pymongo import MongoClient
from bson.objectid import ObjectId

# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
user = "seen"
password = "ifFvApoasv9lLvqR"
up = user + ":" + password

client = MongoClient("mongodb+srv://"+up+"@movies.oysuj.mongodb.net/Movies?retryWrites=true&w=majority")
db = client["database"]
db = db["movies"]

result = int(db.estimated_document_count())
print(result)