
import os
import grpc
from anime_pb2 import *
from anime_pb2_grpc import AnimeStub

anime_host = os.getenv("animeS_HOST", "localhost")
anime_channel = grpc.insecure_channel(f"{anime_host}:50053")
anime_client = AnimeStub(anime_channel)

request = AnimeByNameRequest(name= "Bleach",max_results=10)
response = anime_client.SearchByName(request)

print(response)