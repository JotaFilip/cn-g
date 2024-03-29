import unittest
import os
import grpc

from library_pb2 import *
from library_pb2_grpc import LibraryStub

from book_pb2 import *

lib_host = os.getenv("LIBRARY_HOST", "localhost")
lib_channel = grpc.insecure_channel(f"{lib_host}:50050")
lib_client = LibraryStub(lib_channel)

# books_host = os.getenv("BOOKS_HOST", "localhost")
# books_channel = grpc.insecure_channel(f"{books_host}:50051")
# books_client = BookStub(books_channel)

class AnimeTestCase(unittest.TestCase):

    def test_recommend_one(self):
        recommend_request = RecommendationRequest(user_id="1", max_results=30, types=["BOOK"])
        print(lib_client.Recommend(recommend_request).recommendations[0])
        self.assertEqual(len(lib_client.Recommend(recommend_request).recommendations), 30)

    def test_recommend_two(self):
        recommend_request = RecommendationRequest(user_id="1", max_results=30, types=["BOOK", "ANIME"])
        self.assertEqual(len(lib_client.Recommend(recommend_request).recommendations), 30)

    def test_recommend_three(self):
        recommend_request = RecommendationRequest(user_id="1", max_results=30, types=["BOOK", "ANIME", "SHOW"])
        self.assertEqual(len(lib_client.Recommend(recommend_request).recommendations), 30)

    def test_item(self):

        books_request = BookData()
        books_request.book_title = "TestaLibrary"
        books_request.description = "Um livro temporario para testar o library"
        books_request.genres.append("Classics")

        books_request.book_rating = 4.55
        books_request.img_url = "https://images.gr-assets.com/books/1511302904l/890.jpg"



        recommend_request = AddItemRequest( book=books_request)

        book_id = lib_client.AddItem(recommend_request).id
        self.assertTrue(book_id)

        item_id = ItemId(id=book_id, type="BOOK")
        self.assertTrue(lib_client.GetItem(item_id))

        self.assertTrue(lib_client.RemoveItem(item_id))

if __name__ == '__main__':
    unittest.main()
