from concurrent import futures
from pymongo import MongoClient

import grpc
from grpc_interceptor import ExceptionToStatusInterceptor
from grpc_interceptor.exceptions import NotFound

from library_pb2 import (
    Type,
    BasicInfoResponse,
    BookData,
    BookBasicInfo,
    IMDBData,
	IMDBBasicInfo,
	AnimeData,
	AnimeBasicInfo,
	RecommendationRequest,
	BookByIdRequest,
	IMDBByIdRequest,
	AnimeByIdRequest,
	SearchByNameRequest,
	SearchByCategoryRequest,
    
)
import library_pb2_grpc

# Acesso ah base de dados


class LibraryService(library_pb2_grpc.LibraryServicer):

    def Recommend(self, request, context):

        chosen_type = request.types
		num_results = min(request.max_results, len(books_with_name))
        book_with_id = books_database[request.book_id]
        return BookData(books=book_with_id)
        
    def GetBook(self, request, context):
    
        if request.name not in books_database:
            raise NotFound("Name not found")
        
        books_with_name = books_database[request.name]
        num_results = min(request.max_results, len(books_with_name))
        searched_books = random.sample(books_with_name, num_results)

        return BookDataList(books=searched_books)
        
    def GetIMDB(self, request, context):
    
        if request.category not in books_database:
            raise NotFound("Category not found")
        
        books_with_category = books_database[request.category]
        num_results = min(request.max_results, len(books_with_name))
        searched_books = random.sample(books_with_category, num_results)

        return BookDataList(books=searched_books)
    
	def GetAnime(self, request, context):
	
	def SearchByName(self, request, context):
	
	def SearchByCategory(self, request, context):


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
