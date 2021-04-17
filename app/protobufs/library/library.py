from concurrent import futures
import os

import grpc
from grpc_interceptor import ExceptionToStatusInterceptor

from book_pb2 import *
from book_pb2_grpc import BookStub

from imdb_pb2 import *
from imdb_pb2_grpc import IMDBStub

from anime_pb2 import *
from anime_pb2_grpc import AnimeStub

from account_pb2 import *
from account_pb2_grpc import AccountStub

from utils_pb2 import *

from library_pb2 import *
import library_pb2_grpc

# with open("library.key", "rb") as fp:
    # library_key = fp.read()
# with open("library.pem", "rb") as fp:
    # library_cert = fp.read()
# with open("ca.pem", "rb") as fp:
    # ca_cert = fp.read()
# creds = grpc.ssl_channel_credentials(ca_cert, library_key, library_cert)

# # initialize channels
# books_host = os.getenv("BOOKS_HOST", "localhost")
# books_channel = grpc.secure_channel(f"{books_host}:50051", creds)
# books_client = BookStub(books_channel)

# imdbs_host = os.getenv("IMDBS_HOST", "localhost")
# imdbs_channel = grpc.secure_channel(f"{imdbs_host}:50052", creds)
# imdbs_client = IMDBStub(imdbs_channel)

# animes_host = os.getenv("ANIMES_HOST", "localhost")
# animes_channel = grpc.secure_channel(f"{animes_host}:50053", creds)
# animes_client = AnimeStub(animes_channel)

