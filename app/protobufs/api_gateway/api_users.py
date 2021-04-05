
# Users API
import os

from app.protobufs.account.account_pb2 import *
from signin_pb2 import *

from signin_pb2_grpc import SignInStub
from account_pb2 import *
import grpc
from grpc_interceptor import ExceptionToStatusInterceptor
#
from verifier import Verifier
from flask import Flask, jsonify, request, url_for, abort, g
from flask_httpauth import HTTPBasicAuth
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
auth = HTTPBasicAuth()
sign_host = os.getenv("SIGNIN_HOST", "localhost")
sign_channel = grpc.insecure_channel(f"{sign_host}:50056")
signin_client = SignInStub(sign_channel)

#@auth.verify_password
def verify_password(username_or_token, password, required_scopes=None):
    #Try to see if it's a token first
    user_id = Verifier.verify_auth_token(username_or_token)
    if not user_id: #significa que o token é invalido
        #user = session.query(User).filter_by(username = username_or_token).first()
        #if not user or not user.verify_password(password):
        request = VerificarRequest(username = username_or_token, password=password)
        response = signin_client.VerificarPassword(request)
        if not response.success:
            return None
        user_id = response.id

    g.user_id = user_id
    #token = g.user.generate_auth_token()
    return {'sub': user_id, 'valid': True}
    #if token:
    #    responseObject = {
    #        'status': 'success',
    #        'message': 'Successfully logged in.',
    #        'auth_token': token.decode()
    #    }
    #    return jsonify(responseObject), 200
#@auth.login_required
def loginUser():

    token = Verifier.generate_auth_token(g.user_id)
    #token = g.user.generate_auth_token()
    #
    return jsonify({'token': token.decode('ascii')})

#


def createUser(body):
    request =EmailRequest (
        email = body["email"],
        username = body["username"]
    )
    return signin_client.CreateUser(request).success
def givePassword(body):
    request = PasswordRequest (
        username = body["username"],
        password = body["password"],
        nonce=body["nonce"]
    )
    return signin_client.UserPassword(request).success



def logoutUser():
    return "Logged Out"

def getUserByName(username):
    request = GetUserRequest (
        name = username
    )
    return signin_client.GetUserByName(request)

def updateUser(username,body):
    request = UpdateUserRequest (
        username = username,
        new_username = body.username,
        new_password = body.password
    )
    return signin_client.UpdateUser(request)

def deleteUser(username):
    request = DeleteUserRequest (
        username = username
    )
    return signin_client.DeleteUser(request)