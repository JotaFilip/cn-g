
# Users API

from account_pb2 import *
from account_pb2_grpc import AccountStub

acc_host = os.getenv("ACCOUNTS_HOST", "localhost")
acc_channel = grpc.insecure_channel(f"{acc_host}:50054")
acc_client = AccountStub(acc_channel)

def createUser(body):
    request = CreateUserRequest (
        username = body.username,
        password = body.password 
    )
    return acc_client.CreateUser(request)

def loginUser(username,password):
    request = LoginRequest (
        username = username,
        password = password
    )
    return acc_client.CreateUser(request)

def logoutUser():
    return acc_client.LogoutUser()

def getUserByName(username):
    request = GetUserRequest (
        name = username
    )
    return acc_client.GetUserByName(request)

def updateUser(username,body):
    request = UpdateUserRequest (
        username = username,
        new_username = body.username,
        new_password = body.password
    )
    return acc_client.UpdateUser(request)

def deleteUser(username):
    request = DeleteUserRequest (
        username = username
    )
    return acc_client.DeleteUser(request)