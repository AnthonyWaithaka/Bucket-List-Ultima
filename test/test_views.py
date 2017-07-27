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
        response = self.app.post('/signup/', data={'email':'guy@yes.com',
                                                   'user':'guy', 'pass':'aaa',
                                                   'pass2':'aaa'})
        self.assertEqual(response.status_code, 200, msg="Did not return sign_up page")

    def test_signup_data(self):
        """Test return value when user creates
        a new account
        """
        response = self.app.post('/signup/', data={'email':'guy@yes.com', 'user':'guy',
                                                   'pass':'aaa', 'pass2':'aaa'})
        self.assertTrue('login' in response.get_data(as_text=True), msg="Did not create account")

    def test_login_status_code(self):
        """Test HTTP GET request when user logs in to
        their account
        """
        response = self.app.post('/signup/', data={'email':'guy@yes.com',
                                                   'user':'guy', 'pass':'aaa',
                                                   'pass2':'aaa'})
        login_response = self.app.post('/login/', data={'logemail':'guy', 'logpassword':'aaa'})
        self.assertEqual(login_response.status_code, 200, msg="Did not return bucket_lists page")

if __name__ == '__main__':
    unittest.main()