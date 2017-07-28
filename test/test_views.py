# test_views.py
"""unittest file for views functions
"""
from app import APP
from flask import session
import unittest

class ViewsTestCase(unittest.TestCase):
    """Several test cases for functionality
    in views
    """
    @classmethod
    def setUpClass(cls):
        """Set up objects and data for the test suite
        """
        pass

    @classmethod
    def tearDownClass(cls):
        """Clean up the data from the tests
        """
        pass

    def setUp(self):
        """Create a test client
        """
        self.app = APP.test_client()
        self.app.testing = True

    def tearDown(self):
        """Clean up the data from the tests
        """
        self.app.data = {}
        self.app.free_id = 0

    def test_index_status_code(self):
        """Send HTTP GET request to the app
        on index
        """
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200, msg="Index page was not rendered")

    def test_signup_status_code(self):
        """Test HTTP GET request when user creates
        a new account
        """
        response = self.app.post('/signup/', data={'email':'guy1@yes.com',
                                                   'user':'guy1', 'pass':'aaa1',
                                                   'pass2':'aaa1'})
        self.assertEqual(response.status_code, 200, msg="Did not return sign_up page")

    def test_signup_data(self):
        """Test return value when user creates
        a new account
        """
        response = self.app.post('/signup/', data={'email':'guy2@yes.com', 'user':'guy2',
                                                   'pass':'aaa2', 'pass2':'aaa2'})
        self.assertTrue('login' in response.get_data(as_text=True), msg="Did not create account")

    def test_login_status_code(self):
        """Test HTTP GET request when user logs in to
        their account
        """
        response = self.app.post('/signup/', data={'email':'guy3@yes.com',
                                                   'user':'guy3', 'pass':'aaa3',
                                                   'pass2':'aaa3'})
        login_response = self.app.post('/login/', data={'logemail':'guy3', 'logpassword':'aaa3'})
        self.assertEqual(login_response.status_code, 200, msg="Did not enter login verification page")

    def test_bucketlists_status_code(self):
        """Test HTTP GET request when user navigates to their account's bucket
        list page
        """
        response = self.app.post('/signup/', data={'email':'guy4@yes.com', 'user':'guy4',
                                                   'pass':'aaa4', 'pass2':'aaa4'})
        login_response = self.app.post('/login/', data={'logemail':'guy4',
                                                        'logpassword':'aaa4'})
        bucketlist_page_request = self.app.get('/mylists')
        self.assertEqual(bucketlist_page_request.status_code, 302,
                         msg="Did not render bucketlists page")

    def test_list_created_status_code(self):
        """Test HTTP GET request when user creates a new bucketlist
        """
        response = self.app.post('/signup/', data={'email':'guy5@yes.com', 'user':'guy5',
                                                   'pass':'aaa5', 'pass2':'aaa5'})
        login_response = self.app.post('/login/', data={'logemail':'guy5',
                                                        'logpassword':'aaa5'})
        new_bucketlist_response = self.app.post('/newlist', data={'newlistname':'list_01',
                                                                  'list_year':'2018',
                                                                  'list_month':'3',
                                                                  'list_quote':'zzz'})
        bucketlist_page_request = self.app.get('/mylists')
        self.assertEqual(bucketlist_page_request.status_code, 302,
                         msg="Did not render bucket_lists page")

    def test_list_created_correct_data(self):
        """Test data exists when user creates a new bucketlist with an invalid date input
        """
        response = self.app.post('/signup/', data={'email':'guy6@yes.com', 'user':'guy6',
                                                   'pass':'aaa6', 'pass2':'aaa6'})
        login_response = self.app.post('/login/', data={'logemail':'guy6',
                                                        'logpassword':'aaa6'})
        new_bucketlist_response = self.app.post('/newlist', data={'newlistname':'list_02',
                                                                  'list_year':'2017',
                                                                  'list_month':'3',
                                                                  'list_quote':'zzz'})
        bucketlist_page_request = self.app.get('/mylists')
        self.assertTrue('deadline passed' in bucketlist_page_request.get_data(as_text=True),
                        msg="Did not create new list")

if __name__ == '__main__':
    unittest.main()
