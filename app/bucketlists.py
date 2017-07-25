# user.py
"""User module -
See documentation for use
"""

from .newbucketlist import NewBucketList

class BucketLists(object):
    """BucketLists class -
    Has specific methods for bucket list management
    """
    def __init__(self, user_name, user_email, user_password):
        """
        The list and dictionary are for holding non-persistent data
        To indicate the owner of the BucketLists
        """
        self.user_name = user_name
        self.user_email = user_email
        self.user_password = user_password
        self.bucket_lists = {}

    def create_bucket_list(self, list_name, list_year, list_month, list_quote):
        """Create bucket list with arguments from constructor and
        store data in structures within the scope of class instance
        """
        for key in list(self.bucket_lists.keys()):
            if list_name == key:
                return None

        new_bucket_list = NewBucketList(list_name, list_year, list_month, list_quote)
        self.bucket_lists.update({list_name:new_bucket_list})
        return new_bucket_list

    def view_list(self, listname):
        """Return the object type BucketList
        for a given bucket list name
        """
        for key, obj in self.bucket_lists.items():
            if key == listname:
                return obj
        return None

    def delete_list(self, bulist):
        """Deletes bucket list
        and scans for remnants
        """
        for key, obj in self.bucket_lists.items():
            if obj == bulist:
                del self.bucket_lists[key]
                for i in list(self.bucket_lists.values()):
                    if i == bulist:
                        return False
                for j in list(self.bucket_lists.values()):
                    if j == key:
                        return False
                return True

    def update_bucketlist(self, listname, **kwargs):
        """Update bucket list data -
        newlistname
        year
        month
        quote
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
