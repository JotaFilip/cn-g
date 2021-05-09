import sqlalchemy
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

from models import Base, User, Seen, Like

from sqlalchemy import insert

import random

SQLALCHEMY_DATABASE_URI = sqlalchemy.engine.url.URL.create(
    drivername="mysql+mysqlconnector",
    username="cngroupfcul",
    password="178267316238hsugdhgaabhdsauisduiasiud89812989021709120783bjjkhaklnskdj",
    host="34.90.227.81",
    port=3306,
    database="account",
    query={"ssl_ca": "server-ca.pem", 'ssl_cert': 'client-cert.pem', 'ssl_key': 'client-key.pem'},
)
engine = create_engine(SQLALCHEMY_DATABASE_URI)
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

print("Creating Users",end=" \t")
new_users_ids = [ str(i) for i in range(1,2001) ]
new_users     = []
for i in new_users_ids:
    username = "User_" +str(i)
    new_users.append(
        User(
            user_id = i,
            username = username, 
        )
    )
print("done")

print("Populating Users",end=" \t")
DBSession = sessionmaker(bind=engine)
session = DBSession()
session.add_all(new_users)
session.commit()
print("done")

from pymongo import MongoClient

driver = "mongodb+srv://" 
user = "seen"
password = "ifFvApoasv9lLvqR"
up = driver + user + ":" + password

books = MongoClient(up+"@books.lnpq3.mongodb.net/Books?retryWrites=true&w=majority")
books = books["database"]
books = books["books"]

imdb1 = MongoClient(up+"@movies.oysuj.mongodb.net/Movies?retryWrites=true&w=majority")
imdb1 = imdb1["database"]
imdb1 = imdb1["movies"]

imdb2 = MongoClient(up+"@movies-2.nlmxu.mongodb.net/movies?retryWrites=true&w=majority")
imdb2 = imdb2["database"]
imdb2 = imdb2["movies"]

animes = MongoClient(up+"@animes.4nkye.mongodb.net/Animes?retryWrites=true&w=majority")
animes = animes["database"]
animes = animes["animes"]

databases = [(books,0),(imdb1,1),(imdb2,1),(animes,3)]

print("Fetching Items",end=" \t")
likes = []
views = []
for (d,t) in databases:
    ls = list(d.find().limit(10))
    ls = [ (str(l['_id']),t) for l in ls ]
    likes += ls

    vs = list(d.find().limit(10))
    vs = [ (str(v['_id']),t) for v in vs ]
    views += vs
print("done")

# Users -> id:String | username:String | email:String
print("Creating Likes",end=" \t")
new_likes = []
i = 0
for (like,tp) in likes:
    new_likes.append(
        Like(
            user_id = new_users_ids[i], 
            item_id = like,
            item_type = tp,
        )
    )
    i += 1
    i %= len(new_users_ids)
print("done")

print("Creating Views",end=" \t")
new_views = []
i = 0
for (view,tp) in views:
    new_views.append(
        Seen(
            user_id = new_users_ids[i], 
            item_id = view,
            item_type = tp,
        )
    )
    i += 1
    i %= len(new_users_ids)
print("done")

print("Populating Likes and Views",end=" \t")
DBSession = sessionmaker(bind=engine)
session = DBSession()
session.add_all(new_likes)
session.add_all(new_views)
session.commit()
print("done")