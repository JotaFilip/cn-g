import sqlalchemy
from sqlalchemy import Column,Integer,String,Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    user_id = Column(String(256), primary_key=True)
    username = Column(String(128), index=True)

    def getId(self):
        return self.user_id

class Seen(Base):
    __tablename__ = 'seen'

    user_id = Column(String(256), primary_key=True)
    item_type = Column(Integer, primary_key=True)
    item_id = Column(String(128), primary_key=True)

class Like(Base):
    __tablename__ = 'like'

    user_id = Column(String(256), primary_key=True)
    item_type = Column(Integer, primary_key=True)
    item_id = Column(String(128), primary_key=True)

class Contagem(Base):
    __tablename__ = 'contagem'

    user_id = Column(String(256), primary_key=True)
    category = Column(String(128), primary_key=True)
    likes = Column(Integer, default=0)
    views = Column(Integer, default=0)
    def incrementSeens(self):
        self.views += 1
    def incrementLikes(self):
        self.likes += 1

SQLALCHEMY_DATABASE_URI = sqlalchemy.engine.url.URL.create(
    drivername="mysql+mysqlconnector",
    username="cngroupfcul",
    password="178267316238hsugdhgaabhdsauisduiasiud89812989021709120783bjjkhaklnskdj",
    host="34.90.227.81",
    port=3306,
    database="account",
    query={"ssl_ca": "./server-ca.pem", 'ssl_cert': './client-cert.pem', 'ssl_key': './client-key.pem'},
)

#engine = create_engine('mysql+pymysql://cngroupfcul:178267316238hsugdhgaabhdsauisduiasiud89812989021709120783bjjkhaklnskdj@127.0.0.1/account')
engine = create_engine(SQLALCHEMY_DATABASE_URI)
#SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://cngroupfcul:178267316238hsugdhgaabhdsauisduiasiud89812989021709120783bjjkhaklnskdj@192.168.1.250:3306/account'
#engine = create_engine(SQLALCHEMY_DATABASE_URI)

Base.metadata.create_all(engine)
