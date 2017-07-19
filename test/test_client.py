# test_client.py

import unittest

from app.client import bluClient
from app.bucketlist import bluBucketList

class ServerTestCase(unittest.TestCase):
    def setUp(self):
        self.bClient = bluClient('theguy','something@yes.com','aaa1111')
        self.bClient2 = bluClient('thatguy', 'something@no.com', 'bbb1111')

    def test_create_bucket_list_name_repetition(self):
        new_list = self.bClient.createBList('List_01', 2018, "January", "I feel like a million bucks", True)
        new_list2 = self.bClient.createBList('List_02', 2018, "January", "I feel like a million bucks", True)
        self.assertNotEqual(new_list2, False, "Name already used")
    
    def test_view_bucket_list_one_object(self):
        self.bClient.createBList('Awesome Adventure', 2030, "January", "It will be most excellent", False)
        AA_list = self.bClient.viewList('Awesome Adventure')
        self.assertIsInstance(AA_list, bluBucketList, "View Failed")

    def test_view_bucket_list_fail(self):
        self.bClient.createBList('Awesome Adventure 2', 2030, "January", "It will be most excellent", False)
        AA_list = self.bClient.viewList('Awesome Adventure 2')
        self.assertNotEqual(AA_list, None, "View Failed")    

    def test_bucket_list_delete_fail(self):
        new_list = self.bClient.createBList('List_03', 2017, "August", "This is the big one", True)
        self.assertEqual(self.bClient.deleteList(new_list), True, "Delete Failed")

    def test_bucket_list_delete_name_not_exist(self):
        new_list = self.bClient.createBList('List_04', 2017, "August", "This is the big one", True)
        self.assertNotEqual(self.bClient.deleteList(new_list), 2, "Remnant Data - List Name")
    
    def test_bucket_list_delete_object_not_exist(self):
        new_list = self.bClient.createBList('List_05', 2017, "August", "This is the big one", True)
        self.assertNotEqual(self.bClient.deleteList(new_list), 3, "Remnant Data - Object")

    def test_bucket_list_follow_fail(self):
        new_list = self.bClient.createBList('List_06', 2017, "August", "This is the big one", True)
        self.assertEqual(self.bClient.followList('List06'), True, "List follow failed")
    
    def test_bucket_list_follow_unfollow(self):
        new_list = self.bClient.createBList('List_07', 2017, "August", "This is the big one", True)
        self.bClient.followList('List07')
        self.assertEqual(self.bClient.followList('List07'), 2, "List unfollow failed")