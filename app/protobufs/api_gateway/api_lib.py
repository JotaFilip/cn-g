
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
            type = "Book"
        if (r.type == 1):
            type = "Show"
        if (r.type == 2):
            type = "Anime"

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

def getItemById(itemId):

    request = ItemId(id = itemId)
    return lib_client.GetItem(request)

def deleteItem(itemId):

    request = ItemId (
        id = itemId
    )
    return lib_client.RemoveItem(request)

def updateItemSeen(itemId):

    request = ItemId (
        id = itemId,
    )
    return lib_client.UpdateSeenItem(request)

def updateItemLike(itemId):

    request = ItemId (
        id = itemId
    )
    return lib_client.UpdateLikeItem(request)
