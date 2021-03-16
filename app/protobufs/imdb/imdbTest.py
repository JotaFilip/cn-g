from concurrent import futures

import connexion as connexion
import grpc
import os
from grpc_interceptor import ExceptionToStatusInterceptor
from grpc_interceptor.exceptions import NotFound
# 3rd party modules
from flask import make_response, abort


# from library_pb2 import (
#     Type,
#     BasicInfoResponse,
#     BookData,
#     BookBasicInfo,
#     IMDBData,
# 	IMDBBasicInfo,
# 	AnimeData,
# 	AnimeBasicInfo,
# 	RecommendationRequest,
# 	BookByIdRequest,
# 	IMDBByIdRequest,
# 	AnimeByIdRequest,
# 	SearchByNameRequest,
# 	SearchByCategoryRequest,
#
# )
#import library_pb2_grpc

from imdb_pb2 import *
from imdb_pb2_grpc import IMDBStub

# Acesso ah base de dados

recommendations_host = os.getenv("RECOMMENDATIONS_HOST", "localhost")
#
# with open("client.key", "rb") as fp:
#     client_key = fp.read()
# with open("client.pem", "rb") as fp:
#     client_cert = fp.read()
# with open("ca.pem", "rb") as fp:
#     ca_cert = fp.read()
# creds = grpc.ssl_channel_credentials(ca_cert, client_key, client_cert)
#
# recommendations_channel = grpc.secure_channel(
#     f"{recommendations_host}:443", creds
# )
#books_channel = grpc.insecure_channel(f"{recommendations_host}:50051")
#books_client = BookStub(books_channel)
imdbs_channel = grpc.insecure_channel(f"{recommendations_host}:50052")
imdbs_client = IMDBStub(imdbs_channel)
from flask import Flask, render_template
app = connexion.App(__name__, specification_dir="./")

# @app.route("/")
# def render_homepage():
if __name__ == "__main__":

#################################################

    imdbs_request = IMDBByIdRequest(
        imdb_id="tt0000001"
    )
    imdbs_response = imdbs_client.SearchById(
        imdbs_request
    )
    if(imdbs_response is None):
        print("És burro")
    print(imdbs_response.imdb)
    
    imdbs_request = IMDBByNameRequest(
        name="Stalker",
        max_results= 5
    )
    imdbs_response = imdbs_client.SearchByName(
        imdbs_request
    )
    if(imdbs_response is None):
        print("És esperto")
    print(imdbs_response.imdb[0].imdb_title)
    
    imdbs_request = IMDBByCategoryRequest(
        category= "Action",
        max_results= 5
    )
    
    imdbs_response = imdbs_client.SearchByCategory(
        imdbs_request
    )
    
    if(imdbs_response is None):
        print("És esperto")
    print(imdbs_response.imdb[0].imdb_title)

    
# Create a URL route in our application for "/"
# app.add_api("api.yaml")
# @app.route("/")
# def home():
#     """
#     This function just responds to the browser URL
#     localhost:5000/
#
#     :return:        the rendered template "home.html"
#     """
#     return render_template("home.html")
#
#
# if __name__ == "__main__":
#     app.run(debug=True)
