from models import Base, User
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
#
engine = create_engine('sqlite:///users.db')

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

from signin_pb2 import (
    UserData,
    UserDataRequest,
    UserRequest,
    UpdateUserRequest
)
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
        
        receiver_email = request.email
        username = request.username
        nonce = secrets.randbelow(sys.maxsize)

        message = """\
        Subject: Hi there

        Send your (password; nonce) on the register rest_api 
        nonce = """ + nonce
        saveNonceAndEmail(receiver_email,username)
        context = ssl.create_default_context()
        with smtplib.SMTP(smtp_server, port) as server:
            server.ehlo()  # Can be omitted
            server.starttls(context=context)
            server.ehlo()  # Can be omitted
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
        return None

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
    
    server.add_insecure_port("[::]:50054")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
