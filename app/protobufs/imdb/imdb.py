from concurrent import futures
from pymongo import MongoClient

import grpc
from grpc_interceptor import ExceptionToStatusInterceptor
from grpc_interceptor.exceptions import NotFound

from imdb_pb2 import (
    IMDBData,
    IMDBDataList,
    IMDBByIdRequest,
    IMDBByNameRequest,
    IMDBByCategoryRequest, IMDBData
    
)
import imdb_pb2_grpc

# ඞ


class IMDBService(imdb_pb2_grpc.IMDBServicer):
    def SearchById(self, request, context):
        cur = con.cursor()
        cur.execute('SELECT imdb_id,imdb_title,genres,imdb_rating FROM imdb_data WHERE book_id=?', (request.book_id,))
        
        if request.imdb_id not in imdb_database:
            raise NotFound("Id not found")

        imdb_with_id = imdb_database[request.imdb_id]
        return IMDBData(imdb=imdb_with_id)
        
    def SearchByName(self, request, context):
    
        if request.name not in imdb_database:
            raise NotFound("Name not found")
        
        imdb_with_name = imdb_database[request.name]
        num_results = min(request.max_results, len(imdb_with_name))
        searched_imdb = random.sample(imdb_with_name, num_results)

        return IMDBDataList(imdb=searched_imdb)
        
    def SearchByCategory(self, request, context):
    
        if request.category not in imdb_database:
            raise NotFound("Category not found")
        
        imdb_with_category = imdb_database[request.category]
        num_results = min(request.max_results, len(imdb_with_name))
        searched_imdb = random.sample(imdb_with_category, num_results)

        return IMDBDataList(imdb=searched_imdb)
        


def serve():
    interceptors = [ExceptionToStatusInterceptor()]
    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=10), interceptors=interceptors
    )
    imdb_pb2_grpc.add_IMDBServicer_to_server(
        IMDBService(), server
    )
    
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
