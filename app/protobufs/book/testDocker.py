
import os
import grpc
from book_pb2 import *
from book_pb2_grpc import BookStub

book_host = os.getenv("BOOKS_HOST", "localhost")
book_channel = grpc.insecure_channel(f"{book_host}:50051")
book_client = BookStub(book_channel)

request = BooksByNameRequest(name= "Hunger Games",max_results=10)
response = book_client.SearchByName(request)

print(response)