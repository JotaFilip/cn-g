
# Library API

from library_pb2 import *
from library_pb2_grpc import LibraryStub

lib_host = os.getenv("LIBRARY_HOST", "localhost")
lib_channel = grpc.insecure_channel(f"{lib_host}:50054")
lib_client = LibraryStub(lib_channel)

# TODO
# how to handle the user_id situation

def getLibrary(page):

    request = LibPageRequest (
        page = page,
        max_results = 30
    )
    return lib_client.Library(request)

def getSuggestions():

    request = RecommendationRequest (
        user_id = 0,            # TODO
        max_results = 30,
        types = []              # TODO
    )
    return lib_client.Recommend(request)

def addItem(body):

    request = AddItemRequest(body)
    return lib_client.AddItem(request)

def getItemById(itemId):

    request = GetItemRequest(id = itemId)
    return lib_client.GetItem(request)

def deleteItem(itemId):

    request = RemoveItemRequest (
        page = page,
        max_results = 30
    )
    return lib_client.RemoveItem(request)

def updateItemSeen(itemId):

    request = SeenRequest (
        id = itemId,
    )
    return lib_client.UpdateSeenItem(request)

def updateItemLike(itemId):

    request = LikeRequest (
        id = itemId
    )
    return lib_client.UpdateLikeItem(request)
