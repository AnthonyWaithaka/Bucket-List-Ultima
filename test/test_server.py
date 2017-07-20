# test_server.py
"""unittest file for server module
"""
import unittest

from app.server import Server
from app.client import Client
from app.bucketlist import BucketList

class ServerTestCase(unittest.TestCase):
    """Several test cases for positive
    use of server class methods"""
    def setUp(self):
        """Creating a server object for testing
        """
        self.server = Server()

    def test_correct_client_creation(self):
        """Test that a client creation was successful
        """
        new_client = self.server.create_client('something@yes.com', 'guy', 'aaa111', True)
        self.assertIsInstance(new_client, Client, msg="Client creation unsuccessful")

    def test_client_delete(self):
        """Test that client delete was successful
        """
        new_client = self.server.create_client('something2@yes.com', 'guy2', 'aaa113', True)
        self.assertEqual(self.server.delete_client(new_client), None, msg="Delete unsuccessful")

    def test_client_view(self):
        """Test that client view was successful
        """
        new_client = self.server.create_client('something3@yes.com', 'guy3', 'aaa114', True)
        new_client.create_bucket_list("guy3's list", 2012, "December",
                                      "I have a good feeling about this", True)
        guy4_list = self.server.view_client('guy3')
        self.assertIsInstance(guy4_list[0], BucketList, msg="List return unsuccessful")

    def test_client_search(self):
        """Test that client search was successful
        """
        self.server.create_client('something4@yes.com', 'guy4', 'aaa115', True)
        self.assertEqual(self.server.search_client('something4@yes.com'),
                         'guy4', msg="Search return unsuccessful")

    def test_client_view_bucket_list(self):
        """Test that bucket list was returned successfully
        """
        new_client = self.server.create_client('something5@yes.com', 'guy5', 'aaa116', True)
        new_client.create_bucket_list('List_01', 2018, "January",
                                      "I feel like a million bucks", True)
        self.assertIsInstance(self.server.view_bucket_list('List_01', 'guy5'),
                              BucketList, msg="Bucket list creation unsuccessful")

    def test_client_reset_details(self):
        """Test that client data can be updated successfully
        First argument must be username
        Optional arguments are:
        'newusername'
        'oldpassword'
        'newpassword'
        'oldemail'
        'newemail'
        """
        new_client = self.server.create_client('something6@yes.com', 'guy6', 'aaa117', True)
        new_client.create_bucket_list('Cartoon binge', 2018, "January",
                                      "I feel like a million bucks", True)
        self.server.reset_client('guy6', newusername='guy7')
        bucket_list = self.server.view_bucket_list('Cartoon binge', 'guy7')
        self.assertEqual(bucket_list.list_name, 'Cartoon binge', msg="Username change unsuccessful")
