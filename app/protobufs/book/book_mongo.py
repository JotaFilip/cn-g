from concurrent import futures

import grpc
from grpc_interceptor import ExceptionToStatusInterceptor
from grpc_interceptor.exceptions import NotFound

from pymongo import MongoClient

# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
user = "seen"
password = "ifFvApoasv9lLvqR"
up = user + ":" + password

db = MongoClient("mongodb+srv://"+up+"@books.lnpq3.mongodb.net/Books?retryWrites=true&w=majority")
db = db["database"]
db = db["books"]

from book_pb2 import (
    BookData,
    BookDataList,
    BookByIdRequest,
    BooksByNameRequest,
    BooksByCategoryRequest, BookResponse,

)
import book_pb2_grpc

class BookService(book_pb2_grpc.BookServicer):
    def SearchById(self, request, context):
        results = db.find({ "_id": request.anime_id}).limit(1)

        if len(results) <= 0:
            raise NotFound("Id not found")
        return book_to_proto(results[0])

    def SearchByName(self, request, context):
        results = db.find({ "name": request.name}).limit(request.max_results)
        return [ book_to_proto(anime) for anime in results ]

    def SearchByCategory(self, request, context):
        results = db.find({ "category": { "$all": request.category } }).limit(request.max_results)
        return [ book_to_proto(anime) for anime in results ]

def book_to_proto(book):
    return BookData (
        book_id = result["_id"],
        book_title = result["name"],
        description = result["description"],
        genres = result["category"],
        book_rating = result["rating"],
        img_url = result["imageURL"]
    )

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