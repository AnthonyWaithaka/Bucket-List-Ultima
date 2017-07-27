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
        login_response = self.app.post('/login/', data={'logemail':'guy3', 'logpassword':'aaa3'},
                                                        follow_redirects=True)
        self.assertEqual(login_response.status_code, 302, msg="Did not return bucket_lists page")

    def test_login_data(self):
        """Test session data when user logs in to
        their account
        """
        response = self.app.post('/signup/', data={'email':'guy4@yes.com',
                                                   'user':'guy4', 'pass':'aaa4',
                                                   'pass2':'aaa4'})
        login_response = self.app.post('/login/', data={'logemail':'guy4', 'logpassword':'aaa4'})
        self.assertEqual(session['loginuser'], 'guy4', msg="User did not log in successfully")

if __name__ == '__main__':
    unittest.main()