from concurrent import futures
from pymongo import MongoClient

import grpc
from grpc_interceptor import ExceptionToStatusInterceptor
from grpc_interceptor.exceptions import NotFound

from anime_pb2 import (
    AnimeData,
    AnimeDataList,
    AnimeByIdRequest,
    AnimeByNameRequest,
    AnimeByCategoryRequest,
    
)
import anime_pb2_grpc

# Acesso ah base de dados


class AnimeService(anime_pb2_grpc.AnimeServicer):
    def SearchById(self, request, context):
        cur = con.cursor()
        cur.execute('SELECT anime_id,anime_title,genres,anime_rating FROM anime_data WHERE anime_id=?', (request.anime_id,))
        
        anime = cur.fetchone()
        print(anime)
        if anime is None:
            raise NotFound("Id not found")
        send = AnimeData(anime_id = anime[0], anime_title = anime[1], genres = anime[2], anime_rating = anime[3])
        print(send)
        return AnimeResponse(anime = send)
        #if request.anime_id not in anime_database:
        #    raise NotFound("Id not found")

        #anime_with_id = anime_database[request.anime_id]
        #return AnimeData(anime=anime_with_id)
        
    def SearchByName(self, request, context):
    
        cur = con.cursor()
        cur.execute('SELECT anime_id,anime_title,genres,anime_rating FROM anime_data WHERE anime_title LIKE ? ', ( request.name,))
        anime_with_name = cur.fetchall()
        
        if anime_with_name is None:
            raise NotFound("Id not found")
            
        num_results = min(request.max_results, len(animes_with_name))
        searched_animes = random.sample(animes_with_name, num_results)

        return AnimeDataList(anime=searched_animes)
    
        #if request.name not in anime_database:
        #    raise NotFound("Name not found")
        
        #anime_with_name = anime_database[request.name]
        #num_results = min(request.max_results, len(anime_with_name))
        #searched_anime = random.sample(anime_with_name, num_results)

        #return AnimeDataList(anime=searched_anime)
        
    def SearchByCategory(self, request, context):
    
        cur = con.cursor()
        cur.execute('SELECT anime_id,anime_title,genres,anime_rating FROM anime_data WHERE genres LIKE ? ', ("%" + request.category + "%",))
        anime_with_category = cur.fetchall()
        
        if anime_with_category is None:
            raise NotFound("Id not found")
            
        num_results = min(request.max_results, len(anime_with_category))
        searched_animes = random.sample(animes_with_category, num_results)

        return AnimeDataList(animes=searched_animes)
    
        #if request.category not in anime_database:
        #    raise NotFound("Category not found")
        
        #anime_with_category = anime_database[request.category]
        #num_results = min(request.max_results, len(anime_with_name))
        #searched_anime = random.sample(anime_with_category, num_results)

        #return AnimeDataList(anime=searched_anime)
        


def serve():
    interceptors = [ExceptionToStatusInterceptor()]
    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=10), interceptors=interceptors
    )
    anime_pb2_grpc.add_AnimeServicer_to_server(
        animeService(), server
    )
    
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
