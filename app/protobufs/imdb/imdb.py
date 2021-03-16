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

class IMDBService(imdb_pb2_grpc.IMDBServicer):
    def SearchById(self, request, context):
        cur = con.cursor()
        cur.execute('SELECT imdb_id,imdb_title,genres,imdb_rating FROM imdb_data WHERE imdb_id=?', (request.imdb_id,))
        
        if request.imdb_id not in imdb_database:
            raise NotFound("Id not found")

        imdb_with_id = imdb_database[request.imdb_id]
        return IMDBData(imdb=imdb_with_id)
        
    def SearchByName(self, request, context):
    
        cur = con.cursor()
        cur.execute('SELECT imdb_id,imdb_title,genres,imdb_rating FROM imdb_data WHERE imdb_title = ? ', ( request.name,))
        imdb_with_name = cur.fetchall()
        
        if imdb_with_name is None:
            raise NotFound("Name not found")
            
        num_results = min(request.max_results, len(imdb_with_name))
        searched_imdb = random.sample(imdb_with_name, num_results)

        return IMDBDataList(imdb=searched_imdb)
        
    def SearchByCategory(self, request, context):
    
        cur = con.cursor()
        cur.execute('SELECT imdb_id,imdb_title,genres,imdb_rating FROM imdb_data WHERE genres LIKE ? ', ("%" + request.category + "%",))
        imdb_with_category = cur.fetchall()
        
        if imdb_with_category is None:
            raise NotFound("Category not found")
        
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
    
    server.add_insecure_port("[::]:50052")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
