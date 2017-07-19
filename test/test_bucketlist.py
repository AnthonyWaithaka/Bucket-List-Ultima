# test_bucketlist.py

#create activity #view activity #edit activity #compute deadline #view comments

import unittest

from app.bucketlist import bluBucketList
from app.activity import bluActivity

class ServerTestCase(unittest.TestCase):
    def setUp(self):
        self.bList = bluBucketList('List 01', 2012, "March", "The quote", True)