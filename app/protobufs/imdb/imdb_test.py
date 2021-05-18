import unittest
import os
import grpc

from imdb_pb2 import *
from imdb_pb2_grpc import IMDBStub

#with open("library.key", "rb") as fp:
#    library_key = fp.read()
#with open("library.pem", "rb") as fp:
#    library_cert = fp.read()
#with open("ca.pem", "rb") as fp:
#    ca_cert = fp.read()
#creds = grpc.ssl_channel_credentials(ca_cert, library_key, library_cert)

#imdbs_host = os.getenv("IMDBS_HOST", "localhost")
#imdbs_channel = grpc.secure_channel(f"{imdbs_host}:50052", creds)
#imdbs_client = IMDBStub(imdbs_channel)

imdbs_host = os.getenv("IMDBS_HOST", "localhost")
imdbs_channel = grpc.insecure_channel(f"{imdbs_host}:50052")
imdbs_client = IMDBStub(imdbs_channel)

class imdbTestCase(unittest.TestCase):

    def test_get_imdbs(self):
        imdbs_request = GetIMDBsRequest(page=1, max_results=32)
        self.assertEqual(len(imdbs_client.GetIMDBs(imdbs_request).imdbs), 32)

    def test_add_imdb(self):
        imdbs_request = IMDBData()
        imdbs_request.imdb_title="Testa"
        imdbs_request.genres.append("Documentary")
        
        imdbs_request.imdb_rating = 4.55
        imdbs_request.type = "short"
        
        id = imdbs_client.AddIMDB(imdbs_request).imdb_id
        
        self.assertNotEqual(id, None)
        
        imdbs_request = IMDBByIdRequest(imdb_id=id)
        self.assertEqual(imdbs_client.RemoveIMDB(imdbs_request).success, True)

    def test_remove_imdb_invalid_id(self):
        imdbs_request = IMDBByIdRequest(imdb_id="")
        self.assertEqual(imdbs_client.RemoveIMDB(imdbs_request).success, False)

    def test_get_imdb(self):
        imdbs_request = IMDBByIdRequest(imdb_id="606e2683b3fff1da8a207ade")
        self.assertEqual(imdbs_client.SearchById(imdbs_request).imdb_title, "Carmencita")

    def test_get_imdb_not_exists(self):
        imdbs_request = IMDBByIdRequest(imdb_id="000000000000000000000000")
        self.assertEqual(imdbs_client.SearchById(imdbs_request), IMDBData())

    def test_get_imdb_invalid_id(self):
        imdbs_request = IMDBByIdRequest(imdb_id="")
        self.assertEqual(imdbs_client.SearchById(imdbs_request), IMDBData())

    def test_imdb_search_by_name(self):
        imdbs_request = IMDBByNameRequest(name="Buffalo Bill and Escort", max_results=32)
        self.assertEqual(imdbs_client.SearchByName(imdbs_request).imdbs[0].imdb_id, "606e2683b3fff1da8a207b6a")

    def test_imdb_search_by_name_not_exists(self):
        imdbs_request = IMDBByNameRequest(name="teste123 name not exists 123 $$$", max_results=32)
        self.assertFalse(imdbs_client.SearchByName(imdbs_request).imdbs)

    def test_imdb_search_by_category(self):
        imdbs_request = IMDBByCategoryRequest(category="Documentary", max_results=32)
        self.assertNotEqual(len(imdbs_client.SearchByCategory(imdbs_request).imdbs), 0)

    def test_imdb_search_by_category_not_exists(self):
        imdbs_request = IMDBByCategoryRequest(category="teste123 category not exists 123 $$$", max_results=32)
        self.assertEqual(len(imdbs_client.SearchByCategory(imdbs_request).imdbs), 0)

if __name__ == '__main__':
    unittest.main()
