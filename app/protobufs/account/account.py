from concurrent import futures

import grpc
from grpc_interceptor import ExceptionToStatusInterceptor
from grpc_interceptor.exceptions import NotFound

from pymongo import MongoClient

# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
user = "seen"
password = "ifFvApoasv9lLvqR"
up = user + ":" + password

client = MongoClient("mongodb+srv://"+up+"@seen.2xwmp.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client["database"]
db = db["users"]

from account_pb2 import (
    AllLikesAndViewsResponse,
    LikesAndViewsRequest,
)
import account_pb2_grpc

class AccountService(account_pb2_grpc.AccountServicer):
    def GetAllLikesAndViews(self, request, context):
        return GetUser(request.username)
        
    def GetBookLikesAndViews(self, request, context):
        return GetUser(request.username).books

    def GetIMDBLikesAndViews(self, request, context):
        return GetUser(request.username).imdbs
        
    def GetAnimeLikesAndViews(self, request, context):
        return GetUser(request.username).animes

    def GetUser(self, username):
        results = list(db.find({ "username": user_id}).limit(1))

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