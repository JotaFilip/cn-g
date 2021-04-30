import unittest
import os
import grpc

from book_pb2 import *
from book_pb2_grpc import BookStub

#with open("library.key", "rb") as fp:
#    library_key = fp.read()
#with open("library.pem", "rb") as fp:
#    library_cert = fp.read()
#with open("ca.pem", "rb") as fp:
#    ca_cert = fp.read()
#creds = grpc.ssl_channel_credentials(ca_cert, library_key, library_cert)

#books_host = os.getenv("BOOKS_HOST", "localhost")
#books_channel = grpc.secure_channel(f"{books_host}:50051", creds)
#books_client = BookStub(books_channel)

books_host = os.getenv("BOOKS_HOST", "localhost")
books_channel = grpc.insecure_channel(f"{books_host}:50051")
books_client = BookStub(books_channel)


class bookTestCase(unittest.TestCase):

    def test_get_animes(self):
        books_request = GetBooksRequest(page=1, max_results=32)
        self.assertEqual(len(books_client.GetBooks(books_request).books), 32)

    def test_add_book(self):
        books_request = BookData()
        books_request.book_title="Testa"
        books_request.description="Um livro temporario para testar"
        books_request.genres.append("Classics")
        
        books_request.book_rating = 4.55
        books_request.img_url = "https://images.gr-assets.com/books/1511302904l/890.jpg"
        
        id = books_client.AddBook(books_request).book_id
        
        self.assertNotEqual(id, None)
        
        books_request = BookByIdRequest(book_id=id)
        self.assertEqual(books_client.RemoveBook(books_request).success, True)

    def test_get_book(self):
        books_request = BookByIdRequest(book_id="606e25ad5e927a606f534284")
        self.assertEqual(books_client.SearchById(books_request).book_title, "Of Mice and Men")

    def test_book_search_by_name(self):
        books_request = BooksByNameRequest(name="Of Mice and Men", max_results=32)
        self.assertEqual(books_client.SearchByName(books_request).books[0].book_id, "606e25ad5e927a606f534284")

    def test_book_search_by_category(self):
        books_request = BooksByCategoryRequest(category="Classics", max_results=32)
        self.assertNotEqual(len(books_client.SearchByCategory(books_request).books), 0)
                
if __name__ == '__main__':
    unittest.main()
