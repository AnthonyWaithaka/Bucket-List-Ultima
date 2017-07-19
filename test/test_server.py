# test_server.py
"""
unittest file for server module
"""
import unittest

from app.server import bluServer
from app.client import bluClient
from app.bucketlist import bluBucketList

class ServerTestCase(unittest.TestCase):
    def setUp(self):
        self.bServer = bluServer()

    def test_email_is_valid(self):
        self.assertNotEqual(self.bServer.validateEmail('something@yes.com'), False, "Not a Valid Email Address")

    def test_create_client_tAndC_fail(self):
        new_client = self.bServer.createClient('something@yes.com', 'thisguy', 'aaa1111', True)
        self.assertNotEqual(new_client, 1, "Must Accept Terms and Conditions")

    def test_create_client_email_valid(self):
        new_client = self.bServer.createClient('something@yes.com', 'thisguy', 'aaa1111', True)
        self.assertNotEqual(new_client, 2, "Invalid Email Address")

    def test_create_client_email_repetition(self):
        new_client = self.bServer.createClient('something@yes.com', 'thisguy', 'aaa1111', True)
        new_client2 = self.bServer.createClient('something@no.com', 'thatguy', 'bbb1112', True)
        self.assertNotEqual(new_client2, 3, "Client Email address already in use")

    def test_create_client_password_repetition(self):
        new_client = self.bServer.createClient('something1@yes.com', 'whichguy', 'aaa1113', True)
        new_client2 = self.bServer.createClient('something1@no.com', 'anotherguy', 'aaa1114', True)
        self.assertNotEqual(new_client2, 4, "Client Password already in use")

    def test_create_client_username_repetition(self):
        new_client = self.bServer.createClient('something2@yes.com', 'thisone', 'aaa1115', True)
        new_client2 = self.bServer.createClient('something2@no.com', 'thatone', 'aaa1116', True)
        self.assertNotEqual(new_client2, 5, "Client Username already in use")

    def test_client_is_valid_object(self):
        new_client = self.bServer.createClient('something3@yes.com', 'theseguys', 'aaa1117', True)
        new_client2 = self.bServer.createClient('something3@no.com', 'thoseguys', 'aaa1118', True)
        self.assertIsInstance(new_client2, bluClient, "Invalid Client Object")
    #Observation, cannot use the same data pairs as previous test function. It will raise an error

    def test_client_delete_fail(self):
        new_client = self.bServer.createClient('something4@yes.com', 'theseguys', 'aaa1119', True)
        self.assertEqual(self.bServer.deleteClient(new_client), True, "Delete Failed")

    def test_client_delete_id_not_exist(self):
        new_client = self.bServer.createClient('something6@yes.com', 'guy2', 'aaa1121', True)
        self.assertNotEqual(self.bServer.deleteClient(new_client), 2, "Remnant Data")
    
    def test_client_delete_id_still_exist(self):
        new_client = self.bServer.createClient('something7@yes.com', 'guy3', 'aaa1122', True)
        self.assertNotEqual(self.bServer.deleteClient(new_client), 3, "Remnant Data")
    
    def test_client_view_fail(self):
        new_client = self.bServer.createClient('something8@yes.com', 'guy4', 'aaa1123', True)
        new_client.createBList("guy4's list", 2012, "December", "I have a good feeling about this", True)
        guy4_lists = self.bServer.viewClient('guy4')
        self.assertIsInstance(guy4_lists[0], bluBucketList, "View Failed")

    def test_client_view_id_not_exist(self):
        new_client = self.bServer.createClient('something9@yes.com', 'guy5', 'aaa1124', True)
        self.assertNotEqual(self.bServer.viewClient('guy5'), 1, "Username does not exist")
    
    def test_client_search_fail(self):
        new_client = self.bServer.createClient('something10@yes.com', 'guy6', 'aaa1125', True)
        self.assertEqual(self.bServer.searchClient('something10@yes.com'), 'guy6', "Search Failed")
    
    def test_client_search_id_not_exist(self):
        new_client = self.bServer.createClient('something11@yes.com', 'guy7', 'aaa1126', True)
        self.assertNotEqual(self.bServer.searchClient('something11@yes.com'), False, "Username does not exist")

    def test_client_view_bList_not_exist(self):
        new_client = self.bServer.createClient('something12@yes.com', 'guy8', 'aaa1127', True)
        new_list = new_client.createBList('List_01', 2018, "January", "I feel like a million bucks", True)
        self.assertNotEqual(self.bServer.viewbList('List_01','guy8'), None, "Bucket list does not exist")