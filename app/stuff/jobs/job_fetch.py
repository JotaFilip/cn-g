import sqlalchemy
from sqlalchemy import Column,Integer,String,Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

class ImportData:
    Base = declarative_base()
    def __init__(self):
        self.SQLALCHEMY_DATABASE_URI = sqlalchemy.engine.url.URL.create(
            drivername="mysql+mysqlconnector",
            username="cngroupfcul",
            password="178267316238hsugdhgaabhdsauisduiasiud89812989021709120783bjjkhaklnskdj",
            host="34.90.227.81",
            port=3306,
            database="account",
            query={"ssl_ca": "server-ca.pem", 'ssl_cert': 'client-cert.pem', 'ssl_key': 'client-key.pem'},
        )

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

    def create_session(self):
        engine = create_engine(self.SQLALCHEMY_DATABASE_URI)
        self.Base.metadata.bind = engine
        DBSession = sessionmaker(bind=engine)
        session = DBSession()
        return session

    def import_views(self):
        session = self.create_session()
        views = session.query(self.Seen).all()
        return views

    def import_likes(self):
        session = self.create_session()
        likes = session.query(self.Like).all()
        return likes