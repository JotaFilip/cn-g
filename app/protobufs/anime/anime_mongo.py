from concurrent import futures

import grpc
from grpc_interceptor import ExceptionToStatusInterceptor
from grpc_interceptor.exceptions import NotFound

from pymongo import MongoClient

# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
user = "seen"
password = "ifFvApoasv9lLvqR"
up = user + ":" + password

db = MongoClient("mongodb+srv://"+up+"@animes.4nkye.mongodb.net/Animes?retryWrites=true&w=majority")
db = db["database"]
db = db["animes"]

from anime_pb2 import (
    AnimeData,
    AnimeDataList,
    AnimeByIdRequest,
    AnimeByNameRequest,
    AnimeByCategoryRequest,
    AnimeResponse
)

import anime_pb2_grpc

class AnimeService(anime_pb2_grpc.AnimeServicer):
    def SearchById(self, request, context):
        results = db.find({ "_id": request.anime_id}).limit(1)

        if len(results) <= 0:
            raise NotFound("Id not found")
        return anime_to_proto(results[0])

    def SearchByName(self, request, context):
        results = db.find({ "name": request.name}).limit(request.max_results)
        return [ anime_to_proto(anime) for anime in results ]

    def SearchByCategory(self, request, context):
        results = db.find({ "category": { "$all": request.category } }).limit(request.max_results)
        return [ anime_to_proto(anime) for anime in results ]

def anime_to_proto(result):
    return AnimeData (
        anime_id = result["_id"],
        anime_title = result["name"],
        genres = result["category"],
        anime_rating = result["rating"],
        img_url = result["imageURL"]
    )

def serve():
    interceptors = [ExceptionToStatusInterceptor()]
    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=10), interceptors=interceptors
    )
    anime_pb2_grpc.add_AnimeServicer_to_server(
        AnimeService(), server
    )
    
    server.add_insecure_port("[::]:50053")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
