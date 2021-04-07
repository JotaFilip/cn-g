from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint

# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
user = "seen"
password = "ifFvApoasv9lLvqR"
up = user + ":" + password

client = MongoClient("mongodb+srv://"+up+"@books.lnpq3.mongodb.net/Books?retryWrites=true&w=majority")
db = client["database"]

# drop everything in there
db.drop_collection("books")

db = db["books"]

# Issue the serverStatus command and print the results
# serverStatusResult=db.command("serverStatus")
# pprint(serverStatusResult)

# open file to parse it
import csv

insert_list = []
with open("app/databases/data/GoodReads/book_data.csv","r",encoding="utf8") as f:
    reader = csv.reader(f)

    first_elem = True
    for row in reader:
        genres = row[10].split("|")
        genres = [ g.strip() for g in genres ]

        if first_elem:
            first_elem = False
            continue

        book = {
            'name' : row[9].strip(),
            'description': row[1].strip(),
            'category': genres,
            'rating' : float(row[6])*2,
            'imageURL' : row[11].strip()
        }

        # append 
        insert_list.append(book)

        # insert
        if len(insert_list) >= 100_000:
            result = db.insert_many(insert_list)
            insert_list = []

# insert rest
if len(insert_list) > 0:
    result = db.insert_many(insert_list)
    insert_list = []

print('Done')