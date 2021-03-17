from concurrent import futures

import grpc
from grpc_interceptor import ExceptionToStatusInterceptor
from grpc_interceptor.exceptions import NotFound
import sqlite3
import random

con = sqlite3.connect('Shows', check_same_thread=False)

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
        cur = con.cursor()

        cur.execute('SELECT title_basics.tconst,title_basics.primaryTitle,title_basics.genres,title_ratings.averageRating FROM title_basics, title_ratings WHERE title_basics.tconst=? AND title_ratings.tconst=?', (request.imdb_id, request.imdb_id))
        print(request.imdb_id)
        
        imdb = cur.fetchone()
        
        if imdb is None:
            raise NotFound("Id not found")
        send = IMDBData(imdb_id = imdb[0], imdb_title = imdb[1], genres = imdb[2], imdb_rating = imdb[3])
        print(send)
        return IMDBResponse(imdb=send)
        
    def SearchByName(self, request, context):
    
        cur = con.cursor()
        cur.execute('SELECT title_basics.tconst,title_basics.primaryTitle,title_basics.genres,title_ratings.averageRating FROM title_basics, title_ratings WHERE title_basics.primaryTitle = ? AND title_ratings.tconst=title_basics.tconst', (request.name,))
        imdb_with_name = cur.fetchall()
        
        if imdb_with_name is None:
            raise NotFound("Name not found")
            
        num_results = min(request.max_results, len(imdb_with_name))
        searched_imdb = random.sample(imdb_with_name, num_results)

        send = []
        for imdb in searched_imdb:
            curr = IMDBData(imdb_id =imdb[0], imdb_title = imdb[1],genres = imdb[2], imdb_rating = imdb[3])
            send.append(curr)

        return IMDBDataList(imdb=send)
        
    def SearchByCategory(self, request, context):
    
        cur = con.cursor()
        cur.execute('SELECT title_basics.tconst,title_basics.primaryTitle,title_basics.genres,title_ratings.averageRating FROM title_basics, title_ratings WHERE title_basics.genres LIKE ? AND title_ratings.tconst=title_basics.tconst', ("%" + request.category + "%",))
        imdb_with_category = cur.fetchall()
        
        if imdb_with_category is None:
            raise NotFound("Category not found")
        
        num_results = min(request.max_results, len(imdb_with_category))
        searched_imdb = random.sample(imdb_with_category, num_results)
        send = []
        for imdb in searched_imdb:
            curr = IMDBData(imdb_id =imdb[0], imdb_title = imdb[1],genres = imdb[2], imdb_rating = imdb[3])
            send.append(curr)

        return IMDBDataList(imdb=send)
        


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
