from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint

# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
user = "seen"
password = "ifFvApoasv9lLvqR"
up = user + ":" + password

client = MongoClient("mongodb+srv://"+up+"@movies.oysuj.mongodb.net/Movies?retryWrites=true&w=majority")
db = client["database"]

# drop everything in there
db.drop_collection("movies")

db = db["movies"]

# Issue the serverStatus command and print the results
# serverStatusResult=db.command("serverStatus")
# pprint(serverStatusResult)

# open file to parse it
import csv

ratings = {}
# load ratings
with open("cn-g/app/databases/data/IMDB/title.ratings.tsv","r",encoding="utf8") as f:
    reader = csv.reader(f,delimiter="\t")

    first_elem = True
    for row in reader:

        if first_elem:
            first_elem = False
            continue

        ratings[row[0]] = float(row[1])
print("Loaded ratings")

insert_list = []
count = 0
total = 6_300_000
with open("cn-g/app/databases/data/IMDB/title.basics.tsv","r",encoding="utf8") as f:
    reader = csv.reader(f,delimiter="\t")

    first_elem = True
    for row in reader:

        if count >= 3_300_000:
            break

        if first_elem:
            first_elem = False
            continue

        genres = []

        if len(row) >= 9:
            genres = row[8].split(",")

        rating = "-"
        if row[0] in ratings:
            rating = ratings[row[0]]

        movie = {
            # 'id': row[0],
            'name' : row[2],
            'category': genres,
            'rating' : rating,
            # 'imageURL' : "",
            'type': row[1],
        }

        # append
        insert_list.append(movie)

        # insert
        if len(insert_list) >= 100_000:

            result = db.insert_many(insert_list)
            insert_list = []

            count += 100_000
            print(str(count * 100 // total) + "%")

if insert_list != []:
    result = db.insert_many(insert_list)
    insert_list = []

print('Done')