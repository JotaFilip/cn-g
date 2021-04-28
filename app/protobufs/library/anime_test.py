import unittest
import os
import grpc

from anime_pb2 import *
from anime_pb2_grpc import AnimeStub

# with open("library.key", "rb") as fp:
#     library_key = fp.read()
# with open("library.pem", "rb") as fp:
#     library_cert = fp.read()
# with open("ca.pem", "rb") as fp:
#     ca_cert = fp.read()
# creds = grpc.ssl_channel_credentials(ca_cert, library_key, library_cert)
#
# animes_host = os.getenv("ANIMES_HOST", "localhost")
# animes_channel = grpc.secure_channel(f"{animes_host}:50053", creds)
# animes_client = AnimeStub(animes_channel)

animes_host = os.getenv("ANIMES_HOST", "localhost")
animes_channel = grpc.insecure_channel(f"{animes_host}:50053")
animes_client = AnimeStub(animes_channel)

class AnimeTestCase(unittest.TestCase):

    def test_get_anime(self):
        animes_request = AnimeByIdRequest(anime_id="606e252aebddc73ebfb15500")
        self.assertEqual(animes_client.SearchById(animes_request).anime_title, "Inu X Boku Secret Service")

    def test_remove_anime(self):
        animes_request = AnimeByIdRequest(anime_id="606e252aebddc73ebfb15500")
        self.assertEqual(animes_client.RemoveAnime(animes_request).success, True)

    def test_add_anime(self):
        animes_request = AnimeByIdRequest(anime_id="606e252aebddc73ebfb15500")
        self.assertEqual(animes_client.AddAnime(animes_request).success, True)
        
    def test_anime_search_by_name(self):
        animes_request = AnimeByIdRequest(anime_id="606e252aebddc73ebfb15522")
        self.assertEqual(animes_client.SearchByName("One Piece").animes[0], animes_request)

    def test_anime_search_by_category(self):
        self.assertEqual(animes_client.assertNotEqual("Action"), None)
        
if __name__ == '__main__':
    unittest.main()
