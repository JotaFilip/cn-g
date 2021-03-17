from concurrent import futures

import grpc
from grpc_interceptor import ExceptionToStatusInterceptor
from grpc_interceptor.exceptions import NotFound

from pymongo import MongoClient
from bson.objectid import ObjectId

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

     def GetIMDB(self, request, context):
        page = request.page * request.max_results
        results = list(db.find().skip(page).limit(request.max_results))
        results = [ imdb_to_proto(imdb) for imdb in results ]
        return IMDBDataList( imdbs = results )
        
    def SearchById(self, request, context):
        results = list(db.find({ "_id": ObjectId(request.imdb_id) }).limit(1))

        if len(results) <= 0:
            raise NotFound("Id not found")
        return IMDB( imdb = imdb_to_proto(results[0]))

    def SearchByName(self, request, context):
        results = list(db.find({ "name": request.name}).limit(request.max_results))
        results = [ imdb_to_proto(imdb) for imdb in results ]
        return IMDBDataList( imdbs = results )

    def SearchByCategory(self, request, context):
        results = list(db.find({ "category": { "$all": [request.category] } }).limit(request.max_results))
        results = [ imdb_to_proto(imdb) for imdb in results ]
        return IMDBDataList( imdbs = results )

def imdb_to_proto(result):
    imdb = IMDBData (
        imdb_id = str(result["_id"]),
        imdb_title = result["name"],
        genres = result["category"],
        imdb_rating = result["rating"],
        img_url = result["imageURL"],
        type = result["type"],
    )
    imdb.genres.extends(result["category"])
    return imdb

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
