
import os
import grpc
from library_pb2 import *
from library_pb2_grpc import LibraryStub

library_host = os.getenv("LIBRARY_HOST", "localhost")
library_channel = grpc.insecure_channel(f"{library_host}:50050")
library_client = LibraryStub(library_channel)

request = LibPageRequest(page=0,max_results=10)
response = library_client.Library(request)

print(response)