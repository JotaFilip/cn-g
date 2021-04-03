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
    password_hash = Column(String(64))
    password_salt = Column(String(64))

    def hash_password(self, password, salt):
        self.password_hash = pwd_context.encrypt(password + salt)
        self.password_salt = salt

    def verify_password(self, password, salt):
        return pwd_context.verify(password + salt, self.password_hash + self.password_salt)

    def generate_auth_token(self, expiration=600):
        s = Serializer(secret_key, expires_in=expiration)
        return s.dumps({'id': self.id})

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(secret_key)
        try:
            data = s.loads(token)
        except SignatureExpired:
            # Valid Token, but expired
            return None
        except BadSignature:
            # Invalid Token
            return None
        user_id = data['id']
        return user_id


engine = create_engine('sqlite:///usersWithTokens.db')

Base.metadata.create_all(engine)
