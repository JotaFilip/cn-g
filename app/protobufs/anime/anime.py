from concurrent import futures

import grpc
from utils_pb2 import *
from grpc_interceptor import ExceptionToStatusInterceptor
from grpc_interceptor.exceptions import NotFound

from pymongo import MongoClient
from bson.objectid import ObjectId

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
    AddAnimeResponse
)
import anime_pb2_grpc

class AnimeService(anime_pb2_grpc.AnimeServicer):

    def GetAnimes(self, request, context):
        page = request.page * request.max_results
        results = list(db.find().skip(page).limit(request.max_results))
        results = [ anime_to_proto(anime) for anime in results ]
        return AnimeDataList(animes = results)

    def SearchById(self, request, context):
        try:
            results = list(db.find({ "_id": ObjectId(request.anime_id)}).limit(1))

            if len(results) <= 0:
               return AnimeData()
            return anime_to_proto(results[0])
        except:
            return AnimeData()

    def SearchByName(self, request, context):
        results = list(db.find({ "name": request.name}).limit(request.max_results))
        results = [ anime_to_proto(anime) for anime in results ]
        return AnimeDataList( animes = results )

    def SearchByCategory(self, request, context):
        results = list(db.find({ "category": { "$all": [request.category] } }).limit(request.max_results))
        results = [ anime_to_proto(anime) for anime in results ]
        return AnimeDataList(animes=results)

    def AddAnime(self, request, context):
        id = db.insert_one(proto_to_anime(request)).inserted_id
        return AddAnimeResponse(anime_id=str(id))

    def RemoveAnime(self, request, context):
        try:
            db.delete_one({"_id": ObjectId(request.anime_id)})
            return Success(success=True)
        except:
            return Success(success=False)


def anime_to_proto(result):
    anime = AnimeData (
        anime_id = str(result["_id"]),
        anime_title = result["name"],
        anime_rating = result["rating"],
        img_url = result["imageURL"]
    )
    anime.genres.extend(result["category"])
    return anime

def proto_to_anime(proto):
    anime = {
            'name' : proto.anime_title,
            'category': [c for c in proto.genres],
            'rating' : proto.anime_rating,
            'imageURL' : proto.img_url
    }
    
    return anime

def serve():
    interceptors = [ExceptionToStatusInterceptor()]
    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=10), interceptors=interceptors
    )
    anime_pb2_grpc.add_AnimeServicer_to_server(
        AnimeService(), server
    )

    # with open("anime.key", "rb") as fp:
        # anime_key = fp.read()
    # with open("anime.pem", "rb") as fp:
        # anime_cert = fp.read()
    # with open("ca.pem", "rb") as fp:
        # ca_cert = fp.read()

    # creds = grpc.ssl_server_credentials(
        # [(anime_key, anime_cert)],
        # root_certificates=ca_cert,
        # require_client_auth=True,
    # )

    # server.add_secure_port("[::]:50053", creds)
    server.add_insecure_port("[::]:50053")
    server.start()
    server.wait_for_termination()



if __name__ == "__main__":
    serve()
