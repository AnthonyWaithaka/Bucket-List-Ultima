# test_client.py
"""unittest file for client module
"""
import unittest

from app.client import Client
from app.bucketlist import BucketList

class ServerTestCase(unittest.TestCase):
    """Several test cases for positive
    use of server class method"""
    def setUp(self):
        """Creating a client object for testing
        """
        self.client = Client('theguy', 'something@yes.com', 'aaa1111')

    def test_create_bucket_list(self):
        """Test that bucket list creation was successful
        """
        new_list = self.client.create_bucket_list('List_01', 2018, "January",
                                                  "I feel like a million bucks", True)
        self.assertIsInstance(new_list, BucketList, msg="Bucket List creation unsuccessful")

    def test_view_bucket_list(self):
        """Test that a valid object is returned
        """
        self.client.create_bucket_list('Awesome Adventure', 2030, "January",
                                       "It will be most excellent", False)
        self.assertIsInstance(self.client.view_list('Awesome Adventure'), BucketList,
                              msg="View did not return bucket list")

    def test_bucket_list_delete(self):
        """Test for successful deletion of bucket list
        """
        new_list = self.client.create_bucket_list('List_02', 2017, "August",
                                                  "This is the big one", True)
        self.assertEqual(self.client.delete_list(new_list), True, msg="Delete operation failed")

    def test_bucket_list_follow(self):
        """Test for successful entry in follow list
        """
        self.client.create_bucket_list('List_03', 2017, "August", "This is the big one", True)
        self.assertEqual(self.client.follow_list('List06'), True, msg="List follow failed")

    def test_bucket_list_unfollow(self):
        """Test for successful unfollow procedure
        """
        self.client.create_bucket_list('List_04', 2017, "August", "This is the big one", True)
        self.client.follow_list('List04')
        self.assertEqual(self.client.follow_list('List04'), False, msg="List unfollow failed")

    def test_bucket_list_reset(self):
        """Test that bucketlist data can be updated successfully
        First argument must be listname
        Optional arguments are:
        'newlistname'
        'year'
        'month'
        'quote'
        """
        new_list = self.client.create_bucket_list('Coco List',
                                                  2017, "August", "This is the big one", True)
        self.client.reset_bucketlist('Coco List', newlistname='Coffee List')
        self.assertEqual(new_list.list_name, 'Coffee List', msg="List update failed")
