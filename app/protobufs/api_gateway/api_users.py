
# Users API
import os
from signin_pb2 import *
from signin_pb2_grpc import SignInStub

sign_host = os.getenv("SIGNIN_HOST", "localhost")
sign_channel = grpc.insecure_channel(f"{sign_host}:50055")
sign_client = SignInStub(sign_channel)

def createUser(body):
    request = CreateUserRequest (
        username = body.username,
        password = body.password 
    )
    return sign_client.CreateUser(request)

def loginUser(username,password):
    request = LoginRequest (
        username = username,
        password = password
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