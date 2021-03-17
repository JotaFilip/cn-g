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

from book_pb2 import *
from book_pb2_grpc import BookStub

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
books_channel = grpc.insecure_channel(f"{recommendations_host}:50051")
books_client = BookStub(books_channel)
#animes_channel = grpc.insecure_channel(f"{recommendations_host}:50051")
#animes_client = AnimeStub(animes_channel)
from flask import Flask, render_template
app = connexion.App(__name__, specification_dir="./")

# @app.route("/")
# def render_homepage():
if __name__ == "__main__":

#################################################
    print("Request - Find book by ID: 6050c7a8b8a16ddf981960dd")
    books_request = BookByIdRequest(
        book_id="6050c7a8b8a16ddf981960dd"
    )
    books_response = books_client.SearchById(
        books_request
    )
    if(books_response is None):
        print("Response: Book not found")
    else:
        print("Response:", books_response.book)

    print("Request - Find book by name: The Hunger Games")
    
    books_request = BooksByNameRequest(
        name= "The Hunger Games",
        max_results= 5
    )
    books_response = books_client.SearchByName(
        books_request
    )
    if(books_response is None):
        print("Response: Book not found")
    else:
        print("Response: Title:", books_response.books[0].book_title, "Genre:", books_response.books[0].genres[0], "Rating:", books_response.books[0].book_rating)
    
    books_request = BooksByCategoryRequest(
        category= "Fiction",
        max_results= 5
    )
    print("Request - Find book by category: Fiction")
    
    books_response = books_client.SearchByCategory(
        books_request
    )
    
    
    if(books_response is None):
        print("Response: Book not found")
    else:
        print("Response ")
        for book in books_response.book:
             print("Title:", book.book_title, "Genre:", books_response.books[0].genres[0], "Rating:", books_response.books[0].book_rating)

    
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
