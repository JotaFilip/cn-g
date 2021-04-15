import unittest
import os
import grpc

from book_pb2 import *
from book_pb2_grpc import BookStub

with open("library.key", "rb") as fp:
    library_key = fp.read()
with open("library.pem", "rb") as fp:
    library_cert = fp.read()
with open("ca.pem", "rb") as fp:
    ca_cert = fp.read()
creds = grpc.ssl_channel_credentials(ca_cert, library_key, library_cert)

books_host = os.getenv("BOOKS_HOST", "localhost")
books_channel = grpc.secure_channel(f"{books_host}:50051", creds)
books_client = BookStub(books_channel)

class bookTestCase(unittest.TestCase):
    def test_get_book(self):
        books_request = BookByIdRequest(book_id="606e25ad5e927a606f534284")
        self.assertEqual(books_client.SearchById(books_request).book_title, "Of Mice and Men")

    def test_remove_book(self):
        books_request = BookByIdRequest(book_id="606e25ad5e927a606f534284")
        self.assertEqual(books_client.SearchById(books_request).book_title, True)

    def test_add_book(self):
        books_request = BookByIdRequest(book_id="606e25ad5e927a606f534284")
        self.assertEqual(books_client.SearchById(books_request).book_title, True)

if __name__ == '__main__':
    unittest.main()
