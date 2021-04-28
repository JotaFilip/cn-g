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




    def test_add_anime(self):

        animes_request = AnimeData()
        animes_request.anime_title="Testa"
        animes_request.genres.append("Action")
        
        #animes_request.genres.extend(["Action", "Adventure"])
        #animes_request.genres = ["Action"]
        
        #-------------------------------------------------------
        #animes_genres = AnimeByIdRequest(anime_id="606e252aebddc73ebfb15542")
        #animes_request.genres.extend(animes_client.SearchById(animes_genres).genres)
        #-------------------------------------------------------
        
        #animes_request.genres[:] = ["Action"]
        
        animes_request.anime_rating = 4.55
        animes_request.img_url="https://myanimelist.cdn-dena.com/images/anime/6/73245.jpg"
        
        #animes_request = AnimeData(anime_id="lqh8252mebdd8plebfb15522", anime_title="Testa", genres = extend(["Action"]), anime_rating = 4.55, img_url="https://myanimelist.cdn-dena.com/images/anime/6/73245.jpg")
        
        id = animes_client.AddAnime(animes_request).anime_id
        
        self.assertNotEqual(id, None)
        
        animes_request = AnimeByIdRequest(anime_id=id)
        self.assertEqual(animes_client.RemoveAnime(animes_request).success, True)

    def test_get_anime(self):
        animes_request = AnimeByIdRequest(anime_id="606e252aebddc73ebfb15542")
        self.assertEqual(animes_client.SearchById(animes_request).anime_title, "Lupin III: Lupin Ikka Seizoroi")

    def test_anime_search_by_name(self):
        animes_request = AnimeByNameRequest(name="One Piece", max_results=32)
        self.assertEqual(animes_client.SearchByName(animes_request).animes[0].anime_id, "606e252aebddc73ebfb15522")

    def test_anime_search_by_category(self):
        animes_request = AnimeByCategoryRequest(category="Action", max_results=32)
        self.assertNotEqual(len(animes_client.SearchByCategory(animes_request).animes), 0)

if __name__ == '__main__':
    unittest.main()
