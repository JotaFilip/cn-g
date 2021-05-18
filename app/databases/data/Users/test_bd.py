import sqlalchemy
from sqlalchemy import func, distinct
from sqlalchemy.exc import IntegrityError

from models import Base, User, Seen, Like, Contagem
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
#

SQLALCHEMY_DATABASE_URI = sqlalchemy.engine.url.URL.create(
    drivername="mysql+mysqlconnector",
    username="cngroupfcul",
    password="178267316238hsugdhgaabhdsauisduiasiud89812989021709120783bjjkhaklnskdj",
    host="34.90.227.81",
    port=3306,
    database="account",
    query={"ssl_ca": "server-ca.pem", 'ssl_cert': 'client-cert.pem', 'ssl_key': 'client-key.pem'},

)

def GetLikesItem(request):
        engine = create_engine(SQLALCHEMY_DATABASE_URI)

        Base.metadata.bind = engine
        DBSession = sessionmaker(bind=engine)
        session = DBSession()
        counts = session.query(Like).filter_by(item_id=request.id, item_type=request.type).count()
        session.commit()
        return counts

def GetSeensItem(request):
    engine = create_engine(SQLALCHEMY_DATABASE_URI)

    Base.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    counts = session.query(Seen).filter_by(item_id=request.id, item_type=request.type).count()
    session.commit()
    return counts

def GetTopTen(request):
    engine = create_engine(SQLALCHEMY_DATABASE_URI)
    Base.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    count_ = func.count(distinct(Like.user_id))
    likes = session.query(Like.item_type, Like.item_id, count_.label('likes')) \
                    .filter_by(item_type=request.type) \
                    .group_by(Like.item_type, Like.item_id) \
                    .order_by('likes') \
                    .limit(10) \
                    .all()

    session.commit()
    # rs = [ (r.item_id,r.item_type) for r in likes ]
    return likes

from typing import NamedTuple
class GetLikes(NamedTuple):
    id:str   = "606e25ad5e927a606f53428b"
    type:int = 0

class GetViews(NamedTuple):
    id:str   = "606e25ad5e927a606f53428b"
    type:int = 0

class GetTop(NamedTuple):
    type:int = 0

print(GetLikesItem(GetLikes()))
print(GetSeensItem(GetViews()))
rs = GetTopTen(GetTop())
[ print(r) for r in rs ]