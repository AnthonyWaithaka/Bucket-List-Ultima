# client.py
"""Client module -
See documentation for use
"""

from app.bucketlist import BucketList

class Client(object):
    """Client class -
    Has specific methods for bucket list management
    """
    def __init__(self, user_name, user_email, user_password):
        """
        The list and dictionary are for holding non-persistent data
        """
        self.user_name = user_name
        self.user_email = user_email
        self.user_password = user_password
        self.bucket_lists = {}
        self.followed_lists = []


    def create_bucket_list(self, list_name, list_year, list_month, list_quote, set_active):
        """Creates bucket list with arguments from constructor and
        stores data in structures within the scope of class instance
        """
        for key in list(self.bucket_lists.keys()):
            if list_name == key:
                return None

        #verifying that the month is not a number:
        if not list_month.isalpha():
            return None

        new_bucket_list = BucketList(list_name, list_year, list_month, list_quote, set_active)
        self.bucket_lists.update({list_name:new_bucket_list})
        return new_bucket_list

    def view_list(self, listname):
        """Returns the object type BucketList
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

    def follow_list(self, list_name):
        """Stores or removes a bucket list
        from followed lists when called
        """
        for i in self.followed_lists:
            if list_name == i:
                self.followed_lists.remove(list_name)
                return False
        self.followed_lists.append(list_name)
        return True

    def reset_username(self, username):
        """Replace the current username
        """
        self.user_name = username
        return None

    def reset_useremail(self, useremail):
        """Replace the current useremail
        """
        self.user_email = useremail
        return None

    def reset_userpassword(self, userpassword):
        """Replace the current userpassword
        """
        self.user_password = userpassword
        return None

    def reset_bucketlist(self, listname, **kwargs):
        """Reset bucket list data
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
