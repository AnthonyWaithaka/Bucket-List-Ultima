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

    def view_activity(self, activity_name, *args):
        """Given an activity name as argument
        and a property type
        Returns the respective property type data
        """
        for i in list(self.activity_list.keys()):
            if i == activity_name:
                for arg in args:
                    if arg == 'media_list':
                        return self.activity_list[activity_name].media_path_list
                    elif arg == 'status':
                        return self.activity_list[activity_name].status_
        return None

    def edit_status(self, activity_name):
        """Given an activity name as argument
        Can edit the achieved status of
        the respective activity object
        """
        for i in list(self.activity_list.keys()):
            if i == activity_name:
                self.activity_list[activity_name].flip_status()
        return None

    def delete_activity(self, activity_name):
        """Deletes an activity
        """
        for i in list(self.activity_list.keys()):
            if i == activity_name:
                del self.activity_list[activity_name]
        return None

    def reset_activity(self, activity_name, newname):
        """Reset activity name
        """
        for i in list(self.activity_list.keys()):
            if i == activity_name:
                self.activity_list[newname] = self.activity_list.pop(activity_name)
                self.activity_list[newname].activity_name = newname
