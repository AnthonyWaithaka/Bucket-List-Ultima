# test_server.py
"""unittest file for server module
"""
import unittest

from app.user import User
from app.bucketlist import BucketList
from app.activity import Activity

class UserTestCase(unittest.TestCase):
    """Several test cases for positive
    use of server class methods"""
    def setUp(self):
        """Creating an User object for testing
        """
        self.app = User()

    def test_user_signup_was_correct(self):
        """Test that a client creation was successful
        """
        new_user = self.app.create_user('something@yes.com', 'guy', 'aaa111', True)
        self.assertIsInstance(new_user, BucketList, msg="Client creation unsuccessful")

    def test_user_delete(self):
        """Test that user delete was successful
        """
        new_user = self.app.create_user('something2@yes.com', 'guy2', 'aaa113', True)
        self.assertEqual(self.app.delete_user(new_user), None, msg="Delete unsuccessful")

    def test_user_view(self):
        """Test that user view was successful
        """
        new_user = self.app.create_user('something3@yes.com', 'guy3', 'aaa114', True)
        new_user.create_bucket_list("guy3's list", 2012, "December",
                                    "I have a good feeling about this")
        guy4_list = self.app.view_user('guy3')
        self.assertIsInstance(guy4_list[0], Activity, msg="List return unsuccessful")

    def test_user_search(self):
        """Test that user search was successful
        """
        self.app.create_user('something4@yes.com', 'guy4', 'aaa115', True)
        self.assertEqual(self.app.search_user('something4@yes.com'),
                         'guy4', msg="Search return unsuccessful")

    def test_user_view_bucket_list(self):
        """Test that bucket list was returned successfully
        """
        new_user = self.app.create_user('something5@yes.com', 'guy5', 'aaa116', True)
        new_user.create_bucket_list('List_01', 2018, "January",
                                      "I feel like a million bucks")
        self.assertIsInstance(self.app.view_bucket_list('List_01', 'guy5'),
                              Activity, msg="Bucket list creation unsuccessful")

    def test_user_reset_details(self):
        """Test that client data can be updated successfully
        First argument must be username
        Optional arguments are:
        'newusername'
        'oldpassword'
        'newpassword'
        'oldemail'
        'newemail'
        """
        new_user = self.app.create_user('something6@yes.com', 'guy6', 'aaa117', True)
        new_user.create_bucket_list('Cartoon binge', 2018, "January",
                                    "I feel like a million bucks")
        self.app.reset_user('guy6', newusername='guy7')
        bucket_list = self.app.view_bucket_list('Cartoon binge', 'guy7')
        self.assertEqual(bucket_list.list_name, 'Cartoon binge', msg="Username change unsuccessful")