# accounts_host = os.getenv("ACCOUNTS_HOST", "localhost")
# accounts_channel = grpc.secure_channel(f"{accounts_host}:50055", creds)
# accounts_client = AccountStub(accounts_channel)

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

        animes_request = GetAnimesRequest(page=page, max_results=n)
        r1 = animes_client.GetAnimes(animes_request).animes
        books_request = GetBooksRequest(page=page, max_results=n)
        r2 = books_client.GetBooks(books_request).books
        imdbs_request = GetIMDBsRequest(page=page, max_results=n)
        r3 = imdbs_client.GetIMDBs(imdbs_request).imdbs

        r1 = [ItemInfo(id=r.anime_id, name=r.anime_title, type=Type.ANIME) for r in r1]
        r2 = [ItemInfo(id=r.book_id, name=r.book_title, type=Type.BOOK) for r in r2]
        r3 = [ItemInfo(id=r.imdb_id, name=r.imdb_title, type=Type.SHOW) for r in r3]
        results = r1 + r2 + r3

        return ItemInfoResponse(recommendations=results)

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
        r = []
        for type in types:

            if (type == Type.ANIME):

                for top in top_categories:
                    animes_category_request = AnimeByCategoryRequest(category=top[0],
                                                                     max_results=max)  # top[0] = categoria
                    get_random_sample = animes_client.SearchByCategory(animes_category_request).animes
                    cur = [ItemInfo(id=c.anime_id, name=c.anime_title, type=Type.ANIME) for c in get_random_sample]
                    r = r + cur
                if not r:
                    animes_random_request = GetAnimesRequest(page=0, max_results=max)
                    get_random_sample = animes_client.GetAnimes(animes_random_request).animes
                    cur = [ItemInfo(id=c.anime_id, name=c.anime_title, type=Type.ANIME) for c in get_random_sample]
                    r = r + cur
            elif (type == Type.BOOK):

                for top in top_categories:
                    books_category_request = BooksByCategoryRequest(category=top[0],
                                                                    max_results=max)  # top[0] = categoria
                    get_random_sample = books_client.SearchByCategory(books_category_request).books
                    cur = [ItemInfo(id=c.book_id, name=c.book_title, type=Type.BOOK) for c in get_random_sample]
                    r = r + cur
                if not r:
                    books_random_request = GetBooksRequest(page=0, max_results=max)
                    get_random_sample = books_client.GetBooks(books_random_request).books
                    cur = [ItemInfo(id=c.book_id, name=c.book_title, type=Type.BOOK) for c in get_random_sample]
                    r = r + cur

            elif (type == Type.SHOW):

                for top in top_categories:
                    imdbs_category_request = IMDBByCategoryRequest(category=top[0],
                                                                   max_results=max)  # top[0] = categoria
                    get_random_sample = imdbs_client.SearchByCategory(imdbs_category_request).imdbs
                    cur = [ItemInfo(id=c.imdb_id, name=c.imdb_title, type=Type.SHOW) for c in get_random_sample]
                    r = r + cur
                if not r:
                    imdbs_random_request = GetIMDBsRequest(page=0, max_results=max)
                    get_random_sample = imdbs_client.GetIMDBs(imdbs_random_request).imdbs
                    cur = [ItemInfo(id=c.imdb_id, name=c.imdb_title, type=Type.SHOW) for c in get_random_sample]
                    r = r + cur

        return ItemInfoResponse(recommendations=r)

    def AddItem(self, request, context):
        id = request.user_id
        type = request.type

        user_id_request = UserId(id=id)
        isAdmin = accounts_client.VerificarAdmin(user_id_request).success

        if not isAdmin:
            return Success(success=False)

        if (type == Type.ANIME):
            return animes_client.AddAnime(request.anime)
        elif (type == Type.BOOK):
            return books_client.AddBook(request.book)
        elif (type == Type.SHOW):
            return imdbs_client.AddIMDB(request.imdb)

        else:
            return Success(success=False)

    def GetItem(self, request, context):
        id = request.id
        type = request.type

        seen_and_like_item_request = SeenAndLikeItem(id=id, type=type)
        likes = accounts_client.GetLikesItem(seen_and_like_item_request).count
        seens = accounts_client.GetSeensItem(seen_and_like_item_request).count

        if (type == Type.ANIME):
            animes_request = AnimeByIdRequest(anime_id=id)
            anime = animes_client.SearchById(animes_request)
            return Item(anime=anime, likes=likes, seens=seens)
        elif (type == Type.BOOK):
            books_request = BookByIdRequest(book_id=id)
            book = books_client.SearchById(books_request)
            return Item(book=book, likes=likes, seens=seens)
        elif (type == Type.SHOW):
            imdbs_request = IMDBByIdRequest(imdb_id=id)
            imdb = imdbs_client.SearchById(imdbs_request)
            return Item(imdb=imdb, likes=likes, seens=seens)
        else:
            return Item()

    def RemoveItem(self, request, context):
        id = request.user_id
        type = request.type

        user_id_request = UserId(id=id)
        isAdmin = accounts_client.VerificarAdmin(user_id_request).success

        if not isAdmin:
            return Success(success=False)

        if (type == Type.ANIME):
            return animes_client.RemoveAnime(AnimeByIdRequest(anime_id=request.id))
        elif (type == Type.BOOK):
            return books_client.RemoveBook(BookByIdRequest(book_id=request.id))
        elif (type == Type.SHOW):
            return imdbs_client.RemoveIMDB(IMDBByIdRequest(imdb_id=request.id))
        else:
            return Success(success=False)

    def AddSeenItem(self, request, context):
        id = request.id
        type = request.type

        if (type == Type.ANIME):

            animes_request = AnimeByIdRequest(anime_id=id)
            anime = animes_client.SearchById(animes_request)
            genres = anime.genres
            seen_and_like_request = SeenAndLikeInfo(user_id=request.user_id, id=id, type=type, categories=genres)

            return accounts_client.Seen(seen_and_like_request)

        elif (type == Type.BOOK):

            books_request = BookByIdRequest(book_id=id)
            book = books_client.SearchById(books_request)
            genres = book.genres
            seen_and_like_request = SeenAndLikeInfo(user_id=request.user_id, id=id, type=type, categories=genres)

            return accounts_client.Seen(seen_and_like_request)

        elif (type == Type.SHOW):

            imdbs_request = IMDBByIdRequest(imdb_id=id)
            imdb = imdbs_client.SearchById(imdbs_request)
            genres = imdb.genres
            seen_and_like_request = SeenAndLikeInfo(user_id=request.user_id, id=id, type=type, categories=genres)

            return accounts_client.Seen(seen_and_like_request)

    def AddLikeItem(self, request, context):
        id = request.id
        type = request.type

        if (type == Type.ANIME):

            animes_request = AnimeByIdRequest(anime_id=id)
            anime = animes_client.SearchById(animes_request)
            genres = anime.genres

            seen_and_like_request = SeenAndLikeInfo(user_id=request.user_id, id=id, type=type, categories=genres)

            ret = accounts_client.Like(seen_and_like_request)
            return ret

        elif (type == Type.BOOK):

            books_request = BookByIdRequest(book_id=id)
            book = books_client.SearchById(books_request)
            genres = book.genres
            seen_and_like_request = SeenAndLikeInfo(user_id=request.user_id, id=id, type=type, categories=genres)

            return accounts_client.Like(seen_and_like_request)

        elif (type == Type.SHOW):

            imdbs_request = IMDBByIdRequest(imdb_id=id)
            imdb = imdbs_client.SearchById(imdbs_request)
            genres = imdb.genres
            seen_and_like_request = SeenAndLikeInfo(user_id=request.user_id, id=id, type=type, categories=genres)

            return accounts_client.Like(seen_and_like_request)


def serve():
    interceptors = [ExceptionToStatusInterceptor()]
    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=10), interceptors=interceptors
    )
    library_pb2_grpc.add_LibraryServicer_to_server(
        LibraryService(), server
    )

    # creds_server = grpc.ssl_server_credentials(
        # [(library_key, library_cert)],
        # root_certificates=ca_cert,
        # require_client_auth=True,
    # )
    
    # server.add_secure_port("[::]:50050", creds_server)
    # server.start()
    # server.wait_for_termination()
    
    server.add_insecure_port("[::]:50050")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
