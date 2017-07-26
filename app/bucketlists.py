# user.py
"""Bucketlists class -
Store data for all bucketlists the user has and
manage the bucketlists.
"""

from .newbucketlist import NewBucketList

class BucketLists(object):
    """BucketLists class -
    Stores records for the owner of the Bucketlists and
    the bucketlist names alongside their objects in the object
    attributes.
    Has methods to create, read, update and delete all bucketlists.
    """
    def __init__(self, user_name, user_email, user_password):
        """Initialization -
        The dictionary has the name of the bucketlist as the key and
        the object itself as the respective value.
        """
        self.user_name = user_name
        self.user_email = user_email
        self.user_password = user_password
        self.bucket_lists = {}

    def create_bucket_list(self, list_name, list_year, list_month, list_quote):
        """Create a bucketlist object -
        Returns None if the name of the bucketlist already exists in the records.
        Returns the new bucketlist object if it was successfully created.
        """
        for key in list(self.bucket_lists.keys()):
            if list_name == key:
                return None

        new_bucket_list = NewBucketList(list_name, list_year, list_month, list_quote)
        self.bucket_lists.update({list_name:new_bucket_list})
        return new_bucket_list

    def view_list(self, listname):
        """Read a bucketlist object using the bucketlist name-
        Return the bucketlist object if the name exists in the records.
        Return None otherwise.
        """
        for key, obj in self.bucket_lists.items():
            if key == listname:
                return obj
        return None

    def delete_list(self, bulist):
        """Delete a bucketlist -
        Return True if the bucketlist was deleted successfully.
        Return False if the bucketlist name still exists.
        """
        for key in list(self.bucket_lists.keys()):
            if key == bulist:
                del self.bucket_lists[key]
                for i in list(self.bucket_lists.keys()):
                    if i == bulist:
                        return False
                return True

    def update_bucketlist(self, listname, **kwargs):
        """Update bucket list data using the following argument values:
        1. listname (required) - The name of the bucketlist to be updated
        2. newlistname
        3. year
        4. month
        5. quote
        Return None if the data update was successful.
        Return False otherwise.
        """
        newlistname = kwargs.get('newlistname', None)
        newlistyear = kwargs.get('year', None)
        newlistmonth = kwargs.get('month', None)
        newlistquote = kwargs.get('quote', None)
        for i in list(self.bucket_lists.keys()):
            if i == listname:
                if newlistyear is not None:
                    self.bucket_lists[listname].list_year = newlistyear

                if newlistmonth is not None:
                    self.bucket_lists[listname].list_month = newlistmonth

                if newlistquote is not None:
                    self.bucket_lists[listname].list_quote = newlistquote

                if newlistname is not None:
                    self.bucket_lists[newlistname] = self.bucket_lists.pop(listname)
                    self.bucket_lists[newlistname].list_name = newlistname

                return None
        return False
