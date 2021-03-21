from concurrent import futures
import os

import grpc
from grpc_interceptor import ExceptionToStatusInterceptor
from grpc_interceptor.exceptions import NotFound

from book_pb2 import *
from book_pb2_grpc import BookStub

from imdb_pb2 import *
from imdb_pb2_grpc import IMDBStub

from anime_pb2 import *
from anime_pb2_grpc import AnimeStub

from library_pb2 import (
    Type,
    ItemInfoResponse,
    ItemInfo,
	Item,
	LibPageRequest,
	RecommendationRequest,
	SearchByNameRequest,
    SearchByCategoryRequest,
    AddItemRequest,
    ItemId
)
import library_pb2_grpc

# initialize channels
books_host = os.getenv("BOOKS_HOST", "localhost")
books_channel = grpc.insecure_channel(f"{books_host}:50051")
books_client = BookStub(books_channel)

imdbs_host = os.getenv("IMDBS_HOST", "localhost")
imdbs_channel = grpc.insecure_channel(f"{imdbs_host}:50052")
imdbs_client = IMDBStub(imdbs_channel)

animes_host = os.getenv("ANIMES_HOST", "localhost")
animes_channel = grpc.insecure_channel(f"{animes_host}:50053")
animes_client = AnimeStub(animes_channel)

class LibraryService(library_pb2_grpc.LibraryServicer):

    def Library(self, request, context):

        page = request.page
        max_results = request.max_results

        n = max_results // 3

        animes_request = GetAnimesRequest( page = page, max_results = n )
        r1 = animes_client.GetAnimes(animes_request).animes
        books_request = GetBooksRequest( page = page, max_results = n )
        r2 = books_client.GetBooks(books_request).books
        imdbs_request = GetIMDBsRequest( page = page, max_results = n )
        r3 = imdbs_client.GetIMDBs(imdbs_request).imdbs

        r1 = [ ItemInfo( id = r.anime_id, name = r.anime_title, type = Type.ANIME) for r in r1 ]
        r2 = [ ItemInfo( id = r.book_id, name = r.book_title, type = Type.BOOK) for r in r2 ]
        r3 = [ ItemInfo( id = r.imdb_id, name = r.imdb_title, type = Type.SHOW) for r in r3 ]
        results = r1+r2+r3
        
        return ItemInfoResponse( recommendations = results )


    def Recommend(self, request, context):
        return None

    def GetItem(self, request, context):
        return None

    def RemoveItem(self, request, context):
        return None
    
    def UpdateSeenItem(self, request, context):
        return None

    def UpdateLikeItem(self, request, context):
        return None

    def SearchByName(self, request, context):
        return None

    def SearchByCategory(self, request, context):
        return None

def serve():
    interceptors = [ExceptionToStatusInterceptor()]
    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=10), interceptors=interceptors
    )
    library_pb2_grpc.add_LibraryServicer_to_server(
        LibraryService(), server
    )
    
    server.add_insecure_port("[::]:50050")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()