
# Library API
import os
from book_pb2 import *
from anime_pb2 import *
from imdb_pb2 import *
from library_pb2 import *
from library_pb2_grpc import LibraryStub
from account_pb2 import *
import grpc
from grpc_interceptor import ExceptionToStatusInterceptor
import connexion

# with open("api_gateway.key", "rb") as fp:
    # api_gateway_key = fp.read()
# with open("api_gateway.pem", "rb") as fp:
    # api_gateway_cert = fp.read()
# with open("ca.pem", "rb") as fp:
    # ca_cert = fp.read()
# creds = grpc.ssl_channel_credentials(ca_cert, api_gateway_key, api_gateway_cert)

# lib_host = os.getenv("LIBRARY_HOST", "localhost")
# lib_channel = grpc.secure_channel(f"{lib_host}:50050", creds)
# lib_client = LibraryStub(lib_channel)
from functools import wraps
lib_host = os.getenv("LIBRARY_HOST", "localhost")
lib_channel = grpc.insecure_channel(f"{lib_host}:50050")
lib_client = LibraryStub(lib_channel)

from flask import redirect
# how to handle the user_id situation

types = {
    "BOOK":  0,
    "SHOW":  1,
    "ANIME": 2,
}
ids = {
    0: "BOOK",
    1: "SHOW",
    2: "ANIME",
}

def get_type(type):
    if type not in types:
        return None
    return types[type]

def get_id(id):
    if id not in ids:
        return None
    return ids[id]

def getLibrary(page):

    request = LibPageRequest (
        page = page,
        max_results = 30
    )
    print(request)
    ret = []
    for r in lib_client.Library(request).recommendations:
        tp = get_id(r.type)
        type = "All" if not tp else tp

        object = {"id" : r.id, "name" : r.name, "type" : type}
        ret.append(object)
    return ret

def getSuggestions(user,body):
   # print(user)
#    print(request.context['user'])
#    print(request.context['user'])

    r = RecommendationRequest (
        user_id = user,
        max_results = 30,
        types = body["tipos"]
    )
    ret = []
    for r in lib_client.Recommend(r).recommendations:
        tp = get_id(r.type)
        type = "All" if not tp else tp

        object = {"id": r.id, "name": r.name, "type": type}
        ret.append(object)
    return ret

def addItem(body):

    # TODO o enum e o id estavam trocados e estava a lançar um erro, temos que por uma condição e verificar input
    type= body["type"]
    if (type == "BOOK"):

        type = 0
        data = BookData(book_title = body["name"], img_url= body["photoUrl"], book_rating= body["rating"], description= body["description"], genres = category_to_genres(body["category"]) )
        request = AddItemRequest(type=type, book=data)
    elif (type == "SHOW"):
        type = 1
        data = IMDBData(imdb_title=body["name"], img_url=body["photoUrl"], imdb_rating=body["rating"],
                        description=body["description"], genres= category_to_genres(body["category"]), type=body["type"])
        request = AddItemRequest(type=type, imdb=data)

    elif (type == "ANIME"):
        type = 2
        data = AnimeData(anime_title=body["name"], img_url=body["photoUrl"], anime_rating=body["rating"],
                        description=body["description"], genres= category_to_genres(body["category"]))
        request = AddItemRequest( type=type, anime=data)

    else:
        return 'false',405
    return lib_client.AddItem(request).id, body["type"]

def category_to_genres(category):
    lista = []
    for c in category:
        lista.append(c["name"])
    return lista

def getItemById(type,itemId):
    type = get_type(type)
    if type is None: return 'false', 400

    # TODO o enum e o id estavam trocados e estava a lançar um erro, temos que por uma condição e verificar input
    request = ItemId(id = itemId, type=type)
    response= lib_client.GetItem(request)
    if(response.book.book_id == '' and response.imdb.imdb_id == '' and response.anime.anime_id == ''):
        return 'Id Not Found', 400
    if (response.book.book_id != ''):
        category = []
        for cat in response.book.genres:
            category.append(cat)

        return {"id" : response.book.book_id, "name" : response.book.book_title, "type" : "BOOK", "description": response.book.description,
                "photoUrl":response.book.img_url, "category": category, "rating": response.book.book_rating, "likes": response.likes, "seens": response.seens}
    if (response.imdb.imdb_id != ''):
        category = []
        for cat in response.imdb.genres:
            category.append(cat)

        return {"id": response.imdb.imdb_id, "name": response.imdb.imdb_title, "type": "SHOW",
                "photoUrl": response.imdb.img_url, "category": category, "rating": response.imdb.imdb_rating, "likes": response.likes, "seens": response.seens}


    if (response.anime.anime_id != ''):
        category = []
        for cat in response.anime.genres:
            category.append(cat)

        return {"id":response.anime.anime_id, "name":response.anime.anime_title, "type": "ANIME",
                "photoUrl": response.anime.img_url, "category": category, "rating": response.anime.anime_rating, "likes": response.likes, "seens": response.seens}
    return 'Id Not Found', 400

def deleteItem(type,itemId):
    type = get_type(type)
    if type is None: return 'false', 400

    # TODO o enum e o id estavam trocados e estava a lançar um erro, temos que por uma condição e verificar input
    request = ItemIdAndUser(
        id = itemId,
        type = type
    )
    return lib_client.RemoveItem(request).success

def updateItemSeen(user,type,itemId):
    type = get_type(type)
    if type is None: return 'false', 400

    request =  ItemIdAndUser (
        user_id=user,
        id = itemId,
        type = type
    )
    return lib_client.AddSeenItem(request).success

def removeItemSeen(user,type,itemId):
    type = get_type(type)
    if type is None: return 'false', 400

    request =  ItemIdAndUser (
        user_id=user,
        id = itemId,
        type = type
    )
    return lib_client.RemoveSeenItem(request).success

def updateItemLike(user,type,itemId):
    type = get_type(type)
    if type is None: return 'false', 400

    request =  ItemIdAndUser(
        user_id=user,
        id = itemId,
        type = type
    )
    return lib_client.AddLikeItem(request).success

def removeItemLike(user,type,itemId):
    type = get_type(type)
    if type is None: return 'false', 400

    request =  ItemIdAndUser(
        user_id=user,
        id = itemId,
        type = type
    )
    return lib_client.RemoveLikeItem(request).success

# def getViewsOf(type,itemId):
#     type = get_type(type)
#     if not type: return 'false', 400
#
#     request = SeenAndLikeItem(
#         id   = itemId,
#         type = type
#     )
#     r = lib_client.GetSeensItem(request).count
#     return r
#
# def getLikesOf(type,itemId):
#     type = get_type(type)
#     if not type: return 'false', 400
#
#     request = SeenAndLikeItem(
#         id   = itemId,
#         type = type
#     )
#     r = lib_client.GetLikesItem(request).count
#     return r

def getTopTen(type):
    type = get_type(type)
    if not type: return 'false', 400

    request = TopTenRequest(
        type = type
    )
    rs = lib_client.GetTopTen(request).infos
    t = lambda x : { 'id': x.id, 'type': x.type }
    return [ t(r) for r in rs ]