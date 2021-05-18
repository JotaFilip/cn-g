from concurrent import futures

import grpc
from grpc_interceptor import ExceptionToStatusInterceptor
from grpc_interceptor.exceptions import NotFound
from utils_pb2 import *

from pymongo import MongoClient
from bson.objectid import ObjectId

# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
user = "seen"
password = "ifFvApoasv9lLvqR"
up = user + ":" + password

db1 = MongoClient("mongodb+srv://"+up+"@movies.oysuj.mongodb.net/Movies?retryWrites=true&w=majority")
db1 = db1["database"]
db1 = db1["movies"]

db2 = MongoClient("mongodb+srv://"+up+"@movies-2.nlmxu.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db2 = db2["database"]
db2 = db2["movies"]

from imdb_pb2 import (
    IMDBData,
    IMDBDataList,
    IMDBByIdRequest,
    IMDBByNameRequest,
    IMDBByCategoryRequest,
    IMDBData,
    AddIMDBResponse
)

import imdb_pb2_grpc

class IMDBService(imdb_pb2_grpc.IMDBServicer):

    def GetIMDBs(self, request, context):

        n_results = request.max_results

        db1_size = db1.estimated_document_count()
        first = request.page * n_results
        last = (request.page + 1) * request.max_results - 1

        results = []
        if last < db1_size:
            results = list(db1.find().skip(first).limit(n_results))
        elif first > db1_size:
            results = list(db2.find().skip(first+1-db1_size).limit(n_results))
        else:
            limit1 = db1_size - first
            limit2 = n_results - limit1
            results  = list(db1.find().skip(first).limit(limit1))
            results += list(db2.find().skip(db1_size-first+1).limit(limit2))

        results = [ imdb_to_proto(imdb) for imdb in results ]
        return IMDBDataList( imdbs = results )
        
    def SearchById(self, request, context):
        try:
            results = list(db1.find({ "_id": ObjectId(request.imdb_id) }).limit(1))
            if len(results) <= 0:
                results = list(db2.find({ "_id": ObjectId(request.imdb_id) }).limit(1))

            if len(results) <= 0:
                raise NotFound("Id not found")

            return imdb_to_proto(results[0])
        except:
            return IMDBData()

    def SearchByName(self, request, context):
        req = { "name": { "$regex" : ".*"+request.name+".*" } }
        results = search_by_name(req,request.max_results)
        return IMDBDataList( imdbs = results )

    def SearchByCategory(self, request, context):
        n_results = request.max_results
        results = list(db1.find({ "category": { "$all": [request.category] } }).limit(n_results))

        if len(results) < n_results:
            results += list(db2.find({ "category": { "$all": [request.category] } }).limit(n_results-len(results)))

        results = [ imdb_to_proto(imdb) for imdb in results ]
        return IMDBDataList( imdbs = results )

    def AddIMDB(self, request, context):
        imdb = proto_to_imdb(request)
        try:
            id = db1.insert_one(imdb).inserted_id
        except Exception:
            try:
                id = db2.insert_one(imdb).inserted_id
            except Exception: 
                return AddIMDBResponse(imdb_id=None)
        return AddIMDBResponse(imdb_id=str(id))

    def RemoveIMDB(self, request, context):
        try:
            db1.delete_one({"_id": ObjectId(request.imdb_id)})
        except Exception:
            try:
                db2.delete_one({"_id": ObjectId(request.imdb_id)})
            except Exception:
                return Success(success=False)
        return Success(success=True)

def search_by_name(request,n_results):
    results = list(db1.find(request).limit(n_results))
    if len(results) < n_results:
        results += list(db2.find(request).limit(len(results)-n_results))

    return [ imdb_to_proto(imdb) for imdb in results ]

def imdb_to_proto(result):
    if(result["rating"]== '-'):
        result["rating"] = None
    imdb = IMDBData (
        imdb_id = str(result["_id"]),
        imdb_title = result["name"],
        genres = result["category"],
        imdb_rating = result["rating"],
        # img_url = result["imageURL"],
        type = result["type"],
    )
    # imdb.genres.extends(result["category"])
    return imdb

def proto_to_imdb(proto):
    movie = {
        'name': proto.imdb_title,
        'category': [c for c in proto.genres],
        'rating': proto.imdb_rating,
        'imageURL' : proto.img_url,
        'type': proto.type
    }
    return movie

def serve():
    interceptors = [ExceptionToStatusInterceptor()]
    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=10), interceptors=interceptors
    )
    imdb_pb2_grpc.add_IMDBServicer_to_server(
        IMDBService(), server
    )
    
    # with open("imdb.key", "rb") as fp:
        # imdb_key = fp.read()
    # with open("imdb.pem", "rb") as fp:
        # imdb_cert = fp.read()
    # with open("ca.pem", "rb") as fp:
        # ca_cert = fp.read()
    
    # creds = grpc.ssl_server_credentials(
        # [(imdb_key, imdb_cert)],
        # root_certificates=ca_cert,
        # require_client_auth=True,
    # )
    
    # server.add_secure_port("[::]:50052", creds)
    server.add_insecure_port("[::]:50052")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
