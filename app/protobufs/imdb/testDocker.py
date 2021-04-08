
import os
import grpc
from imdb_pb2 import *
from imdb_pb2_grpc import IMDBStub

imdb_host = os.getenv("IMDBS_HOST", "localhost")
imdb_channel = grpc.insecure_channel(f"{imdb_host}:50052")
imdb_client = IMDBStub(imdb_channel)

request = IMDBByNameRequest(name= "Carmencita",max_results=10)
response = imdb_client.SearchByName(request)

print(response)