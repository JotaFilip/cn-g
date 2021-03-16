from concurrent import futures
from pymongo import MongoClient

import grpc
from grpc_interceptor import ExceptionToStatusInterceptor
from grpc_interceptor.exceptions import NotFound

from book_pb2 import BookData, BookByIdRequest, BooksByNameRequest, BooksByCategoryRequest
from book_pb2_grpc import BookStub

from imdb_pb2 import IMDBData, IMDBByIdRequest, IMDBByNameRequest, IMDBByCategoryRequest
from imdb_pb2_grpc import IMDBStub

from anime_pb2 import AnimeData, AnimeByIdRequest, AnimeByNameRequest, AnimeByCategoryRequest
from anime_pb2_grpc import AnimeStub

from library_pb2 import (
    Type,
    BasicInfoResponse,
    BookBasicInfo,
	IMDBBasicInfo,
	AnimeBasicInfo,
	RecommendationRequest,
	SearchByNameRequest,
	SearchByCategoryRequest,
    
)
import library_pb2_grpc

class LibraryService(library_pb2_grpc.LibraryServicer):

    def Recommend(self, request, context):

        chosen_type = request.types
        num_results = min(request.max_results, len(books_with_name))
        book_with_id = 1
        return BookData(books=book_with_id)
        
    def GetBook(self, request, context):
                
        books_channel = grpc.insecure_channel(f"{recommendations_host}:50051")
        books_client = BookStub(books_channel)
        
        books_request = BookByIdRequest(
            book_id=request.book_id
        )
    
        books_response = books_client.SearchById(
            books_request
        )
        
        if(books_response is None):
            print("ERROR")
        print(books_response.book)

        return BookDataList(books=books_response.book)
        
    def GetIMDB(self, request, context):
        
        imdb_channel = grpc.insecure_channel(f"{recommendations_host}:50052")
        imdb_client = IMDBStub(imdb_channel)
        
        imdb_request = IMDBByIdRequest(
            imdb_id=request.imdb_id
        )
    
        imdb_response = imdb_client.SearchById(
            imdb_request
        )
        
        if(imdb_response is None):
            print("ERROR")
        print(imdb_response.imdb)

        return imdbDataList(imdb=imdb_response.imdb)
    
	def GetAnime(self, request, context):
        
        animes_channel = grpc.insecure_channel(f"{recommendations_host}:50053")
        animes_client = AnimeStub(animes_channel)
        
        animes_request = AnimeByIdRequest(
            anime_id=request.anime_id
        )
    
        animes_response = animes_client.SearchById(
            animes_request
        )
        
        if(animes_response is None):
            print("ERROR")
        print(animes_response.anime)

        return AnimeDataList(anime=animes_response.anime)
	
	def SearchByName(self, request, context):
        
        book_list = []
        imdb_list = []
        anime_list = []
        
        if request.types == Type.BOOK || request.types == Type.ALL:
        
            books_channel = grpc.insecure_channel(f"{recommendations_host}:50051")
            books_client = BookStub(books_channel)
            
            books_request = BooksByNameRequest(
                name=request.name
                max_results=request.max_results
            )
        
            books_response = books_client.SearchByName(
                books_request
            )
            
            if(books_response is None):
                print("ERROR")
            print(books_response.books)
            
            for x in books_response.books:
                cur = BookBasicInfo (
                    book_id = x.book_id,
                    book_name = x.book_title
                )
                book_list.append(cur)
            
            
            #return BasicInfoResponse(book_recommendations=book_list, imdb_recommendations=None, anime_recommendations=None)
        
        if request.types == Type.SHOW || request.types == Type.ALL:
            
            imdb_channel = grpc.insecure_channel(f"{recommendations_host}:50052")
            imdb_client = IMDBStub(imdb_channel)
            
            imdb_request = IMDBByNameRequest(
                name=request.name
                max_results=request.max_results
            )
        
            imdb_response = imdb_client.SearchByName(
                imdb_request
            )
            
            if(imdb_response is None):
                print("ERROR")
            print(imdb_response.imdb)
            
            for x in imdb_response.imdb:
                cur = IMDBBasicInfo (
                    imdb_id = x.imdb_id,
                    imdb_name = x.imdb_title
                )
                imdb_list.append(cur)
                
            #return BasicInfoResponse(imdb_recommendations=imdb_list, imdb_recommendations=None, anime_recommendations=None)

        if request.types == Type.ANIME || request.types == Type.ALL:
        
            animes_channel = grpc.insecure_channel(f"{recommendations_host}:50053")
            animes_client = AnimeStub(animes_channel)
            
            animes_request = AnimeByNameRequest(
                name=request.name
                max_results=request.max_results
            )
        
            animes_response = animes_client.SearchByName(
                animes_request
            )
            
            if(animes_response is None):
                print("ERROR")
            print(animes_response.anime)
            
            for x in animes_response.anime:
                cur = AnimeBasicInfo (
                    anime_id = x.anime_id,
                    anime_name = x.anime_title
                )
                anime_list.append(cur)
                
            #return BasicInfoResponse(book_recommendations=book_list, imdb_recommendations=None, anime_recommendations=None)
            
        return BasicInfoResponse(book_recommendations=book_list, imdb_recommendations=imdb_list, anime_recommendations=anime_list)

	def SearchByCategory(self, request, context):
    
        book_list = []
        imdb_list = []
        anime_list = []
        
        if request.types == Type.BOOK:
        
            books_channel = grpc.insecure_channel(f"{recommendations_host}:50052")
            books_client = BookStub(books_channel)
            
            books_request = BooksByCategoryRequest(
                category=request.category
                max_results=request.max_results
            )
        
            books_response = books_client.SearchByCategory(
                books_request
            )
            
            if(books_response is None):
                print("ERROR")
            print(books_response.books)
            
            for x in books_response.books:
                cur = BookBasicInfo (
                    book_id = x.book_id,
                    book_name = x.book_title
                )
                book_list.append(cur)
                
            #return BasicInfoResponse(book_recommendations=book_list, imdb_recommendations=None, anime_recommendations=None)
            
        if request.types == Type.SHOW || request.types == Type.ALL:
            
            imdb_channel = grpc.insecure_channel(f"{recommendations_host}:50052")
            imdb_client = IMDBStub(imdb_channel)
            
            imdb_request = IMDBByCategoryRequest(
                category=request.category
                max_results=request.max_results
            )
        
            imdb_response = imdb_client.SearchByCategory(
                imdb_request
            )
            
            if(imdb_response is None):
                print("ERROR")
            print(imdb_response.imdb)
            
            for x in imdb_response.imdb:
                cur = IMDBBasicInfo (
                    imdb_id = x.imdb_id,
                    imdb_name = x.imdb_title
                )
                imdb_list.append(cur)
                
            #return BasicInfoResponse(imdb_recommendations=imdb_list, imdb_recommendations=None, anime_recommendations=None)

        if request.types == Type.ANIME || request.types == Type.ALL:
        
            animes_channel = grpc.insecure_channel(f"{recommendations_host}:50053")
            animes_client = AnimeStub(animes_channel)
            
            animes_request = AnimeByCategoryRequest(
                category=request.category
                max_results=request.max_results
            )
        
            animes_response = animes_client.SearchByCategory(
                animes_request
            )
            
            if(animes_response is None):
                print("ERROR")
            print(animes_response.anime)
            
            for x in animes_response.anime:
                cur = AnimeBasicInfo (
                    anime_id = x.anime_id,
                    anime_name = x.anime_title
                )
                anime_list.append(cur)
                
            #return BasicInfoResponse(book_recommendations=book_list, imdb_recommendations=None, anime_recommendations=None)
            
        return BasicInfoResponse(book_recommendations=book_list, imdb_recommendations=imdb_list, anime_recommendations=anime_list)


def serve():
    interceptors = [ExceptionToStatusInterceptor()]
    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=10), interceptors=interceptors
    )
    book_pb2_grpc.add_BookServicer_to_server(
        BookService(), server
    )
    
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
