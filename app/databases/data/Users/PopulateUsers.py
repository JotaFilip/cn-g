import sqlalchemy
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

from models import Base, User, Seen, Like, Contagem

from sqlalchemy import insert

SQLALCHEMY_DATABASE_URI = sqlalchemy.engine.url.URL.create(
    drivername="mysql+mysqlconnector",
    username="cngroupfcul",
    password="178267316238hsugdhgaabhdsauisduiasiud89812989021709120783bjjkhaklnskdj",
    host="34.90.227.81",
    port=3306,
    database="account",
    query={"ssl_ca": "server-ca.pem"},
)
engine = create_engine(SQLALCHEMY_DATABASE_URI)

# Users -> id:String | username:String | email:String
new_users_ids = []
new_users     = []
for i in range(2000):
    username = "User_" +str(i)
    email    = "email_"+str(i)+"@email.com"
    new_users.append(
        User(
            username=username, 
            email=email
        )
    )
    new_users_ids.append(username)

DBSession = sessionmaker(bind=engine)
session = DBSession()
session.add_all(new_users)
session.commit()

exit()
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

likes = []
views = []
for (d,t) in databases:
    ls = list(d.find().limit(10))
    ls = [ (l['_id'],t) for l in ls ]
    likes += ls

    vs = list(d.find().limit(10))
    vs = [ (v['_id'],t) for v in vs ]
    views += vs

# Users -> id:String | username:String | email:String
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
    i %= len(new_likes)

new_views = []
i = 0
for (view,tp) in views:
    new_views.append(
        View(
            user_id = new_users_ids[i], 
            item_id = view,
            item_type = tp,
        )
    )
    i += 1
    i %= len(new_users_ids)

DBSession = sessionmaker(bind=engine)
session = DBSession()
session.add_all(new_views)
session.add_all(new_likes)
session.commit()