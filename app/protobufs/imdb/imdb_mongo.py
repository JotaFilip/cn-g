from concurrent import futures

import grpc
from grpc_interceptor import ExceptionToStatusInterceptor
from grpc_interceptor.exceptions import NotFound
import sqlite3
import random

# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
user = "seen"
password = "ifFvApoasv9lLvqR"
up = user + ":" + password

client = MongoClient("mongodb+srv://"+up+"@movies.oysuj.mongodb.net/Movies?retryWrites=true&w=majority")
db = client["database"]
db = db["movies"]

from imdb_pb2 import (
    IMDBData,
    IMDBDataList,
    IMDBByIdRequest,
    IMDBByNameRequest,
    IMDBByCategoryRequest, 
    IMDBData,
    IMDBResponse
)

import imdb_pb2_grpc

class IMDBService(imdb_pb2_grpc.IMDBServicer):
    def SearchById(self, request, context):
        results = db.find({ "_id": request.imdb_id}).limit(1)

        if len(results) <= 0:
            raise NotFound("Id not found")
        return imdb_to_proto(results[0])

    def SearchByName(self, request, context):
        results = db.find({ "name": request.name}).limit(request.max_results)
        return [ imdb_to_proto(imdb) for imdb in results ]

    def SearchByCategory(self, request, context):
        results = db.find({ "category": { "$all": request.category } }).limit(request.max_results)
        return [ imdb_to_proto(imdb) for imdb in results ]

def imdb_to_proto(imdb):
    return IMDBData (
        imdb_id = result["_id"],
        imdb_title = result["name"],
        genres = result["category"],
        imdb_rating = result["rating"],
        img_url = result["imageURL"],
        type = result["type"],
    )


def serve():
    interceptors = [ExceptionToStatusInterceptor()]
    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=10), interceptors=interceptors
    )
    imdb_pb2_grpc.add_IMDBServicer_to_server(
        IMDBService(), server
    )
    
    server.add_insecure_port("[::]:50052")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
