import unittest
import os
import grpc

from imdb_pb2 import *
from imdb_pb2_grpc import IMDBStub

with open("library.key", "rb") as fp:
    library_key = fp.read()
with open("library.pem", "rb") as fp:
    library_cert = fp.read()
with open("ca.pem", "rb") as fp:
    ca_cert = fp.read()
creds = grpc.ssl_channel_credentials(ca_cert, library_key, library_cert)

imdbs_host = os.getenv("IMDBS_HOST", "localhost")
imdbs_channel = grpc.secure_channel(f"{imdbs_host}:50052", creds)
imdbs_client = IMDBStub(imdbs_channel)

class imdbTestCase(unittest.TestCase):

    def test_get_imdb(self):
        imdbs_request = IMDBByIdRequest(imdb_id="606e2683b3fff1da8a207ade")
        self.assertEqual(imdbs_client.SearchById(imdbs_request).imdb_title, "Carmencita")

    def test_remove_imdb(self):
        imdbs_request = IMDBByIdRequest(imdb_id="606e2683b3fff1da8a207ade")
        self.assertEqual(imdbs_client.AddIMDB(imdbs_request).imdb_title, True)

    def test_add_imdb(self):
        imdbs_request = IMDBByIdRequest(imdb_id="606e2683b3fff1da8a207ade")
        self.assertEqual(imdbs_client.RemoveIMDB(imdbs_request).imdb_title, True)

    def test_imdb_search_by_name(self):
        imdbs_request = IMDBByIdRequest(imdb_id="606e2683b3fff1da8a207b6a")
        self.assertEqual(imdbs_client.SearchByName("Buffalo Bill and Escort")[0], imdbs_request)

    def test_imdb_search_by_category(self):
        self.assertEqual(imdbs_client.assertNotEqual("short"), None)
        
if __name__ == '__main__':
    unittest.main()
