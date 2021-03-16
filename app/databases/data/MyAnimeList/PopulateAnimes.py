from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint

# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
user = "seen"
password = "ifFvApoasv9lLvqR"
up = user + ":" + password

client = MongoClient("mongodb+srv://"+up+"@animes.4nkye.mongodb.net/Animes?retryWrites=true&w=majority")
db = client["database"]

# drop everything in there
db.drop_collection("animes")

db = db["animes"]

# Issue the serverStatus command and print the results
# serverStatusResult=db.command("serverStatus")
# pprint(serverStatusResult)

# open file to parse it
import csv

# title_english,      2
# image_url,          5
# score,              14
# genre,              27

insert_list = []
with open("cn-g/app/databases/data/MyAnimeList/AnimeList.csv","r",encoding="utf8") as f:
    reader = csv.reader(f)

    first_elem = True
    for row in reader:
        genres = row[28].split(",")
        genres = [ g.strip() for g in genres ]

        if first_elem:
            first_elem = False
            continue

        anime = {
            'name' : row[2],
            'category': genres,
            'rating' : float(row[15]),
            'imageURL' : row[5]
        }

        insert_list.append(anime)

        # insert
        if len(insert_list) >= 100_000:
            result = db.insert_many(insert_list)
            insert_list = []

# insert rest
if len(insert_list) > 0:
    result = db.insert_many(insert_list)
    insert_list = []

print('Done')