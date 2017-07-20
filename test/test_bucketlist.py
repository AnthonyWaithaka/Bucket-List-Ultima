# test_bucketlist.py
"""unittest file for bucketlist module
"""
#create activity #view activity #edit activity #compute deadline #view comments

import unittest

from app.bucketlist import BucketList
from app.activity import Activity

class ServerTestCase(unittest.TestCase):
    """Several test cases for 'happy' use of bucketlist methods
    """
    def setUp(self):
        """Initialization of test object
        """
        self.bucket_list = BucketList('List 01', 2012, "March", "The quote", True)

    def test_create_activity(self):
        """Test for successful creation of activity object
        """
        new_activity = self.bucket_list.create_activity('climb mt everest',
                                                        ['.app/templates/static/images/climbmt'],
                                                        False)
        self.assertIsInstance(new_activity, Activity, msg="Activity not created")

    def test_view_activity(self):
        """Test for successful return of activity object data
        """
        pass

    def test_edit_activity(self):
        """Test for successful edit of activity object data
        """
        pass