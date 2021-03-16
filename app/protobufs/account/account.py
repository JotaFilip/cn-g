from concurrent import futures
#from pymongo import MongoClient
from copy import copy
import random


import grpc
from grpc_interceptor import ExceptionToStatusInterceptor
from grpc_interceptor.exceptions import NotFound
import sqlite3
con = sqlite3.connect('Books', check_same_thread=False)
from account_b2 import (
    SpecificLikesAndViewsResponse,
    AllLikesAndViewsResponse,
    LikesAndViewsRequest,
)
import account_pb2_grpc

class AccountService(account_pb2_grpc.AccountServicer):
    def GetAllLikesAndViews(self, request, context):
        cur = con.cursor()
        cur.execute('SELECT book_id,book_title,genres,book_rating FROM book_data WHERE book_id=?', (request.book_id,))

        all_likes_and_views = cur.fetchone()
        print(all_likes_and_views)
        if all_likes_and_views is None:
            raise NotFound("User not found")
        books_likes_and_views = SpecificLikesAndViewsResponse(likes = all_likes_and_views[0][0],
                                                            views = all_likes_and_views[0][1])
        imdb_likes_and_views = SpecificLikesAndViewsResponse(likes = all_likes_and_views[1][0],
                                                            views = all_likes_and_views[1][1])
        animes_likes_and_views = SpecificLikesAndViewsResponse(likes = all_likes_and_views[2][0],
                                                            views = all_likes_and_views[2][1])

        return AllLikesAndViewsResponse(book_likes_views = books_likes_and_views,
                                        imdb_likes_views = imdb_likes_and_views,
                                        anime_likes_views = animes_likes_and_views)
        
    def GetBookLikesAndViews(self, request, context):
    
        cur = con.cursor()
        cur.execute('SELECT book_id,book_title,genres,book_rating FROM book_data WHERE book_title = ? ', ( request.name,))

        specific_likes_and_views = cur.fetchone()
        print(specific_likes_and_views)
        if specific_likes_and_views is None:
            raise NotFound("User not found")
        return SpecificLikesAndViewsResponse(likes = specific_likes_and_views[0],
                                                            views = specific_likes_and_views[1])

    def GetBookLikesAndViews(self, request, context):
    
        cur = con.cursor()
        cur.execute('SELECT book_id,book_title,genres,book_rating FROM book_data WHERE book_title = ? ', ( request.name,))

        specific_likes_and_views = cur.fetchone()
        print(specific_likes_and_views)
        if specific_likes_and_views is None:
            raise NotFound("User not found")
        return SpecificLikesAndViewsResponse(likes = specific_likes_and_views[0],
                                                            views = specific_likes_and_views[1])
        
    def GetBookLikesAndViews(self, request, context):
    
        cur = con.cursor()
        cur.execute('SELECT book_id,book_title,genres,book_rating FROM book_data WHERE book_title = ? ', ( request.name,))

        specific_likes_and_views = cur.fetchone()
        print(specific_likes_and_views)
        if specific_likes_and_views is None:
            raise NotFound("User not found")
        return SpecificLikesAndViewsResponse(likes = specific_likes_and_views[0],
                                                            views = specific_likes_and_views[1])
        


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
