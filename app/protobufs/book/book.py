from concurrent import futures
import grpc
from grpc_interceptor import ExceptionToStatusInterceptor
from utils_pb2 import *
from grpc_interceptor.exceptions import NotFound
from pymongo import MongoClient
from bson.objectid import ObjectId



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
    BooksByCategoryRequest
)
import book_pb2_grpc

class BookService(book_pb2_grpc.BookServicer):

    def GetBooks(self, request, context):
        page = request.page * request.max_results
        results = list(db.find().skip(page).limit(request.max_results))
        results = [ book_to_proto(book) for book in results ]
        return BookDataList( books = results )

    def SearchById(self, request, context):
        results = list(db.find({ "_id": ObjectId(request.book_id) }).limit(1))

        if len(results) <= 0:
            return BookData()
        return book_to_proto(results[0])
        

    def SearchByName(self, request, context):
        results = list(db.find({ "name": request.name}).limit(request.max_results))
        results = [ book_to_proto(book) for book in results ]
        return BookDataList( books = results )

    def SearchByCategory(self, request, context):
        results = list(db.find({ "category": { "$all": [request.category] } }).limit(request.max_results))
        results = [ book_to_proto(book) for book in results ]
        return BookDataList( books = results )

    def AddBook(self, request, context):
        db.insert_one(proto_to_book(request))
        return Success(success=True)

    def RemoveBook(self, request, context):
        db.remove(ObjectId(request.book_id))
        return Success(success=True)

def book_to_proto(result):
    book = BookData (
        book_id = str(result["_id"]),
        book_title = result["name"],
        description = result["description"],
        book_rating = result["rating"],
        img_url = result["imageURL"]
    )
    book.genres.extend(result["category"])
    return book

def proto_to_book(proto):
    book = {
        'name': proto.book_title,
        'description': proto.description,
        'category': [c for c in proto.genres],
        'rating': proto.book_rating,
        'imageURL': proto.img_url
    }
    return book


def serve():
    interceptors = [ExceptionToStatusInterceptor()]
    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=10), interceptors=interceptors
    )
    book_pb2_grpc.add_BookServicer_to_server(
        BookService(), server
    )
    
    with open("book.key", "rb") as fp:
        book_key = fp.read()
    with open("book.pem", "rb") as fp:
        book_cert = fp.read()
    with open("ca.pem", "rb") as fp:
        ca_cert = fp.read()
    
    creds = grpc.ssl_server_credentials(
        [(book_key, book_cert)],
        root_certificates=ca_cert,
        require_client_auth=True,
    )
    
    server.add_secure_port("[::]:50051", creds)
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()