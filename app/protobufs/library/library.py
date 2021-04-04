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

from library_pb2 import *
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

accounts_host = os.getenv("ACCOUNTS_HOST", "localhost")
accounts_channel = grpc.insecure_channel(f"{accounts_host}:50055")
accounts_client = AccountStub(accounts_channel)

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
    
        id = request.user_id
        max = request.max_results
        types = request.types
        
        user_id_request = UserId(id=id)
        categories = accounts_client.GetContagemLikesAndViews(user_id_request).tuples
        
        score_list = {}
        
        for category in categories:
            score_list[category.category] = -category.views + category.likes * 4
            
        sorted_categories = sorted(score_list.items(), key=lambda x: x[1], reverse=True)
        top_categories = sorted_categories[0:3]
        
        for type in types:
            r = []
            if(type == "ANIME"):
                for top in top_categories:
                    animes_category_request = AnimeByCategoryRequest(category=top[0], max) #top[0] = categoria
                    get_random_sample = animes_client.SearchByCategory(animes_category_request)
                    cur = [ ItemInfo( id = c.anime_id, name = c.anime_title, type = Type.ANIME) for c in get_random_sample ]
                    r = r + cur
                    
            elif(type == "BOOK"):
                    books_category_request = BooksByCategoryRequest(category=top[0], max) #top[0] = categoria
                    get_random_sample = books_client.SearchByCategory(books_category_request)
                    cur = [ ItemInfo( id = c.book_id, name = c.book_title, type = Type.BOOK) for c in get_random_sample ]
                    r = r + cur
            elif(type == "SHOW"):
                    imdbs_category_request = IMDBByCategoryRequest(category=top[0], max) #top[0] = categoria
                    get_random_sample = imdbs_client.SearchByCategory(imdbs_category_request)
                    cur = [ ItemInfo( id = c.imdb_id, name = c.imdb_title, type = Type.SHOW) for c in get_random_sample ]
                    r = r + cur

        return r

    def AddItem(self, request, context):
        return None

    def GetItem(self, request, context):
        id = request.id
        type = request.type
        if(type == "ANIME"):
            animes_request = AnimeByIdRequest(anime_id=id)
            anime = animes_client.SearchById(animes_request)
            return Item(anime = anime)
        elif(type == "BOOK"):
            books_request = BookByIdRequest(book_id=id)
            book = books_client.SearchById(books_request)
            return Item(book = book)
        elif(type == "SHOW"):
            imdbs_request = IMDBByIdRequest(imdb_id=id)
            imdb = imdbs_client.SearchById(imdbs_request)
            return Item(imdb = imdb)
        else:
            return Item()







    def RemoveItem(self, request, context):
        return None
    
    def AddSeenItem(self, request, context):
        id = request.id
        type = request.type
        
        if(type == "ANIME"):
        
            animes_request = AnimeByIdRequest(anime_id=id)
            anime = animes_client.SearchById(animes_request)
            genres = anime.genres
            seen_and_like_request = SeenAndLikeInfo(id=id, type=type, categories=genres)
            
            return accounts_client.Seen(seen_and_like_request)
            
        elif(type == "BOOK"):
        
            books_request = BookByIdRequest(book_id=id)
            book = books_client.SearchById(books_request)
            genres = book.genres
            seen_and_like_request = SeenAndLikeInfo(id=id, type=type, categories=genres)
            
            return accounts_client.Seen(seen_and_like_request)
            
        elif(type == "SHOW"):
        
            imdbs_request = IMDBByIdRequest(imdb_id=id)
            imdb = imdbs_client.SearchById(imdbs_request)
            genres = imdb.genres
            seen_and_like_request = SeenAndLikeInfo(id=id, type=type, categories=genres)
            
            return accounts_client.Seen(seen_and_like_request)

    def AddLikeItem(self, request, context):
        id = request.id
        type = request.type
        
        if(type == "ANIME"):
        
            animes_request = AnimeByIdRequest(anime_id=id)
            anime = animes_client.SearchById(animes_request)
            genres = anime.genres
            seen_and_like_request = SeenAndLikeInfo(id=id, type=type, categories=genres)
            
            return accounts_client.Like(seen_and_like_request)
            
        elif(type == "BOOK"):
        
            books_request = BookByIdRequest(book_id=id)
            book = books_client.SearchById(books_request)
            genres = book.genres
            seen_and_like_request = SeenAndLikeInfo(id=id, type=type, categories=genres)
            
            return accounts_client.Like(seen_and_like_request)
            
        elif(type == "SHOW"):
        
            imdbs_request = IMDBByIdRequest(imdb_id=id)
            imdb = imdbs_client.SearchById(imdbs_request)
            genres = imdb.genres
            seen_and_like_request = SeenAndLikeInfo(id=id, type=type, categories=genres)
            
            return accounts_client.Like(seen_and_like_request)

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