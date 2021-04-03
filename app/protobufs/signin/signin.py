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
from concurrent import futures
from pymongo import MongoClient

import grpc
import secrets
from grpc_interceptor import ExceptionToStatusInterceptor
from grpc_interceptor.exceptions import NotFound

from signin_pb2 import *
from utils_pb2 import *
import signin_pb2_grpc

from account_pb2 import AllLikesAndViewsResponse, LikesAndViewsResponse, LikesAndViewsRequest
from account_pb2_grpc import AccountStub



def saveNonceAndEmail(receiver_email, username, nonce):
    pass

import smtplib, ssl

smtp_server = "smtp.gmail.com"
port = 587  # For starttls
sender_email = "cngroupfcul@gmail.com"
password = "@GrupoComputacaomovel2021"

class SignInService(signin_pb2_grpc.SignInServicer):

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

        message = """\
        Subject: Hi there

        Send your (password; nonce) on the register rest_api 
        nonce = """ + str(nonce)
        context = ssl.create_default_context()
        with smtplib.SMTP(smtp_server, port) as mserver:
            mserver.ehlo()  # Can be omitted
            mserver.starttls(context=context)
            mserver.ehlo()  # Can be omitted
            mserver.login(sender_email, password)
            mserver.sendmail(sender_email, email, message)
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





def serve():
    interceptors = [ExceptionToStatusInterceptor()]
    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=10), interceptors=interceptors
    )
    signin_pb2_grpc.add_SignInServicer_to_server(
        SignInService(), server
    )
    
    server.add_insecure_port("[::]:50056")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
