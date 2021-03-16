from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint

# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
user = "seen"
password = "ifFvApoasv9lLvqR"
up = user + ":" + password

client = MongoClient("mongodb+srv://"+up+"@books.lnpq3.mongodb.net/Books?retryWrites=true&w=majority")
db = client["database"]
db = db["books"]

# Issue the serverStatus command and print the results
# serverStatusResult=db.command("serverStatus")
# pprint(serverStatusResult)

# open file to parse it
import csv

with open("cn-g/app/databases/data/GoodReads/book_data.csv","r",encoding="utf8") as f:
    reader = csv.reader(f)

    first_elem = True
    for row in reader:
        genres = row[10].split("|")

        if first_elem:
            first_elem = False
            continue

        book = {
            'name' : row[9],
            'description': row[1],
            'category': genres,
            'rating' : row[6],
            'imageURL' : row[11]
        }

        # insert
        result = db.insert_one(book)
        print(".",end="")

    print('Done')