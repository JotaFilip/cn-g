from pymongo import MongoClient

# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
user = "seen"
password = "ifFvApoasv9lLvqR"
up = user + ":" + password

db = MongoClient("mongodb+srv://"+up+"@animes.4nkye.mongodb.net/Animes?retryWrites=true&w=majority")
db = db["database"]
db = db["animes"]

array = ["Drama","Music"]
result = db.find({ "category": { "$all": array } }).limit(10)
print(result[0]["_id"])