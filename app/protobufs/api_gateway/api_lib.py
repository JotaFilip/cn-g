
# Library API
import os
from book_pb2 import *
from anime_pb2 import *
from imdb_pb2 import *
from library_pb2 import *
from library_pb2_grpc import LibraryStub
import grpc
from grpc_interceptor import ExceptionToStatusInterceptor
from flask import Flask, jsonify, request, url_for, abort, g

lib_host = os.getenv("LIBRARY_HOST", "localhost")
lib_channel = grpc.insecure_channel(f"{lib_host}:50050",options=(('grpc.enable_http_proxy', 0),))
lib_client = LibraryStub(lib_channel)

print(f"{lib_host}:50050")

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

def getSuggestions(body):

    request = RecommendationRequest (
        user_id = g.user_id,
        max_results = 30,
        types = body["tipos"]
    )
    ret = []
    for r in lib_client.Recommend(request).recommendations:
        type = "All"
        if (r.type == 0):
            type = "BOOK"
        if (r.type == 1):
            type = "SHOW"
        if (r.type == 2):
            type = "ANIME"

        object = {"id": r.id, "name": r.name, "type": type}
        ret.append(object)
    return ret

def addItem(body):
    type= body["type"]
    if (type == "BOOK"):

        type = 0
        data = BookData(book_title = body["name"], img_url= body["photoUrl"], book_rating= body["rating"], description= body["description"], genres = category_to_genres(body["category"]) )
        request = AddItemRequest(user_id=g.user_id, type=type, book=data)
    if (type == "SHOW"):
        data = IMDBData(imdb_title=body["name"], img_url=body["photoUrl"], imdb_rating=body["rating"],
                        description=body["description"], genres= category_to_genres(body["category"]), type=body["type"])
        request = AddItemRequest(user_id=g.user_id, type=type, imdb=data)
        type = 1
    if (type == "ANIME"):
        data = AnimeData(anime_title=body["name"], img_url=body["photoUrl"], anime_rating=body["rating"],
                        description=body["description"], genres= category_to_genres(body["category"]))
        request = AddItemRequest(user_id=g.user_id, type=type, anime=data)
        type = 2

    return lib_client.AddItem(request).success

def category_to_genres(category):
    lista = []
    for c in category:
        lista.append(c["name"])
    return lista

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

    if (type == "BOOK"):
        type = 0
    if (type == "SHOW"):
        type = 1
    if (type == "ANIME"):
        type = 2

    request = ItemIdAndUser(
        user_id=g.user_id,
        id = itemId,
        type = type
    )
    return lib_client.RemoveItem(request).success

def updateItemSeen(type,itemId):

    if (type == "BOOK"):
        type = 0
    if (type == "SHOW"):
        type = 1
    if (type == "ANIME"):
        type = 2

    request =  ItemIdAndUser (
        user_id = g.user_id,
        id = itemId,
        type = type
    )
    return lib_client.AddSeenItem(request).success

def updateItemLike(type,itemId):

    if (type == "BOOK"):
        type = 0
    if (type == "SHOW"):
        type = 1
    if (type == "ANIME"):
        type = 2

    request =  ItemIdAndUser(
        user_id=g.user_id,
        id = itemId,
        type = type
    )
    return lib_client.AddLikeItem(request).success
