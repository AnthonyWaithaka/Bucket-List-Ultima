# test_bucketlist.py
"""unittest file for activity methods and data
"""

import unittest

from app.bucketlists import BucketLists
from app.newbucketlist import NewBucketList

class ServerTestCase(unittest.TestCase):
    """Several test cases for 'happy' use of bucketlist methods
    """
    def setUp(self):
        """Initialization of test objects
        """
        self.new_user = BucketLists('guy1', 'guy@yes.com', 'aaa')

    def test_create_activity(self):
        """Test for successful creation of activity object
        """
        new_list = self.new_user.create_bucket_list('List 01', 2012, "March", "The quote")
        new_activity = new_list.create_activity('climb mt everest')
        self.assertEqual(new_list.activity_list[0], 'climb mt everest', msg="Activity not created")

    def test_edit_activity_name(self):
        """Test for successful edit of activity object data
        """
        new_list = self.new_user.create_bucket_list('List 01', 2012, "March", "The quote")
        new_list.create_activity('climb mt everest')
        new_list.update_activity('climb mt everest', 'descend mt everest')
        self.assertEqual(new_list.activity_list[0],
                         'descend mt everest', msg="Activity status not changed")

    def test_deleted_activity(self):
        """Test for successful deletion
        """
        new_list = self.new_user.create_bucket_list('List 01', 2012, "March", "The quote")
        new_list.create_activity('climb mt everest')
        new_list.delete_activity('climb mt everest')
        self.assertEqual(new_list.activity_list, [], msg="Activity not deleted")
