
# Library API
import os
from library_pb2 import *
from library_pb2_grpc import LibraryStub
import grpc
from grpc_interceptor import ExceptionToStatusInterceptor

lib_host = os.getenv("LIBRARY_HOST", "localhost")
lib_channel = grpc.insecure_channel(f"{lib_host}:50050")
lib_client = LibraryStub(lib_channel)

# TODO
# how to handle the user_id situation

def getLibrary(page):

    request = LibPageRequest (
        page = page,
        max_results = 30
    )
    ret = []
    for r in lib_client.Library(request).recommendations:
        type= "All"
        if (r.type == 0):
            type = "BOOK"
        if (r.type == 1):
            type = "SHOW"
        if (r.type == 2):
            type = "ANIME"

        object = {"id" : r.id, "name" : r.name, "type" : type}
        ret.append(object)
    return ret

def getSuggestions():

    request = RecommendationRequest (
        user_id = "0",            # TODO
        max_results = 30,
        types = []              # TODO
    )
    return lib_client.Recommend(request)

def addItem(body):

    request = AddItemRequest(body)
    return lib_client.AddItem(request)

def getItemById(type,itemId):

    request = ItemId(id = itemId, type=type)
    response= lib_client.GetItem(request)
    if(response.book.book_id == '' and response.imdb.imdb_id == '' and response.anime.anime_id == ''):
        return 'Id Not Found', 400
    if (response.book.book_id != ''):
        category = []
        for cat in response.book.genres:
            category.append(cat)

        return {"id" : response.book.book_id, "name" : response.book.book_title, "type" : "BOOK", "description": response.book.description,
                "photoUrl":response.book.img_url, "category": category, "rating": response.book.book_rating}
    if (response.imdb.imdb_id != ''):
        category = []
        for cat in response.imdb.genres:
            category.append(cat)

        return {"id": response.imdb.imdb_id, "name": response.imdb.imdb_title, "type": "SHOW",
                "photoUrl": response.imdb.img_url, "category": category, "rating": response.imdb.imdb_rating}


    if (response.anime.anime_id != ''):
        category = []
        for cat in response.anime.genres:
            category.append(cat)

        return {"id":response.anime.anime_id, "name":response.anime.anime_title, "type": "ANIME",
                "photoUrl": response.anime.img_url, "category": category, "rating": response.anime.anime_rating}
    return 'Id Not Found', 400

def deleteItem(type,itemId):

    request = ItemId (
        id = itemId,
        type = type
    )
    return lib_client.RemoveItem(request)

def updateItemSeen(type,itemId):

    request = ItemId (
        id = itemId,
        type = type
    )
    return lib_client.UpdateSeenItem(request)

def updateItemLike(type,itemId):

    request = ItemId (
        id = itemId,
        type = type
    )
    return lib_client.UpdateLikeItem(request)
