
# Users API
import os
from signin_pb2 import *
from signin_pb2_grpc import SignInStub
import grpc
from grpc_interceptor import ExceptionToStatusInterceptor
#
from models import Base, User
from flask import Flask, jsonify, request, url_for, abort, g
from flask_httpauth import HTTPBasicAuth
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
auth = HTTPBasicAuth()
engine = create_engine('sqlite:///usersWithTokens.db')

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

@auth.verify_password
def verify_password(username_or_token, password):
    #Try to see if it's a token first
    user_id = User.verify_auth_token(username_or_token)
    if user_id:
        user = session.query(User).filter_by(id = user_id).one()
    else:
        user = session.query(User).filter_by(username = username_or_token).first()
        if not user or not user.verify_password(password):
            return False
    g.user = user
    return True
@auth.login_required
def loginUser():
    token = g.user.generate_auth_token()
    return jsonify({'token': token.decode('ascii')})
#
sign_host = os.getenv("SIGNIN_HOST", "localhost")
sign_channel = grpc.insecure_channel(f"{sign_host}:50055")
sign_client = SignInStub(sign_channel)

def createUser(body):
    request = CreateUserRequest (
        username = body.username,
        password = body.password 
    )
    return sign_client.CreateUser(request)



def logoutUser():
    return sign_client.LogoutUser()

def getUserByName(username):
    request = GetUserRequest (
        name = username
    )
    return sign_client.GetUserByName(request)

def updateUser(username,body):
    request = UpdateUserRequest (
        username = username,
        new_username = body.username,
        new_password = body.password
    )
    return sign_client.UpdateUser(request)

def deleteUser(username):
    request = DeleteUserRequest (
        username = username
    )
    return sign_client.DeleteUser(request)