from concurrent import futures
from pymongo import MongoClient

import grpc
from grpc_interceptor import ExceptionToStatusInterceptor
from grpc_interceptor.exceptions import NotFound

from signin_pb2 import (
    UserData,
    Success,
    Empty,
    UserDataRequest,
    UserRequest,
    UpdateUserRequest
)
import signin_pb2_grpc

from account_pb2 import AnimeData, AnimeByIdRequest, AnimeByNameRequest, AnimeByCategoryRequest
from account_pb2_grpc import AccountStub

class SignInService(signin_pb2_grpc.SignInServicer):

    def CreateUser(self, request, context):
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
    book_pb2_grpc.add_BookServicer_to_server(
        BookService(), server
    )
    
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
