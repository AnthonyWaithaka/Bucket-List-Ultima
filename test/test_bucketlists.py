# test_client.py
"""unittest file for client module
"""
import unittest

from app.bucketlist import BucketList
from app.activity import Activity

class BucketListTestCase(unittest.TestCase):
    """Several test cases for positive
    use of bucketlists class methods"""
    def setUp(self):
        """Create a new user object for testing
        """
        self.new_user = BucketList('theguy', 'something@yes.com', 'aaa1111')

    def test_create_bucket_list(self):
        """Test that bucket list creation was successful
        """
        new_list = self.new_user.create_bucket_list('List_01', 2018, "January",
                                                    "I feel like a million bucks")
        self.assertIsInstance(new_list, Activity, msg="Bucket List creation unsuccessful")

    def test_view_bucket_list(self):
        """Test that a valid object with saved data is returned
        """
        self.new_user.create_bucket_list('Awesome Adventure', 2030, "January",
                                         "It will be most excellent")
        self.assertIsInstance(self.new_user.view_list('Awesome Adventure'), Activity,
                              msg="View did not return bucket list")

    def test_bucket_list_delete(self):
        """Test for successful deletion of bucket list
        """
        new_list = self.new_user.create_bucket_list('List_02', 2017, "August",
                                                    "This is the big one")
        self.assertEqual(self.new_user.delete_list('List_02'), True, msg="Delete operation failed")

    def test_bucket_list_update(self):
        """Test that bucketlist data can be updated successfully
        First argument must be listname
        Optional arguments are:
        'newlistname'
        'year'
        'month'
        'quote'
        """
        new_list = self.new_user.create_bucket_list('Coco List',
                                                    2017, "August", "This is the big one")
        self.new_user.update_bucketlist('Coco List', newlistname='Coffee List')
        self.assertEqual(new_list.list_name, 'Coffee List', msg="List update failed")
