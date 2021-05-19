import unittest
import os
import grpc

from account_pb2 import *
from account_pb2_grpc import AccountStub

accounts_host = os.getenv("ACCOUNTS_HOST", "localhost")
accounts_channel = grpc.insecure_channel(f"{accounts_host}:50055")
accounts_client = AccountStub(accounts_channel)

class MyTestCase(unittest.TestCase):

    def test_seen(self):
        seen_and_like_info = SeenAndLikeInfo(user_id="608f3ba995657a00692583ae", id="606e252aebddc73ebfb15542",
                                             type="ANIME", categories=["Action"])

        accounts_client.Remove_Seen(seen_and_like_info)

        self.assertTrue(accounts_client.Seen(seen_and_like_info).success)

        seen_and_like_item = SeenAndLikeItem(id="606e252aebddc73ebfb15542", type="ANIME")
        self.assertNotEqual(accounts_client.GetSeensItem(seen_and_like_item), 0)

        self.assertTrue(accounts_client.Remove_Seen(seen_and_like_info).success)

    def test_like(self):
        seen_and_like_info = SeenAndLikeInfo(user_id="608f3ba995657a00692583ae", id="606e252aebddc73ebfb15542",
                                             type="ANIME", categories=["Action"])

        accounts_client.Remove_Like(seen_and_like_info)

        self.assertTrue(accounts_client.Like(seen_and_like_info).success)

        seen_and_like_item = SeenAndLikeItem(id="606e252aebddc73ebfb15542", type="ANIME")
        self.assertNotEqual(accounts_client.GetLikesItem(seen_and_like_item), 0)

        self.assertTrue(accounts_client.Remove_Like(seen_and_like_info).success)

    def test_seen_not_exists_id(self):
        seen_and_like_info = SeenAndLikeInfo(user_id="608f3ba995657a00692583ae", id="000000000000000000000000",
                                             type="ANIME", categories="Action")
        self.assertFalse(accounts_client.Seen(seen_and_like_info).success)

    def test_seen_not_exists_user(self):
        seen_and_like_info = SeenAndLikeInfo(user_id="111111a995657a0069111111", id="606e252aebddc73ebfb15542",
                                             type="ANIME", categories="Action")
        self.assertFalse(accounts_client.Seen(seen_and_like_info).success)

    def test_views_and_likes_count(self):
        user_id = UserId(id="606e252aebddc73ebfb15542")
        self.assertIsNotNone(accounts_client.GetContagemLikesAndViews(user_id).tuples)

    def test_create_user(self):
        username_request = UpdateUserRequest(user_id="608f8ptn95657a0069258000", new_username="Leitao")
        self.assertTrue(accounts_client.UpdateUser(username_request).success)

        username_request = UsernameRequest(username="Leitao")
        self.assertEqual("Leitao", accounts_client.GetUserByName(username_request).username)

        user_request = UserRequest(user_id="608f8ptn95657a0069258000")
        self.assertTrue(accounts_client.DeleteUser(user_request).success)

if __name__ == '__main__':
    unittest.main()
