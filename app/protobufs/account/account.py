from models import Base, User
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
#
engine = create_engine('sqlite:///usersWithTokens.db')

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()
#
import sys
import secrets
from concurrent import futures

import grpc
from grpc_interceptor import ExceptionToStatusInterceptor
from grpc_interceptor.exceptions import NotFound

from account_pb2 import *
import account_pb2_grpc

import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
smtp_server = "smtp.gmail.com"
port = 587  # For starttls
sender_email = "cngroupfcul@gmail.com"
password = "@GrupoComputacaomovel2021"
class AccountService(account_pb2_grpc.AccountServicer):
    def GetAllLikesAndViews(self, request, context):
        return GetUser(request.username)
        
    def GetBookLikesAndViews(self, request, context):
        return GetUser(request.username).books

    def GetIMDBLikesAndViews(self, request, context):
        return GetUser(request.username).imdbs
        
    def GetAnimeLikesAndViews(self, request, context):
        return GetUser(request.username).animes
    def VerificarPassword(self, request, context):

        # user = session.query(User).filter_by(username = username_or_token).first()
        # if not user or not user.verify_password(password):
        return None
    # SIGN IN
    def CreateUser(self, request, context):
        
        email = request.email
        username = request.username
        nonce = secrets.randbelow(1000000)

        if username is None or email is None:
            Success(success = False) #argumentos insuficientes
        if session.query(User).filter_by(username=username).first() or session.query(User).filter_by(email=email).first() is not None:
            #user = session.query(User).filter_by(username=username).first()
            Success(success = False) #Já existe
        user = User(username=username, email=email, nonce=nonce)
        #user.hash_password(password)
        session.add(user)
        session.commit()

        s = smtplib.SMTP(smtp_server,port)
        s.starttls()
        s.login(sender_email,password)

        msg = MIMEMultipart()
        message = "Dear {}, send your (password; nonce) on the register rest_api\nnonce = {}".format(username,str(nonce))
        msg['From'] = sender_email
        msg['To'] = email
        msg['Subject'] = "Seen nonce register"

        msg.attach(MIMEText(message,'plain'))

        s.send_message(msg)
        del msg
        return Success(success = True)

    def UserPassword(self, request, context):

        username = request.username
        password = request.password
        nonce = request.nonce
        user = session.query(User).filter_by(username=username).first()
        if user is None:
            Success(success = False)
        if not user.verify_nonce(nonce):
            Success(success = False)

        salt = secrets.randbelow(sys.maxsize)
        user.hash_password(password, str(salt))
        session.commit()

        return Success(success = True)
    def LoginUser(self, request, context):
        return None

    def LogoutUser(self, request, context):
        return None

    def GetUserByName(self, request, context):
        return None

    def UpdateUser(self, request, context):
        return None

    def DeleteUser(self, request, context):
        return None

def GetUser(self, username):
    # TODO
    # results = list(db.find({ "username": username}).limit(1))
    results = []

    if len(results) <= 0:
        raise NotFound("Id not found")
    return all_lists_to_proto(results[0])

def all_lists_to_proto(user):
    return LikesAndViewsResponse(
        books = list_to_proto(user,"books"),
        imdbs = list_to_proto(user,"imdbs"),
        animes = list_to_proto(user,"animes")
    )

def list_to_proto(user,type):
    return LikesAndViewsRequest(
        likes = user[type+"_likes"],
        views = user[type+"_views"],
    )

def serve():
    interceptors = [ExceptionToStatusInterceptor()]
    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=10), interceptors=interceptors
    )
    account_pb2_grpc.add_AccountServicer_to_server(
        AccountService(), server
    )
    
    server.add_insecure_port("[::]:50055")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()