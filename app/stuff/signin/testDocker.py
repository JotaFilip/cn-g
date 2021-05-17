
import os
import grpc
from signin_pb2 import *
from account_pb2 import *
from signin_pb2_grpc import SignInStub

signin_host = os.getenv("signinS_HOST", "localhost")
signin_channel = grpc.insecure_channel(f"{signin_host}:50055")
signin_client = SignInStub(signin_channel)

request = UserRequest(username= "admin")
response = signin_client.GetUserByName(request)

print(response)