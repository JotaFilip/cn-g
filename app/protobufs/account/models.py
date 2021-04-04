from sqlalchemy import Column,Integer,String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
from passlib.apps import custom_app_context as pwd_context
import random, string
from itsdangerous import(TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired)

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

    def hash_password(self, password, salt):
        self.password_hash = pwd_context.encrypt(password + salt)
        self.password_salt = salt

    def verify_password(self, password):

        return pwd_context.verify(password + self.password_salt, self.password_hash)

    def verify_nonce(self, nonce):
        return self.nonce == nonce

    def getId(self):
        return self.id




engine = create_engine('sqlite:///usersWithTokens.db')

Base.metadata.create_all(engine)
