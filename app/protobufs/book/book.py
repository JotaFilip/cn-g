from concurrent import futures
#from pymongo import MongoClient
from copy import copy

import grpc
from grpc_interceptor import ExceptionToStatusInterceptor
from grpc_interceptor.exceptions import NotFound
import sqlite3
con = sqlite3.connect('Books', check_same_thread=False)
from book_pb2 import (
    BookData,
    BookDataList,
    BookByIdRequest,
    BooksByNameRequest,
    BooksByCategoryRequest, BookResponse,

)
import book_pb2_grpc

# Acesso ah base de dados

books_database = {
    "id": ["1", "2", "3", "4", "5"],
    "name": ["a", "b", "c", "d", "e"],
    "genre": ["luta", "acao", "romance", "luta", "acao"]
}


class BookService(book_pb2_grpc.BookServicer):
    def SearchById(self, request, context):
        cur = con.cursor()
        cur.execute('SELECT book_id,book_title,genres,book_rating FROM book_data WHERE book_id=?', (request.book_id,))

        book = cur.fetchone()
        print(book)
        if book is None:
            raise NotFound("Id not found")
        send = BookData(book_id =book[0], book_title = book[1],genres = book[2], book_rating = book[3])
        print(send)
        return BookResponse(book=send)
        
    def SearchByName(self, request, context):
    
        #if request.name not in books_database:
        if request.book_id not in books_database["name"]:
            raise NotFound("Name not found")
        cur = con.cursor()
        cur.execute('SELECT book_id,book_title,genres,book_rating FROM book_data WHERE book_title LIKE ? ', ( request.name,))
        #books_with_name = books_database[request.name]
        book_with_id = books_database["name"][request.name]
        num_results = min(request.max_results, len(books_with_name))
        searched_books = random.sample(books_with_name, num_results)

        return BookDataList(books=searched_books)
        
    def SearchByCategory(self, request, context):
    
        #if request.category not in books_database:
        
        if request.book_id not in books_database["genre"]:
            raise NotFound("Category not found")
        cur = con.cursor()
        cur.execute('SELECT book_id,book_title,genres,book_rating FROM book_data WHERE genres LIKE ? ', ("%" + request.category + "%",))
        #books_with_category = books_database[request.category]
        book_with_id = books_database["genre"][request.category]
        num_results = min(request.max_results, len(books_with_name))
        searched_books = random.sample(books_with_category, num_results)

        return BookDataList(books=searched_books)
        


def serve():
    interceptors = [ExceptionToStatusInterceptor()]
    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=10), interceptors=interceptors
    )
    book_pb2_grpc.add_BookServicer_to_server(
        BookService(), server
    )
    
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
