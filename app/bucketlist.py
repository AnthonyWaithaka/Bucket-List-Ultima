# bucketlist.py
"""Bucketlist module -
See documentation for use
"""

from app.activity import Activity

class BucketList(object):
    """BucketList class -
    Has specific methods for activity management
    """
    def __init__(self, list_name, list_year, list_month, list_quote, set_active):
        self.list_name = list_name
        self.list_year = list_year
        self.list_month = list_month
        self.list_quote = list_quote
        self.set_active = set_active
        self.activity_list = {}    #activity_list will have {name:object} format

    def create_activity(self, activity_name, media_path_list, achieved_status):
        """Creates a new activity and stores it
        """
        for i in list(self.activity_list.keys()):
            if i == activity_name:
                return None
        new_activity = Activity(activity_name, media_path_list, achieved_status)
        self.activity_list.update({activity_name:new_activity})
        return new_activity
