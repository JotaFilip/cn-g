from sqlalchemy import Column,Integer,String,Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
from passlib.apps import custom_app_context as pwd_context
import random, string
Base = declarative_base()
secret_key = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(32))


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String(32), index=True)
    email = Column(String, index=True)
    nonce = Column(Integer)
    password_hash = Column(String(64))
    password_salt = Column(String(64))
    admin = Column(Boolean, default=False)

    def hash_password(self, password, salt):
        self.password_hash = pwd_context.encrypt(password + salt)
        self.password_salt = salt

    def verify_password(self, password):

        return pwd_context.verify(password + self.password_salt, self.password_hash)

    def verify_nonce(self, nonce):
        return self.password_hash is None and self.nonce == nonce

    def getId(self):
        return self.id

class Seen(Base):
    __tablename__ = 'seen'

    user_id = Column(Integer, primary_key=True)
    item_type = Column(Integer, primary_key=True)
    item_id = Column(String, primary_key=True)

class Like(Base):
    __tablename__ = 'like'

    user_id = Column(Integer, primary_key=True)
    item_type = Column(Integer, primary_key=True)
    item_id = Column(String, primary_key=True)

class Contagem(Base):
    __tablename__ = 'contagem'

    user_id = Column(Integer, primary_key=True)
    category = Column(String, primary_key=True)
    likes = Column(Integer, default=0)
    views = Column(Integer, default=0)
    def incrementSeens(self):
        self.views += 1
    def incrementLikes(self):
        self.likes += 1




engine = create_engine('sqlite:///usersWithTokens.db')

Base.metadata.create_all(engine)
