# test_bucketlist.py
"""unittest file for activity methods and data
"""

import unittest

from app.bucketlists import BucketLists
from app.newbucketlist import Activity

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
        new_list = self.new_user.create_bucket_list('List 01', 2012, "March", "The quote", True)
        new_activity = new_list.create_activity('climb mt everest',
                                                ['.app/templates/static/images/climbmt'], False)
        self.assertIsInstance(new_activity, Activity, msg="Activity not created")

    def test_view_activity(self):
        """Test for successful return of activity object data
        Can return either 'media_list' or 'status'
        """
        new_list = self.new_user.create_bucket_list('List 01', 2012, "March", "The quote", True)
        new_list.create_activity('climb mt everest',
                                 ['.app/templates/static/images/climbmt'], False)
        activity_data = new_list.view_activity('climb mt everest', 'media_list')
        self.assertEqual(activity_data[0], '.app/templates/static/images/climbmt',
                         msg="Activity property not returned")

    def test_edit_activity_status(self):
        """Test for successful edit of activity object data
        """
        new_list = self.new_user.create_bucket_list('List 01', 2012, "March", "The quote", True)
        new_list.create_activity('climb mt everest',
                                 ['.app/templates/static/images/climbmt'],
                                 False)
        new_list.edit_status('climb mt everest')
        self.assertEqual(new_list.view_activity('climb mt everest', 'status'),
                         True, msg="Activity status not changed")

    def test_deleted_activity(self):
        """Test for successful deletion
        """
        new_list = self.new_user.create_bucket_list('List 01', 2012, "March", "The quote", True)
        new_list.create_activity('climb mt everest',
                                 ['.app/templates/static/images/climbmt'],
                                 False)
        new_list.delete_activity('climb mt everest')
        self.assertEqual(new_list.view_activity('climb mt everest', 'status'),
                                                None, msg="Activity not deleted")
