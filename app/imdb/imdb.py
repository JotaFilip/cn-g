from concurrent import futures
from pymongo import MongoClient

import grpc
from grpc_interceptor import ExceptionToStatusInterceptor
from grpc_interceptor.exceptions import NotFound

from recommendationsIMDB_pb2 import (
    IMDBData,
    IMDBDataList,
    IMDBByIdRequest,
    IMDBByNameRequest,
    IMDBByCategoryRequest,
    
)
import recommendationsIMDB_pb2_grpc

# Acesso ah base de dados


class IMDBService(recommendationsIMDB_pb2_grpc.RecommendationsIMDBServicer):
    def SearchById(self, request, context):
        
        if request.imdb_id not in imdb_database:
            raise NotFound("Id not found")

        imdb_with_id = imdb_database[request.imdb_id]
        return RecommendationResponse(imdb=imdb_with_id)
        
    def SearchByName(self, request, context):
    
        if request.name not in imdb_database:
            raise NotFound("Name not found")
        
        imdb_with_name = imdb_database[request.name]
        num_results = min(request.max_results, len(imdb_with_name))
        searched_imdb = random.sample(imdb_with_name, num_results)

        return RecommendationResponse(imdb=searched_imdb)
        
    def SearchByCategory(self, request, context):
    
        if request.category not in imdb_database:
            raise NotFound("Category not found")
        
        imdb_with_category = imdb_database[request.category]
        num_results = min(request.max_results, len(imdb_with_name))
        searched_imdb = random.sample(imdb_with_category, num_results)

        return RecommendationResponse(imdb=searched_imdb)
        


def serve():
    interceptors = [ExceptionToStatusInterceptor()]
    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=10), interceptors=interceptors
    )
    imdb_pb2_grpc.add_RecommendationsIMDBServicer_to_server(
        IMDBService(), server
    )
    
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
